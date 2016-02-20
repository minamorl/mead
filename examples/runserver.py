from mead.server import serve
from mead.objects import *

router = Router()

@router.route("/", methods=["GET"])
def helloworld(context):
    print(context)
    return response(JSONObject({
        "results":"Hello"
    }))

if __name__ == '__main__':
    serve(router)
