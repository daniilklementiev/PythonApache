import inspect
import os
import appsetting
from starter import MainHandler

class ViewController:

    def __init__(self, handler:MainHandler) -> None:    
        self.handler = handler
        self.view_data = dict()

    def return_view( self, action_name=None, controller_name:str=None, layout_name:str=None) :

        if layout_name is None:
            layout_name = f"{appsetting.VIEWS_PATH}/_layout.html"

        controller_object = inspect.currentframe().f_back.f_locals['self']

        if controller_name is None:
            if hasattr(controller_object, 'short_name') :
                controller_name = controller_object.short_name
            else:
                controller_name = controller_object.__class__.__name__.removesuffix('Controller').lower()

        if action_name == None:
            action_name = inspect.currentframe().f_back.f_code.co_name

        view_name = f"{appsetting.VIEWS_PATH}/{controller_name}/{action_name}.html"

        if not os.path.isfile( layout_name ) or not os.path.isfile( view_name ) :
            print( 'return_view:: file(s) not found: ', view_name )
            self.send_404()
            return
        
        with open( view_name, encoding='utf-8' ) as view :
            view_content = view.read()

        # Перевірити, чи є view_data у об'єкта контролера
        view_data = getattr(controller_object, 'view_data', None)
        if view_data :
            for k, v in view_data.items() :
                view_content = view_content.replace(k, str(v))
                
        # Впровадити значення з view_data у представлення
        with open( layout_name, encoding='utf-8' ) as layout :
            content = layout.read().replace( '<!-- RenderBody -->', view_content )

        self.handler.response_headers[ 'Content-Type' ] = 'text/html'
        self.handler.end( content ) 

