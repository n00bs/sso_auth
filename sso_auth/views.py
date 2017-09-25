from rest_framework_sso import claims
from rest_framework_sso.views import ObtainAuthorizationTokenView
from rest_framework.response import Response


def create_authorization_payload(session_token, user, account=None, **kwargs):
    return {
        claims.TOKEN: claims.TOKEN_AUTHORIZATION,
        claims.SESSION_ID: session_token.pk,
        claims.USER_ID: user.pk,
        claims.EMAIL: user.pk + '@uw.edu',
    }


class ObtainAuthorizationTokenView(ObtainAuthorizationTokenView):
    """
    Returns a JSON Web Token that can be used for authenticated requests.
    """
    def get(self, request, *args, **kwargs):
        response = self.post(request, args, kwargs)
        successful_redirect_url = self.request.GET.get('successful_redirect_url', None)
        if successful_redirect_url:
            # redirect the response token to successful_redirect_url
            print successful_redirect_url
        return response
