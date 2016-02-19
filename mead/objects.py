from abc import ABCMeta, abstractmethod
import functools
import aiohttp


class Resource(metaclass=ABCMeta):
    """Interface for user"""
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


class Context(dict):
    pass


class Response(dict):
    pass


class Session(dict):
    pass

class Router():
        
    def __init__(self):
        self.i = 0
        self.route = []

    def add_route(self, method, path, obj, wrapper):
        self.route.append((method, path, functools.partial(wrapper, obj=obj)))

        
    def __iter__(self):
        return self

    def __next__(self):
        try:
            result = self.route[self.i]
            self.i += 1
            return result
        except IndexError:
            raise StopIteration


async def text_response(request, obj):
    resp = aiohttp.web.Response()
    resp.body = obj(request).encode("utf8")
    return resp
