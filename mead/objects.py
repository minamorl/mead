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

async def create_context(request):
    session = await aiohttp_session.get_session(request)
    return Context({
        "params":  await request.post(),
        "query": request.GET,
        "session": session,
    })


class Resource(metaclass=ABCMeta):
    """Interface for user"""

    path = None

    @abstractmethod
    async def put(self, ctx=None):
        pass

    @abstractmethod
    async def get(self, ctx=None):
        pass

    @abstractmethod
    async def delete(self, ctx=None):
        pass

    @abstractmethod
    async def post(self, ctx=None):
        pass


class NotPathFoundError(Exception):
    pass

class Router():

    def __init__(self):
        self._i = 0
        self._route = []

    def __eq__(self, other):
        return self._route == other._route


    def route(self, path, methods=["GET"]):
        def wrapper(func):
            @functools.wraps(func)
            def _wrapper(*args, **kwargs):
                return func(*args, **kwargs)
            _methods = methods
            if not isinstance(methods, list):
                _methods = [methods]
            for method in _methods:
                self.add_route(method, path, _wrapper)
            return _wrapper
        return wrapper


    def add_route(self, method, path, obj):
        async def wrapped(request):
            context = await create_context(request)
            return obj(context)

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
