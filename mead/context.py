import aiohttp_session
import collections


Context = collections.namedtuple("Context", ["params", "query", "session"])


async def create_context(request):
    return Context(
        params=request.post(),
        query=request.GET,
        session=aiohttp_session.get_session(request))
