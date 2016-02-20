import mead.server
from mead.objects import *

def helloworld(request):
    return response({"results":"Hello, world"})

router = Router()
router.add_route("GET", "/", helloworld)

if __name__ == '__main__':
    mead.server.serve(router)
