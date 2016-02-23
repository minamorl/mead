import pytest
from mead.objects import JSONObject, HTMLString, ResponseObject

def test_all_objects_inherit_responseobject():
    assert issubclass(JSONObject, ResponseObject), JSONObject
    assert issubclass(HTMLString, ResponseObject), HTMLString
