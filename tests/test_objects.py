from mead.objects import Resource, Response, Context

class SampleAPI(Resource):

    obj = None

    def get(self, ctx):
        result = Response({
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
    assert Response({
        "hi": "foo"
    }) == api.get(context)


