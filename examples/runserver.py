from mead.server import serve
from mead.objects import *

router = Router()

def helloworld(context):
    print(context)
    return response(JSONObject({
        "results":"Hello"
    }))

router.add_route("GET", "/", helloworld)
router.add_route("POST", "/", helloworld)
if __name__ == '__main__':
    serve(router)
