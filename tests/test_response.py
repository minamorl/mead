import pytest
from mead.response import response
from aiohttp.web import Response


def test_response_dispatch():
    r = response("string")
    assert isinstance(r, Response)
    assert r.body == "string".encode("utf8")


@pytest.mark.xfail(raises=NotImplementedError)
def test_response_fails_when_argument_type_is_not_defined():
    response(1)
