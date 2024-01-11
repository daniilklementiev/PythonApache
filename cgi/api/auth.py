#!C:\Python311\python.exe
import base64
import os
import mysql.connector
import json
import sys
import re
import hashlib
sys.path.append('../../') # добавляем путь к модулям
import db_ini

db_connection = None

def connect_db_or_exit():
    global db_connection
    if not db_connection:
        try:
            db_connection = mysql.connector.connect(**db_ini.connection_params)
        except mysql.connector.Error as error:
            send_response(500, "Internal Server Error", {"message": f"Database connection error: {error}"})
    return db_connection


def stringify (func) :
    def wrapper(*args, **kwargs) :
        return str(func(*args, **kwargs))
    return wrapper

def get_auth_header_or_exit( auth_scheme:str="Basic " ) -> str :
    auth_header_name = 'HTTP_AUTHORIZATION'
    if not auth_scheme.endswith(' ') :
        auth_scheme += ' ' 
    if not auth_header_name :
        send_response( 401, "Unauthorized", { "message": "Missing required header 'Authorization'" } )
    auth_header_value = os.environ[auth_header_name]
    if not auth_header_value.startswith(auth_scheme) :
        send_response( 401, "Unauthorized", { "message": "Invalid Authorization scheme" } )

    return auth_header_value[len(auth_scheme):]

@stringify
def get_bearer_token_or_exit() :
    token = get_auth_header_or_exit( auth_scheme="Bearer " )
    token_pattern = r"^[0-9a-f-]+$" 
    if not re.match(token_pattern, token) :
        send_response( 401, "Unauthorized", { "message": "Invalid token" } )
    
    return token

def send_response(status_code:int=200, reason_phrase:str=None, body:object=None) -> None:
    status_header = f"Status: {status_code} {reason_phrase if reason_phrase else ''}"
    print(status_header)
    print("Content-Type: application/json; charset=utf-8")
    print("Connection: close")
    print() # end of headers
    print(json.dumps(body) if body else '')
    exit()

def query_params():
    qs = os.environ['QUERY_STRING']
    return { k: v for k, v in (pair.split('=', 1) for pair in qs.split('&')) } if len(qs) > 0 else {} 

def do_get() -> None :
    # params = query_params()
    # login, password = params['login'], params['password']
    # if not 'login' in params :
    #     send_response( 400, "Bad request", { "message": "Missing required parameter 'login'" } )
    # if not 'password' in params :
    #     send_response( 400, "Bad request", { "message": "Missing required parameter 'password'" } )
    # Изменяем алгоритм аутентификации на Baisc Auth
    auth_token = get_auth_header_or_exit("Basic")
    try:
        login, password = base64.b64decode( auth_token, validate=True ).decode().split(':', 1)
    except (TypeError, UnicodeDecodeError):
        send_response( 401, "Unauthorized", { "message": "Invalid token" } )

    sql = "SELECT u.* FROM users u WHERE u.`login`=%s AND u.`password`=%s"
    try :
        with connect_db_or_exit().cursor() as cursor :
            cursor.execute( sql, ( login,
                hashlib.md5( password.encode() ).hexdigest() ) )
            row = cursor.fetchone()
            if row == None :
                send_response( 401, "Unauthorized", { "message": "Credentials rejected" } )
            user_data = dict(zip(cursor.column_names, row))
            
            send_response( body={ "scheme": "Bearer", "token": str(user_data['id']) } )
    except mysql.connector.Error as err :
        send_response( 500, "Internal Server Error", str(err) )   # TODO: прибрати str(err)
   
def do_post() -> None :
    
    token = get_bearer_token_or_exit()
    send_response( body= token )


def main() :
    method = os.environ.get('REQUEST_METHOD', '')
    match method :
        case 'GET':
            do_get()
        case 'POST':
            do_post()
        case _:
            send_response(501, "Not Implemented", {"message": f"Method {method} not supported"})

if __name__ == '__main__':
    main()