from urllib.parse import parse_qs


class Request:
    def __init__(self, rfile):
        self.file = rfile

        self.method = None
        self.uri = None
        self.protocol = None
        self.headers = {}
        self.body = None
        self.post_id = None

        self.__parse_request_line()
        self.__parse_headers()
        self.__parse_body()
        self.__parse_uri()

    def __parse_uri(self):
        if self.uri.startswith('/car?id='):
            array = self.uri.split('?')
            self.uri = array[0]
            array2 = array[1].split('=')
            self.post_id = int(array2[1])

    def __parse_request_line(self):
        request_line = self.__readline()
        # GET / HTTP/1.1    ['GET', '/', 'HTTP/1.1']
        
        print(request_line.split())

        self.method, self.uri, self.protocol = request_line.split()

    def __readline(self):
        return self.file.readline().decode().strip()

    def __parse_headers(self):
        while True:
            header = self.__readline()
            
            if header == '':
                break

            name, value = header.split(': ')
            self.headers[name] = value

    def __parse_specific_body(self):
        if self.headers['Content-Type'] == 'application/x-www-form-urlencoded':
            self.body = parse_qs(self.body)

    def __parse_body(self):
        if 'Content-Length' in self.headers:
            content_length = int(self.headers['Content-Length'])
            self.body = self.file.read(content_length).decode()
            self.__parse_specific_body()

    def __str__(self):
        return (
            f'{"-" * 30}\n'
            f'{self.method} {self.uri}'
        )
