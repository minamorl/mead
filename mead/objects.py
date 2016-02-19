from abc import ABCMeta, abstractmethod
import functools
import aiohttp


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
        self.i = 0
        self.route = []

    def add_route(self, method, path, obj):
        self.route.append((method, path, obj))

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
            result = self.route[self.i]
            self.i += 1
            return result
        except IndexError:
            raise StopIteration


async def text_response(s):
    resp = aiohttp.web.Response()
    resp.body = s.encode("utf8")
    return resp
