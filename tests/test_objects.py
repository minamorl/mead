import json

from mead.objects import *


def test_str_response():
    sample_str = "test"
    assert response(sample_str).body == b"test"


def test_json_response():
    sample_dict1 = {
        "this": {
            "is": {
                "a": "test"
            }
        }
    }
    resp = response(sample_dict1)
    assert sample_dict1 == json.loads(resp.body.decode("utf8"))


def test_router_route():
    router = Router()
    async def sample_callable(requests):
        return resp
    sample_callable = router.route("/")(sample_callable)
    assert len(list(r for r in router)) == 1
