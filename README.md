# mead
Flexible aiohttp Web Server

```python
import mead.server
import mead.objects

async def helloworld(request):
    return await mead.objects.text_response("Hello, world")

router = mead.objects.Router()
router.add_route("GET", "/", helloworld)

if __name__ == '__main__':
    mead.server.serve(router)
```
