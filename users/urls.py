# coding=utf-8

from django.conf.urls import url

from users import views


urlpatterns = [
    url(r'^login/$', views.login_page, name='login_page'),
    url(r'^login/submit/$', views.login, name='login'),
    url(r'^register/$', views.register_page, name='register_page'),
    url(r'^register/submit/$', views.register, name='register'),
]
