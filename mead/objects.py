from abc import ABCMeta, abstractmethod
import functools
import aiohttp
import aiohttp.web
import json
import aiohttp_session


class JSONObject(dict):
    pass

@functools.singledispatch
def response(body):
    pass


@response.register(str)
def _(s):
    resp = aiohttp.web.Response()
    resp.body = s.encode("utf8")
    return resp

@response.register(JSONObject)
def _(dct):
    resp = aiohttp.web.Response()
    resp.body = json.dumps(dct).encode("utf8")
    resp.content_type = "application/json"
    return resp

    
class Context(dict):
    pass

def create_context(request):
    return Context({
        "session": aiohttp_session.get_session(request),
        "params":  request.post(),
        "query": request.get(),
    })


class Resource(metaclass=ABCMeta):
    """Interface for user"""

    path = None

    @abstractmethod
    def put(self, ctx=None):
        pass

    @abstractmethod
    def get(self, ctx=None):
        pass

    @abstractmethod
    def delete(self, ctx=None):
        pass

    @abstractmethod
    def post(self, ctx=None):
        pass


class NotPathFoundError(Exception):
    pass

class Router():

    def __init__(self):
        self._i = 0
        self._route = []

    def __eq__(self, other):
        return self._route == other._route


    def route(self, path, method="GET"):
        def wrapper(func):
            def _wrapper(*args, **kwargs):
                return func(*args, **kwargs)
            return _wrapper
        self._route.append((method, path, wrapper))
        return wrapper


    def add_route(self, method, path, obj):
        def wrapped(request):
            context = create_context(request)
            return obj(request)

        self._route.append((method, path, wrapped))

    def add_resource(self, resource):
        if resource.path is None:
            raise NotPathFoundError
        resource = resource()
            
        self.add_route("GET", resource.path, resource.get)
        self.add_route("POST", resource.path, resource.post)
        self.add_route("PUT", resource.path, resource.put)
        self.add_route("DELETE", resource.path, resource.delete)

    def __iter__(self):
        return self

    def __next__(self):
        try:
            result = self._route[self._i]
            self._i += 1
            return result
        except IndexError:
            raise StopIteration

