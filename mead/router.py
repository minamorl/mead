import functools
from .context import create_context


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
            return await obj(context)

        self.append((method, path, wrapped))
