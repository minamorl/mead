import pytest


@pytest.fixture
def loop():
    import asyncio
    return asyncio.get_event_loop()
