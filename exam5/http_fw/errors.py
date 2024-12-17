from .response import Response
from .request import Request


def not_found(request, response):
    response.set_status(Response.HTTP_NOT_FOUND)
    response.add_header('Content-Type', 'text/html')
    response.set_body('<h1>404 Not Found</h1>')


def internal_server_error(request, response):
    response.set_status(Response.HTTP_INTERNAL_SERVER_ERROR)
    response.add_header('Content-Type', 'text/html')
    response.set_body('<h1>500 INTERNAL_SERVER_ERROR</h1>')
