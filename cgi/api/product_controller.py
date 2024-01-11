import api_controller
import sys
import json
import logging
sys.path.append('../../')
import dao

class ProductController(api_controller.ApiController):
 

    def do_get( self ):
        try :
            products = dao.Products.do_get()
        except RuntimeError as err:
            self.send_response(
                meta={ "service": "product", "count": 0, "status": 500 },
                data={ "message": "Internal server error, see logs for details" } )
        else :
            self.send_response(
                meta={ "service": "product", "count": len(products), "status": 200 },
                data=products )
    

    def do_post(self) : 
        product = self.get_request_json()
        if not 'name' in product and 'price' in product :
            self.send_response( 400, "Bad request", { "message": "Missing required parameter 'name'" } )
        try:
            dao.Products().add(product)
        except :
            self.send_response(
                meta={ "service": "product", "count": 0, "status": 500 },
                data={ "message": "Internal server error, see logs for details" } )
        else :
            self.send_response(
                meta={ "service": "product", "count": 1, "status": 201 },
                data={ "message" : "Created"} )    
        self.send_response(body=product)


    def do_put(self):
        product = self.get_request_json()
        if not 'name' in product and 'price' in product :
            self.send_response( 400, "Bad request", { "message": "Missing required parameter 'name'" } )
        self.send_response(body=product)


'''
    REST - REpresentational State Transfer - архитектура для работы с API
    = в наших задачах - веб-API (или HTTP)
    - единый интерфейс
        = все запросы имеют похожую семантику (роль методов GET, POST...)
        = у них схожие принципы передачи данных (структура Query параметров, тела, заголовков)
        = единый формат ответа (в т.ч. ошибок)
    - отсутствие сохранения состояния
        = каждый запрос - отдельное действие
        = сервер не хранит состояние клиента (в т.ч. авторизацию)

    200 OK
    {
        meta: {
            service: 'product',
            status: 200,
            count: 15
        },
        data: [
            {product1},
            ...
            {product15}
        ]
    }
    
'''