import aiohttp.web
import asyncio
import functools
import aiohttp_session
import aiohttp_session.cookie_storage


async def init(loop, router, session_encrypt_key):
    app = aiohttp.web.Application(loop=loop)

    handler = app.make_handler()
    for method, path, obj in router:
        app.router.add_route(method, path, obj)
    srv = await loop.create_server(handler, '127.0.0.1', 8080)
    aiohttp_session.setup(app, aiohttp_session.cookie_storage.EncryptedCookieStorage(session_encrypt_key))
    return srv, handler


def serve(router, session_encrypt_key=b"aab32gab32gab32gab32gab3225gb32g"):
    print("Starting http://127.0.0.1:8080")
    loop = asyncio.get_event_loop()
    srv, handler = loop.run_until_complete(init(loop, router, session_encrypt_key))
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        loop.run_until_complete(handler.finish_connections())
