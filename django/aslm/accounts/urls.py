from django.urls import re_path
from django.conf import settings
from django.conf.urls.static import static
from adil.accounts.views import SignUp
from adil.accounts.views import LoginView
from adil.accounts.views import LogoutView


urlpatterns = [
    re_path('^signup/$', SignUp.as_view(), name='signup'),
    re_path(r'^login/', LoginView.as_view(redirect_authenticated_user=True), name='login'),
    re_path(r'^logout/', LogoutView.as_view(), name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL + 'accounts/', document_root=settings.STATIC_ROOT)
