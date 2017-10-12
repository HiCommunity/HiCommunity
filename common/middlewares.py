# coding=utf-8
from django.core.urlresolvers import reverse
import re
from common.exception import HiException
from django.shortcuts import render, render_to_response, HttpResponse
import json


class CommonMiddleware(object):

    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response

    def process_exception(self, request, exception):
        if isinstance(exception, HiException):
            if request.method == 'POST':
                return HttpResponse(json.dumps({
                    'result': False,
                    'msg': {
                        'code': exception.code,
                        'desc': exception.desc
                    }
                }))
            else:
                pass


    def process_template_response(self, request, response):
        # urls = (reverse('users:login_page'), reverse('users:register_page'),
        #         reverse('users:logout'))
        # content = response.content
        # for url in urls:
        #     content = re.sub(r'(<a.*?href="%s)(".*?>)' % url,
        #                      r'\1?from_url=%s\2' % url, content)
        # response.content = content

        return response
