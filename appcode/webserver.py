from http.server import HTTPServer, BaseHTTPRequestHandler
import os

class Hello(BaseHTTPRequestHandler):

    def do_GET(self):
       print(self.request)
       self.send_response(200)
       self.end_headers()
       page = f"<h1>hello from {os.getenv('MESSAGE',default='MESSAGE not set')}</h1>"
       self.wfile.write(bytes(page,'utf-8'))

httpd = HTTPServer(('0.0.0.0',80),Hello)
httpd.serve_forever()
