import os
from django.urls import re_path
from django.conf import settings
from django.conf.urls.static import static
from adil.base.views import HomeView


urlpatterns = [
    re_path('^$', HomeView.as_view(), name='home')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL + 'base/', document_root=settings.STATIC_ROOT)
