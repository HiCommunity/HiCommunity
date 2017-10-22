# coding=utf-8

from django.conf.urls import url, include

from hiadmin.views import index


urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^management/', include('hiadmin.urls.management', namespace='management')),
    url(r'^settings/', include('hiadmin.urls.settings', namespace='settings')),
]