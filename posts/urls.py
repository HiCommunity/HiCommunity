# coding=utf-8

from django.conf.urls import url

from posts import views


urlpatterns = [
    url(r'^index/$', views.post_index_page, name='index'),
    url(r'^(?P<board>\w+)/(?P<pid>\d+)/$', views.post_detail_page, name='detail'),
    url(r'^(?P<board>\w+)/new/$', views.new_post, name='new'),
]
