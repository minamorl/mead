from mead.server import Mead
from mead.objects import *

router = Router()
mead = Mead()

@router.route("/", methods=["GET"])
def helloworld(context):
    return response(JSONObject({
        "results":"Hello"
    }))

if __name__ == '__main__':
    mead.serve(router)
