# myapp/middleware.py
class EnsureRemoteAddrMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Set a default IP address if 'REMOTE_ADDR' is missing
        if 'REMOTE_ADDR' not in request.META:
            request.META['REMOTE_ADDR'] = '127.0.0.1'
        return self.get_response(request)