from mead import Mead, response, Router
from mead.objects import JSONObject

router = Router()
mead = Mead(router=router)

@router.route("/", methods=["GET"])
async def helloworld(context):
    return response(JSONObject({
        "results":"Hello"
    }))

if __name__ == '__main__':
    mead.serve()
