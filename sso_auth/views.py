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
        login_at = self.request.GET.get('login_at', None)
        return_to = self.request.GET.get('return_to', None)
        if login_at and return_to:
            # redirect the response token to the client
            token = response.data["token"]
            end_url = login_at + "?return_to=" + return_to + "&token=" + token
            response = HttpResponseRedirect(end_url)
        return response
