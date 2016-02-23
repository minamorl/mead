# mead
Flexible aiohttp Web Server

```python
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
```

## Example: Greeting

```
from mead import Mead, response, Router
from mead.objects import JSONObject


router = Router()
mead = Mead(router=router)


@router.route("/greeting", methods=["GET"])
async def greeting(context):
    ses = await context.session
    try:
        username = ses["username"]
        return response(JSONObject({
            "results": "Hello, {}".format(username)
        }))
    except KeyError:
        return response(JSONObject({
            "results": "Hello."
        }))


@router.route("/greeting", methods=["POST"])
async def greeting(context):
    ses = await context.session
    params = await context.params
    try:
        ses["username"] = params["username"]
        return response(JSONObject({
            "results": "ok"
        }))
    except KeyError:
        return response(JSONObject({
            "results": "Something went wrong."
        }))

if __name__ == '__main__':
    mead.serve()
```
