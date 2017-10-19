# coding=utf-8

from django.conf.urls import url

from posts import views


urlpatterns = [
    url(r'^$', views.post_index, name='index'),
    # url(r'^(?P<region>\w+)/$', views.post_list_page, name='list_no_board'),
    url(r'^(?P<region>\w+)/(?P<board>\w+)/$', views.post_list_page, name='list'),
    url(r'^(?P<region>\w+)/(?P<board>\w+)/(?P<pid>\d+)/$',
        views.post_detail_page, name='detail'),
    url(r'^(?P<region>\w+)/(?P<board>\w+)/new_post/$', views.new_post, name='new'),
]
