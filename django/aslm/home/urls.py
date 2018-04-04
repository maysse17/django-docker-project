import os
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
]

if settings.DEBUG:
    static_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), 'static', 'base'))
    urlpatterns += static(settings.STATIC_URL + 'base/', document_root=static_folder)
