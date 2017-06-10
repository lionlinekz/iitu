"""iitu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from ticket import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'index', views.index, name='index'),
    url(r'ayat', views.complete_ayat, name='complete_ayat'),
    url(r'sure', views.complete_sure, name='complete_sure'),
    url(r'(?P<sura>[0-9]+)/(?P<ayat>[0-9]+)', views.ayat, name='ayat'),
    url(r'(?P<sura>[0-9]+)', views.sura, name='sura'),
    url(r'^$', views.index),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
