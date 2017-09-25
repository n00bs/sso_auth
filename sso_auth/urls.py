from django.conf.urls import url, include
from rest_framework_sso.views import obtain_session_token, \
                                    obtain_authorization_token
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from sso_auth.views import ObtainAuthorizationTokenView

urlpatterns = [
    url(r'^login/',
        auth_views.login, {'template_name': 'login.html'},
        name='login'),
    # Not required as these are refresh tokens
    # url(r'^session/', login_required(obtain_session_token)),
    url(r'^authorize/', login_required(ObtainAuthorizationTokenView.as_view())),
]
