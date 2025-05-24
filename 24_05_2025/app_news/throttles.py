from rest_framework.throttling import SimpleRateThrottle

class ListOnlyThrottle(SimpleRateThrottle):
    scope = 'list_only'

    def get_cache_key(self, request, view):
        if hasattr(view, 'action') and view.action == 'list':
            if request.user.is_authenticated:
                ident = request.user.pk
            else:
                ident = self.get_ident(request) 
            return self.cache_format % {
                'scope': self.scope,
                'ident': ident
            }
        return None 
