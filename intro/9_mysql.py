# Data bases. MySQL
import mysql.connector
import hashlib

db_ini = {
    'host': 'localhost',
    'port': 3306,
    'user': 'py202_user',
    'password': 'pass_202',
    'database': 'py202',
    'charset': 'utf8mb4',
    'use_unicode': True,
    'collation': 'utf8mb4_unicode_ci',
}

db_connection = None

def connect_db():
    global db_connection
    try:
        db_connection = mysql.connector.connect(**db_ini)
    except mysql.connector.Error as error:
        print(error)
    else:
        print("Connection OK")
    
def show_databases():
    global db_connection
    sql = "SHOW DATABASES"
    with db_connection.cursor() as db_cursor:
        db_cursor.execute(sql)
        print(db_cursor.column_names)
        for db in db_cursor:
            print(db)
        
def create_users():
    global db_connection
    sql = """CREATE TABLE users (
        `id` BIGINT UNSIGNED PRIMARY KEY DEFAULT (UUID_SHORT()),
        `login` VARCHAR(32) NOT NULL UNIQUE,
        `password` CHAR(32) NOT NULL,
        `avatar` VARCHAR(256) DEFAULT NULL
        ) ENGINE=InnoDB, DEFAULT CHARSET=utf8mb4 COLLATE utf8mb4_unicode_ci"""
    with db_connection.cursor() as db_cursor:
        db_cursor.execute(sql)
        print(db_cursor.column_names)
        for db in db_cursor:
            print(db)

def add_user(login:str, password:str, avatar:int|None = None) :
    # password = hashlib.md5( password.encode() ).hexdigest()
    sql = "INSERT INTO users (login, password, avatar) VALUES(%s, %s, %s)"
    password = hashlib.md5( password.encode() ).hexdigest()
    try:
        with db_connection.cursor() as cursor:
            cursor.execute(sql, (login, password, avatar))
        db_connection.commit()
    except mysql.connector.Error as err:
        print(err)
        return
    else:
        print("Insert user OK")

def create_products():
    global db_connection
    sql = """CREATE TABLE products (
        `id` BIGINT UNSIGNED PRIMARY KEY DEFAULT (UUID_SHORT()),
        `name`      VARCHAR(32)  NOT NULL,
        `price`     FLOAT        NOT NULL,
        `image_url` VARCHAR(256) DEFAULT NULL
        ) ENGINE=InnoDB, DEFAULT CHARSET=utf8mb4 COLLATE utf8mb4_unicode_ci"""
    with db_connection.cursor() as db_cursor:
        db_cursor.execute(sql)
        print(db_cursor.column_names)
        for db in db_cursor:
            print(db)

def add_product(name:str, price:float, image_url:str = None) :
    sql = "INSERT INTO products (name, price, image_url) VALUES(%s, %s, %s)"
    try:
        with db_connection.cursor() as cursor:
            cursor.execute(sql, (name, price, image_url))
        db_connection.commit()
    except mysql.connector.Error as err:
        print(err)
        return
    else:
        print("Insert product OK")  

def create_cart():
    global db_connection
    sql = """CREATE TABLE carts (
        `id`             BIGINT UNSIGNED PRIMARY KEY DEFAULT (UUID_SHORT()),
        `id_user`        BIGINT UNSIGNED  NOT NULL,
        `id_product`     BIGINT UNSIGNED  NOT NULL,
        `cnt`            INT              NULL DEFAULT 1
        ) ENGINE=InnoDB, DEFAULT CHARSET=utf8mb4 COLLATE utf8mb4_unicode_ci"""
    with db_connection.cursor() as db_cursor:
        db_cursor.execute(sql)
        print(db_cursor.column_names)
        for db in db_cursor:
            print(db)

def main() -> None:
    connect_db()
    #create_users()
    #show_databases()
    user = {
        "login":"user",
        "password":"123",
        "avatar":"user1.png"
    }
    product = {
        "name":"apple",
        "price": 22.50,
        "image_url":"apple.png"
    }
    # add_user(**user)
    # create_products()
    # add_product(**product)
    #create_cart()
    
    
        
    
if __name__ == '__main__':
    main()