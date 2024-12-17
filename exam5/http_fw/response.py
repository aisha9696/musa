from os import fstat


class Response:
    HTTP_OK = 200
    HTTP_BAD_REQUEST = 400
    HTTP_NOT_FOUND = 404
    HTTP_INTERNAL_SERVER_ERROR = 500
    HTTP_MOVED_PERMANENTLY = 301
    
    MESSAGES = {
        HTTP_OK: 'OK',
        HTTP_BAD_REQUEST: 'Bad Request',
        HTTP_NOT_FOUND: 'Not Found',
        HTTP_INTERNAL_SERVER_ERROR: 'Internal Server Error',
        HTTP_MOVED_PERMANENTLY: 'Moved Permanently',
    }

    PROTOCOL = 'HTTP/1.1'
    
    def __init__(self, wfile):
        self.wfile = wfile
        self.status = self.HTTP_OK
        self.headers = {}
        self.body = None
        self.file_body = None

    def set_status(self, new_status: int) -> None:
        self.status = new_status

    def add_header(self, name, value):
        self.headers[name] = value
    
    def set_body(self, body):
        self.body = body.encode()
        self.add_header('Content-Length', len(self.body))

    def set_file_body(self, file):
        self.file_body = file
        size = fstat(file.fileno()).st_size
        self.add_header('Content-Length', size)

    def __get_status_line(self):
        message = self.MESSAGES[self.status]
        return f'{self.PROTOCOL} {self.status} {message}'

    def __get_headers(self):
        headers = []
        
        for name, value in self.headers.items():
            headers.append(f'{name}: {value}')
        
        return headers

    def _write_file_body(self):
        while True:
            data = self.file_body.read(1024)

            if not data:
                break

            self.wfile.write(data)

    def send(self):
        status_line = self.__get_status_line()
        headers = self.__get_headers()
        
        response_str = '\r\n'.join([status_line] + headers) + '\r\n\r\n'
        self.wfile.write(response_str.encode())

        if self.body:
            self.wfile.write(self.body)

        elif self.file_body:
            self._write_file_body()
            