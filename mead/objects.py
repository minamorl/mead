import functools
import aiohttp.web
import ujson
import abc


class ResponsableObject(abc.ABC):

    @abc.abstractmethod
    def to_response():
        pass


class JSONObject(dict, ResponsableObject):

    def to_response(self):
        resp = aiohttp.web.Response()
        resp.body = ujson.dumps(self).encode("utf8")
        resp.content_type = "application/json"
        return resp


class HTMLString(str, ResponsableObject):

    def to_response(self):
        resp = aiohttp.web.Response()
        resp.body = self.encode("utf8")
        resp.content_type = "text/html"
        return resp
