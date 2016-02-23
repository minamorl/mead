import pytest
from unittest.mock import Mock
from mead.context import create_context, Context


@pytest.fixture
def loop():
    import asyncio
    return asyncio.get_event_loop()


def test_create_context(loop):
    async def go():
        assert isinstance(await create_context(Mock()), Context), Context
    loop.run_until_complete(go())
