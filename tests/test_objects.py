import json

from mead.objects import *


def test_json_response():
    sample_dict1 = {
        "this": {
            "is": {
                "a": "test"
            }
        }
    }
    resp = json_response(sample_dict1)
    assert sample_dict1 == json.loads(resp.body.decode("utf8"))

def test_router_route():
    router = Router()
    async def sample_callable(requests):
        return ""
    sample_callable = router.route("/")(sample_callable)
    assert len(list(r for r in router)) == 1
