import mead

class SampleAPI(mead.objects.Resource):
    def get(self, ctx):
        result = mead.objects.Result({
            "hi":"foo"
        })
        return result


api = SampleAPI()
context = mead.objects.Context({
    "session" : None,
    "params" : [("hi","foo")]
})

def test_api_get():
    result = mead.objects.Result({
        "hi":"foo"
    })
    assert result == api.get(context)
