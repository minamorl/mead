import aiohttp.web
import asyncio
import functools
import aiohttp_session
import aiohttp_session.cookie_storage


DEFAULT_ENCRYPT_KEY = b"                                "


class Mead:

    def __init__(self, router=None, app=None, session_encrypt_key=DEFAULT_ENCRYPT_KEY, loop=None):
        self._app = app or aiohttp.web.Application()
        self._router = router
        self._session_encrypt_key = session_encrypt_key
        self._prepared = False
        self._loop = loop or asyncio.get_event_loop()

    @property
    def prepared(self):
        return self._prepared

    @property
    def app(self):
        return self._app

    @property
    def session_encrypt_key(self):
        return self._session_encrypt_key

    @property
    def loop(self):
        return self._loop

    @property
    def router(self):
        return self._router

    def prepare(self):
        if not self.prepared:
            for method, path, obj in self.router:
                self.app.router.add_route(method, path, obj)
            aiohttp_session.setup(
                self.app, aiohttp_session.cookie_storage.EncryptedCookieStorage(self.session_encrypt_key))
        self._prepared = True

    async def init(self, loop, address, port):
        handler = self.app.make_handler()
        self.prepare()
        srv = await self._loop.create_server(handler, address, port)
        return srv, handler

    def serve(self, port=8080, address="127.0.0.1"):
        print("Starting on http://{}:{}".format(address, port))
        self.app._loop = self.loop

        srv, handler = self._loop.run_until_complete(
            self.init(self.loop, address, port))
        try:
            self._loop.run_forever()
        except KeyboardInterrupt:
            self._loop.run_until_complete(handler.finish_connections())

    def __call__(self):
        return self

    def __getattr__(self, attr):
        self.prepare()
        return self.app.__getattribute__(attr)
