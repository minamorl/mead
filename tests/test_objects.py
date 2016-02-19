from mead.objects import Resource, Result, Context


class SampleAPI(Resource):

    def get(self, ctx):
        result = Result({
            "hi": "foo"
        })
        return result

    def delete(self, ctx):
        pass

    def post(self, ctx):
        pass

    def put(self, ctx):
        pass

api = SampleAPI()
context = Context({
    "session": None,
    "params": [("hi", "foo")]
})


def test_api_get():
    result = Result({
        "hi": "foo"
    })
    assert result == api.get(context)
