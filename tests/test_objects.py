from mead import Resource, Result


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
context = mead.objects.Context({
    "session": None,
    "params": [("hi", "foo")]
})


def test_api_get():
    result = mead.objects.Result({
        "hi": "foo"
    })
    assert result == api.get(context)
