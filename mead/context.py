import aiohttp_session


class Context(dict):
    pass

async def create_context(request):
    session = await aiohttp_session.get_session(request)
    return Context({
        "params": await request.post(),
        "query": request.GET,
        "session": session,
    })
