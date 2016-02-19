import mead.server
import mead.objects

class SampleResource(mead.objects.Resource):
    path = "/sample"
    flag = False

    def post(self, ctx=None):
        SampleResource.flag=True
        print(SampleResource.flag)
        if SampleResource.flag:
            return mead.objects.text_response("ok")
        return mead.objects.text_response("fail")

    def put(self, ctx=None):
        return mead.objects.text_response("fail")

    def get(self, ctx=None):
        if SampleResource.flag:
            return mead.objects.text_response("ok")
        return mead.objects.text_response("fail")

    def delete(self, ctx=None):
        return mead.objects.text_response("fail")


router = mead.objects.Router()
router.add_resource(SampleResource)

if __name__ == '__main__':
    mead.server.serve(router)
