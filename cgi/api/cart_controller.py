#!C:\Python311\python.exe
import api_controller
import sys
import json
import logging
sys.path.append('../../')
import dao

class CartController(api_controller.ApiController):
    def __init__(self) -> None :
        self.service_name = "cart"
    
    
    def do_post( self ):
        token = self.get_bearer_token_or_exit()
        user_id = dao.Auth.get_user_id_by_token(token)
        if user_id is None :
            self.send_response( 
                meta={ "service": self.service_name, "count": 0, "status": 403 },
                data={ "message": "Token rejected" }
            )
        body = self.get_request_json()        
        if not 'id_product' in body :
            self.send_response( 
                meta={ "service": self.service_name, "count": 0, "status": 400 },
                data={ "message": "Missing required parameter 'id_product'" }
             )
        try :
            cart_item = { 'id_product' : body['id_product'], 'id_user' : user_id, 'cnt' : 1 }
            dao.Cart.add(dao.Cart(), cart_item)
        except :
            self.send_response(
                meta={ "service": self.service_name, "count": 0, "status": 500 },
                data={ "message": "Internal server error, see logs for details" } )
        else :
            self.send_response(
                meta={ "service": self.service_name, "count": cart_item["cnt"], "status": 200 },
                data=cart_item)