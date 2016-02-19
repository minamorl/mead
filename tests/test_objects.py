from mead.objects import Resource, Result, Context

class SampleAPI(Resource):

    obj = None

    def get(self, ctx):
        result = Result({
            "hi": self.obj,
        })
        return result

    def delete(self, ctx):
        del self.obj

    def post(self, ctx):
        message = ctx["params"]["hi"]
        self.obj = message

    def put(self, ctx):
        pass

api = SampleAPI()
context = Context({
    "session": None,
    "params": {
        "hi": "foo",
    },
})


def test_api_get():
    api.post(context)
    assert Result({
        "hi": "foo"
    }) == api.get(context)


