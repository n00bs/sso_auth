from rest_framework_sso import claims
from rest_framework_sso.views import ObtainAuthorizationTokenView
from rest_framework.response import Response
from django.shortcuts import redirect
from django.http import HttpResponse, HttpResponseRedirect


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
            token = "JWT " + response.data["token"]
            response = HttpResponse(successful_redirect_url)
            response["Authorization"] = token
            import pdb; pdb.set_trace()
        return response
