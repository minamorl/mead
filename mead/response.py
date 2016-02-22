import functools
from .objects import ResponsableObject


@functools.singledispatch
def response(obj):
    raise NotImplementedError


@response.register(str)
def _(s):
    resp = aiohttp.web.Response()
    resp.body = s.encode("utf8")
    return resp


@response.register(ResponsableObject)
def _(obj):
    return obj.to_response()
