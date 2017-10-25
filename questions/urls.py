# coding=utf-8

from django.conf.urls import url

from questions import views


urlpatterns = [
    url(r'^$', views.question_index, name='index'),
    # url(r'^(?P<region>\w+)/$', views.question_list_page, name='list_no_board'),
    url(r'^(?P<region>\w+)/(?P<board>\w+)/$', views.question_list_page, name='list'),
    url(r'^(?P<region>\w+)/(?P<board>\w+)/(?P<pid>\d+)/$',
        views.question_detail_page, name='detail_page'),
    url(r'^(?P<region>\w+)/(?P<board>\w+)/new_question/$',
        views.new_question, name='new_question'),
]
