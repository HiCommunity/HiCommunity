# coding=utf-8

from common.exception import HiException
from common.utils.format_ import ret_format
from django.shortcuts import HttpResponse
import json
from questions import models as questions_models


class CommonMiddleware(object):

    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.
        regions = questions_models.Region.objects.all()
        menus = []
        # [{'region': region_object, 'boards': [board_object1, ...]}, {...}]
        for region in regions:
            boards = region.board_of_region.all()
            menus.append({'region': region, 'boards': boards})

        self.menus = menus
        self.ret = ret_format()

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response

    def process_exception(self, request, exception):
        if isinstance(exception, HiException):
            if request.method in ('POST', 'PUT'):
                result = self.ret
                result['message'] = {
                        'code': exception.code,
                        'desc': exception.desc,
                        'level': exception.level
                }
                return HttpResponse(json.dumps(result))
            elif request.method == 'GET':
                pass
            else:
                pass

    def process_template_response(self, request, response):
        """
        Process after executing views
        :param request:
        :param response:
        :return:
        """
        path_info = request.path_info.strip('/').split('/')
        if path_info[0] == 'questions':
            if not response.context_data:
                response.context_data = {}
            response.context_data['side_nav_menus'] = self.menus
            _len = len(path_info)
            if _len > 1:
                region_address = path_info[1]
                menu = None
                for item in self.menus:
                    if item['region'].address == region_address:
                        menu = item
                        response.context_data['current_region'] = menu['region']
                if _len > 2:
                    board_address = path_info[2]
                    if menu :
                        # if there is any sub menu
                        for board in menu.get('boards', []):
                            if board.address == board_address:
                                response.context_data['current_board'] = board
        return response
