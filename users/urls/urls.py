# coding=utf-8

from django.conf.urls import url, include

from users import views


urlpatterns = [
    url(r'^accounts/', include('users.urls.account_urls', namespace='accounts')),
]
