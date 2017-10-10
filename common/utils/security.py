# coding=utf-8
import hashlib
import json
from django.core.urlresolvers import reverse
from django.shortcuts import HttpResponseRedirect, HttpResponse, Http404
from users.constants.common import SESSION_LOGIN_USER_ID
from common.constants.common import RetMsg


def md5_encode(string):
    """
    Hash a string with MD5
    """
    assert isinstance(string, str)
    m2 = hashlib.md5()
    m2.update(string)
    return m2.hexdigest()


def login_required(func):
    """
    A decorator for views' function who needs verification of user's login
    """
    def inner(request, *args, **kwargs):
        user_id = request.session.get(SESSION_LOGIN_USER_ID)
        if user_id:
            kwargs['user_id'] = user_id
            return func(request, *args, **kwargs)
        else:
            if request.method == 'GET':
                return HttpResponseRedirect(reverse('users:login'))
            else:
                return HttpResponse(json.dumps(
                    {'result': False, 'msg': RetMsg.Users.LOGIN_REQUIRED}))
    return inner


def request_method(method):
    """
    A decoration to ensure the request run in a designated way.
    You need pass a string argument in 'POST', 'GET', 'PUT', 'DELETE'
    """
    assert method in ('POST', 'GET', 'PUT', 'DELETE')
    method = method.upper()

    def wrapper(func):
        def method_filter(request, *args, **kwargs):
            if request.method == method:
                return func(request, *args, **kwargs)
            else:
                if request.method == 'GET':
                    raise Http404
                else:
                    return HttpResponse(json.dumps({'result': False,
                                                    'msg': RetMsg.HTTP.HTTP_404}))
        return method_filter
    return wrapper
