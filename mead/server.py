import aiohttp.web
import asyncio
import functools
import aiohttp_session
import aiohttp_session.cookie_storage


class Mead():

    def __init__(self, router=None, session_encrypt_key=b"                                "):
        self.app = aiohttp.web.Application()
        self.router = router
        self.session_encrypt_key = session_encrypt_key
        self.prepared = False

    def prepare(self):
        if not self.prepared:
            for method, path, obj in self.router:
                self.app.router.add_route(method, path, obj)
            aiohttp_session.setup(self.app, aiohttp_session.cookie_storage.EncryptedCookieStorage(self.session_encrypt_key))
        self.prepared = True

    async def init(self, loop, address, port):
        handler = self.app.make_handler()
        self.prepare()
        srv = await loop.create_server(handler, address, port)
        return srv, handler

    def serve(self, port=8080, address="127.0.0.1"):
        print("Starting on http://{}:{}".format(address, port))
        loop = asyncio.get_event_loop()
        self.app._loop = loop

        srv, handler = loop.run_until_complete(self.init(loop, address, port))
        try:
            loop.run_forever()
        except KeyboardInterrupt:
            loop.run_until_complete(handler.finish_connections())

    def __call__(self):
        return self

    def __getattr__(self, attr):
        self.prepare()
        return self.app.__getattribute__(attr)
