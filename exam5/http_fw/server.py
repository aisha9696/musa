from http_fw.request import Request
from http_fw.response import Response
from http_fw.static_responder import StaticResponder

import socketserver

#REST RESTfull

#CRUDL - Create, Read, Update, Delete, List
#/posts
#GET - /posts
#GET - /posts/{id}
#POST - /posts
#PUT\PATH - /posts/{id}
#DELETE - /posts/{id}


def run(router):

    class Handler(socketserver.StreamRequestHandler):
        
        def handle(self):
            request = Request(self.rfile)
            response = Response(self.wfile)
            response.add_header('Connection', 'close')
            
            static_responder = StaticResponder(request, response)

            print(request)
            
            if static_responder.file:
                static_responder.prepare_response()
            else:
                router.run(request, response)

            response.send()
            

    ADDRESS = ('localhost', 1027)
    socketserver.ThreadingTCPServer.allow_reuse_address = True

    with socketserver.ThreadingTCPServer(ADDRESS, Handler) as server:
        server.serve_forever()
