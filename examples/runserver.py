from mead.server import serve
from mead.objects import *

router = Router()

@router.route("/")
def helloworld(context):
    username = context["query"]["username"]
    print(type(context))
    return response(JSONObject({"results":"Hello"}))

if __name__ == '__main__':
    serve(router)
