import logging
logging.basicConfig(
        filename='logs.txt', 
        level=logging.INFO, 
        format='[%(asctime)s] - [%(levelname)s] in [%(filename)s::%(lineno)d] : %(message)s with %(args)s',
        datefmt='%Y-%m-%d %H:%M:%S')
import os
import json
import sys
import re

class ApiController :
    
    def __init__ (self) -> None:
        self.db_connection = None


    def serve(self) -> None:
        '''Основной метод для обработки запросов с разделением в соответствии с методом запроса''' 
        method = os.environ.get('REQUEST_METHOD', '') # GET
        action = f"do_{method.lower()}" # do_get
        attr = getattr(self, action, None) # self.do_get
        if attr is None :
            self.send_response( 405, "Method Not Allowed", { "message": f"Method '{method}' not allowed" } )
        else: 
            attr()

    
    def send_response(self, 
                      status_code:int=200, 
                      reason_phrase:str=None, 
                      body:object=None,
                      data:object=None,
                      meta:object=None) -> None:
        status_header = f"Status: {status_code} {reason_phrase if reason_phrase else ''}"
        print(status_header)
        print("Content-Type: application/json; charset=utf-8")
        print("Connection: close")
        print() # end of headers
        if body :
            print(json.dumps(body) if body else '', end='')
        else :
            print( json.dumps( { "meta": meta, "data": data } ), end='')
        exit()

    def get_request_json(self) -> dict:
        request_body = sys.stdin.read().encode('cp1251').decode('utf-8')
        return json.loads(request_body)
    

    def get_auth_header_or_exit(self, auth_scheme:str="Basic " ) -> str :
        auth_header_name = 'HTTP_AUTHORIZATION'
        if not auth_scheme.endswith(' ') :
            auth_scheme += ' ' 
        if not auth_header_name :
            self.send_response( 401, "Unauthorized", { "message": "Missing required header 'Authorization'" } )
        auth_header_value = os.environ[auth_header_name]
        if not auth_header_value.startswith(auth_scheme) :
            self.send_response( 401, "Unauthorized", { "message": "Invalid Authorization scheme" } )

        return auth_header_value[len(auth_scheme):]

    def get_bearer_token_or_exit(self) :
        token = self.get_auth_header_or_exit( auth_scheme="Bearer " )
        token_pattern = r"^[0-9a-f-]+$" 
        if not re.match(token_pattern, token) :
            self.send_response( 401, "Unauthorized", { "message": "Invalid token" } )

        return token