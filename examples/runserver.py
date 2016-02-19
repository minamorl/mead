import mead.server
import mead.objects

def helloworld(request):
    return "Hello, World"

router = mead.objects.Router()
router.add_route("GET", "/", helloworld, mead.objects.text_response)

if __name__ == '__main__':
    mead.server.serve(router)
