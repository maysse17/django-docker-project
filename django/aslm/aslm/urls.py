"""aslm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from base.views import HomeView
from django.urls import include
from django_js_reverse.views import urls_js
from django.views.decorators.cache import cache_page
from django.urls import re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include(('base.urls', 'base'), namespace='base')),
    path('accounts/', include(('accounts.urls', 'accounts'), namespace='accounts')),
    path('board/', include(('board.urls', 'board'), namespace='board')),
    re_path(r'^jsreverse/$', cache_page(3600)(urls_js), name='js_reverse'),
]
