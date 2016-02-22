from abc import ABCMeta, abstractmethod
import functools
import aiohttp
import aiohttp.web
import ujson
import aiohttp_session


class JSONObject(dict):
    pass

class HTMLString(str):
    pass

@functools.singledispatch
def response(body):
    pass

@response.register(str)
def _(s):
    resp = aiohttp.web.Response()
    resp.body = s.encode("utf8")
    return resp

@response.register(HTMLString)
def _(s):
    resp = aiohttp.web.Response()
    resp.body = s.encode("utf8")
    resp.content_type = "text/html"
    return resp

@response.register(JSONObject)
def _(dct):
    resp = aiohttp.web.Response()
    resp.body = ujson.dumps(dct).encode("utf8")
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


class NotPathFoundError(Exception):
    pass

class Router(list):

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

        self.append((method, path, wrapped))
