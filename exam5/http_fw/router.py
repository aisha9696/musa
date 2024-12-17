from .errors import not_found, internal_server_error


class Router:
    def __init__(self):
        self.routes = {
            'get': [],
            'post': []
        }

    def add(self, http_method: str, uri: str, ctrl, ctrl_method):
        self.routes[http_method].append({
            'uri': uri,
            'ctrl': ctrl,
            'ctrl_method': ctrl_method
        })

    def get(self, *args):
        self.add('get', *args)

    def post(self, *args):
        self.add('post', *args)

    def run(self, request, response):
        http_method = request.method.lower()
        method_routes = self.routes[http_method]
        route = None
        for r in method_routes:
            if r['uri'] == request.uri:
                route = r
                break
        if not route:
            return not_found(request, response)
        try:
            ctrl = route['ctrl'](request, response)
            getattr(ctrl, route['ctrl_method'])()
        except BaseException as e:
            print(e)
            return internal_server_error(request, response)
