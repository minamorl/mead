import aiohttp.web
import asyncio
import functools


async def init(loop, router):
    app = aiohttp.web.Application(loop=loop)
    handler = app.make_handler()
    for method, path, obj in router():
        app.router.add_route(method, path, obj)
    srv = await loop.create_server(handler, '127.0.0.1', 8080)
    return srv, handler


def serve(router):
    loop = asyncio.get_event_loop()
    srv, handler = loop.run_until_complete(init(loop, router))
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        loop.run_until_complete(handler.finish_connections())


if __name__ == '__main__':
    serve(router)
