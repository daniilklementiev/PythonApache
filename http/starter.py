# Alternative resolve for the server application
import inspect
import appsetting
from http.server import HTTPServer, BaseHTTPRequestHandler
import os
import sys
import uuid
import time
import json
sys.path.append(appsetting.CONTROLLERS_PATH)
# import HomeController

class MainHandler(BaseHTTPRequestHandler):
    sessions = dict() 

    def do_GET(self) -> None:
        url_parts = self.path.split('?')
        if len(url_parts) > 2:
            self.send_404()
            return
        path = url_parts[0]
        # query_string = url_parts[1] if len(url_parts) > 0 else None
        filename = f'{appsetting.WWWROOT_PATH}/{path}'
        if os.path.isfile(filename):
            self.flush_file(filename)
            return
        
        self.response_headers = dict()
        print(self.headers['Cookie'])
        self.cookies = dict( (cookie.split('=') for cookie in self.headers['Cookie'].split('; '))) if 'Cookie' in self.headers else {}
        
        # sessions processing
        session_id = self.cookies['session-id'] if 'session-id' in self.cookies else str(uuid.uuid1())
        if not session_id in MainHandler.sessions:
            MainHandler.sessions[session_id] = {
                'timestamp': time.time(),
                'session-id': session_id
            }
            self.response_headers['Set-Cookie'] = f'session-id={session_id}'
        self.session = MainHandler.sessions[session_id]
        print (self.session)    

        path_parts = path.split('/')
        controller_name = (path_parts[1].capitalize() if  path_parts[1] != '' else 'Home' ) + 'Controller'
        action_name = path_parts[2].lower() if len(path_parts) > 2 and path_parts[2] != '' else 'index'

        try:
            controller_module = __import__(controller_name)
            # controller_module = getattr(sys.modules[__name__], controller_name)
            controller_class = getattr(controller_module, controller_name)
            controller_object = controller_class(handler=self)
            controller_action = getattr(controller_object, action_name)
        except Exception as e:
            controller_action = None
            print(e)
        
        if controller_action :
            controller_action()
        else:
            self.send_404()
            return     

    def end(self, content:any) -> None:
        status_code = 200
        if content == None:
            status_code = 204
        elif type(content) == str:
            if not 'Content-Type' in self.response_headers:
                self.response_headers['Content-Type'] = 'text/html'
        else:
            content = json.dumps(content)
            self.response_headers['Content-Type'] = 'application/json'
        
        self.send_response(status_code)
        for k, v in self.response_headers.items() :
            self.send_header(k, v)
        self.end_headers()
        if content : 
            self.wfile.write(content.encode('utf-8'))
        self.connection.close()   

    def flush_file(self, filename)->None:
        if '..' in filename or not os.path.isfile(filename):
            self.send_404()
            return
        
        ext = filename.split( '.' )[-1] if '.' in filename else ''
        if ext in ( 'html', 'css' ):
            content_type = 'text/' + ext
        elif ext in ( 'js', 'ts' ):
            content_type = 'text/javascript'
        elif ext in ( 'png', 'bmp', 'gif' ):
            content_type = 'image/' + ext
        elif ext == 'ico':
            content_type = 'image/x-icon'
        elif ext in ('py', 'jss', 'php', 'exe', 'env', 'log', 'sql', 'ini', 'bat', 'cmd'):
            self.send_404()
            return
        else:
            content_type = 'application/octet-stream'
        
        self.send_response(200)
        self.send_header('Content-type', content_type)
        self.end_headers()
        
        with open(filename, 'rb') as file:
            self.wfile.write(file.read())
        pass

    def send_404(self) -> None:
        self.send_response(404)
        self.send_header('Status', '404 Not Found')
        self.send_header('Content-type', 'text/plain; charset=utf-8')
        self.end_headers()
        self.wfile.write(b"Requested content not found")

    def log_request(self, code: int | str = "-", size: int | str = "-") -> None:
        return None




def main():
    server = HTTPServer(('127.0.0.1', 82), MainHandler)
    try:
        print("Server started")
        server.serve_forever()
    except :
        print("Server stopped")


if __name__ == '__main__':
    main()