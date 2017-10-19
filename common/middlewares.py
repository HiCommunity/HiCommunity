# coding=utf-8
# from django.core.urlresolvers import reverse
# import re
from common.exception import HiException
from django.shortcuts import HttpResponse
import json
from posts import models as posts_models


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

    @staticmethod
    def process_exception(request, exception):
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

    @staticmethod
    def process_template_response(request, response):
        path_info = request.path_info.strip('/').split('/')
        if path_info[0] == 'post':
            # post页面加上regions信息
            regions = posts_models.Region.objects.all()
            if not response.context_data:
                response.context_data = {}
            response.context_data['regions'] = regions
        return response
