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
    print(type(sample_dict1))
    resp = json_response(sample_dict1)
    assert sample_dict1 == json.loads(resp.body.decode("utf8"))
