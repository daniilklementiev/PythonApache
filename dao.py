# Data Access Layer
import logging
import mysql.connector
import db_ini

db_connection = None

def connect_db() :
    global db_connection
    if not db_connection :
        db_connection = mysql.connector.connect(**db_ini.connection_params)
    return db_connection

class Products:
    def do_get(  ):
        # logging.info('Get works')
        
        ret = []
        sql = "SELECT * FROM products"
        try :
            db = connect_db()
            with db.cursor() as cursor :
                cursor.execute(sql)
                for row in cursor:
                    ret.append( dict( zip(cursor.column_names, map( str, row ) ) ) )
        except mysql.connector.Error as err :
            logging.error('SQL error', {'sql': sql, 'err': err})
            raise RuntimeError( str(err) )
        except Exception as err :
            logging.error('Unknown error', {'err': err})
            raise RuntimeError( str(err) )
        else:
            return ret
        
    def add(product: dict) :
        try:
            db = connect_db()
            sql = "INSERT INTO products (name, price, image_url) VALUES (%(name)s, %(price)s, %(image_url)s)"
            with db.cursor() as cursor :
                cursor.execute(sql, product)
            db.commit()
        except mysql.connector.Error as err :
            logging.error('SQL error', {'sql': sql, 'err': err})
            raise RuntimeError( str(err) )
        except Exception as err :
            logging.error('Unknown error', {'err': err})
            raise RuntimeError( str(err) )


class Cart :       
    def add(self, cart_item: dict) :
        try:
            db = connect_db()
            sql = "SELECT * FROM carts WHERE id_product=%s"
            with db.cursor() as cursor :
                cursor.execute( sql, (str(cart_item['id_product']),) )
                row = cursor.fetchall()
            cart_item_from_db = dict( zip( cursor.column_names, map( str, row[0] ) ) ) if len(row) > 0 else None
            if cart_item_from_db != None:
                cart_item['cnt'] += 1
                sql = "UPDATE carts SET cnt=%s WHERE id_product=%s"
                with db.cursor() as cursor :
                    cursor.execute( sql, (cart_item['cnt'], cart_item['id_product'],) )
            else:
                sql = "INSERT INTO carts (`id_user`, `id_product`, `cnt`) VALUES ( %(id_user)s, %(id_product)s, %(cnt)s )"
                with db.cursor() as cursor :
                    cursor.execute( sql, cart_item )
            db.commit()
        except mysql.connector.Error as err :
            logging.error(str(err), {'sql': sql, 'err': err})
            raise RuntimeError(err)
        except Exception as err:
            logging.error(str(err), { 'err': str(err)})
            raise RuntimeError(err)
    
    def get_items( id_user: str ) -> list:
        ret = []
        sql = "SELECT c.*, p.name, p.price, p.image_url FROM carts c JOIN products p ON c.id_product = p.id WHERE id_user=%s"
        try :
            db = connect_db()
            with db.cursor( dictionary=True) as cursor :
                cursor.execute(sql, (id_user,))
                return [ row for row in cursor ]
        except mysql.connector.Error as err :
            logging.error('SQL error', {'sql': sql, 'err': err})
            raise RuntimeError( str(err) )
        except Exception as err :
            logging.error('Unknown error', {'err': err})
            raise RuntimeError( str(err) )

class Auth:
    def get_user_id_by_token( token: str ) -> str | None:
        sql = "SELECT COUNT(u.id) FROM users u WHERE u.id=%s"
        try :
            db = connect_db()
            with db.cursor() as cursor :
                cursor.execute( sql, ( token, ) )
                cnt = cursor.fetchone()[0]
        except mysql.connector.Error as err :
            logging.error('SQL error', {'sql': sql, 'err': err})
            raise RuntimeError( str(err) )
        except Exception as err :
            logging.error('Unknown error', {'err': err})
            raise RuntimeError( str(err) )
        else :
            return token if cnt == 1 or cnt == "1" else None