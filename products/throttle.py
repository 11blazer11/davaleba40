from rest_framework.throttling import SimpleRateThrottle
from rest_framework.exceptions import Throttled

class PostOnlyThrottle(SimpleRateThrottle):
    scope = 'post_only'
    message = "You can only send one POST request every 10 seconds. Please wait."
    rate = '1/10s' 

    def parse_rate(self, rate):
        return (1, 10)
    

    def get_cache_key(self, request, view):
        if request.method != 'POST':
            return None


        if request.user and request.user.is_authenticated:
            ident = str(request.user.id)
        else:
            ident = self.get_ident(request)

        return self.cache_format % {
            'scope': self.scope,
            'ident': ident
        }
    
    def throttle_failure(self):
        remaining = int(self.wait() or 0)
        raise Throttled(detail=f"dzaan bevira! serveri daigala, ecade {remaining} seconds.")