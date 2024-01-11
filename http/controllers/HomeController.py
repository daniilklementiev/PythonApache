import appsetting   
from starter import MainHandler
import inspect
import os
import time
import sys
from ViewController import ViewController
sys.path.append('./')
import dao
class HomeController(ViewController) : 
    
    def __init__ (self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.short_name = self.__class__.__name__.removesuffix('Controller').lower()
    
    def index(self) -> None :
        self.view_data = { '@timestamp': self.handler.session['timestamp'] }
        if '@view_timestamp' in self.handler.session:
            self.view_data['@view_timestamp'] = self.handler.session['@view_timestamp']
        else:
            self.view_data['@view_timestamp'] = time.time()
        
        products = dao.Products.do_get()
        if len(products) > 0:
            with open(f"{appsetting.VIEWS_PATH}/{self.short_name}/DisplayTemplates/product.html", encoding="utf-8") as tpl:
                data_template = tpl.read()      
            product_views = []
            for product in products:
                product_view = data_template
                for k,v in product.items():
                    product_view = product_view.replace(f"{{{{{k}}}}}", str(v))
                product_views.append(product_view)
            self.view_data['@display_for_product'] = ''.join(product_views)
        self.return_view()

    def privacy(self) -> None:
        self.return_view() 