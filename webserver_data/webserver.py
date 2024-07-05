#NOTE: this is to server a local webpage to view the bot stats
#this is a concept idea and may or may not be finished.

import http.server
import socketserver


port = 8000

 
class RequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self,request, client_address, server, directory=None):
        super().__init__(request, client_address, server)
        return


handler = RequestHandler

#bare min. load a directory and the html will load the data every 10 seconds
#issue is the read/write of data often. database would be ideal if needed for more than debugging

with socketserver.TCPServer(("" , port), handler) as httpd:
    
    print("serving at port", port)
    httpd.serve_forever()