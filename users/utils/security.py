# coding=utf-8
import hashlib
from django.core.urlresolvers import reverse
from django.shortcuts import HttpResponseRedirect, Http404
from users.constants.common import SESSION_LOGIN_USER
from common.exception import HiHttp404
from users.exception import LoginRequired, UserRoleVerificationFailed
from common.utils.string import obj2list
from django.contrib import messages
from common.constants.messages import NOT_ALLOWED_TO_ACCESS, NEED_LOGIN_FIRST


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
        user_id = request.session.get(SESSION_LOGIN_USER)
        if user_id:
            kwargs['user_id'] = user_id
            return func(request, *args, **kwargs)
        else:
            if request.method == 'GET':
                messages.add_message(request, messages.WARNING, NEED_LOGIN_FIRST)
                return HttpResponseRedirect(reverse('accounts:login_page'))
            else:
                raise LoginRequired
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
                    raise HiHttp404
        return method_filter
    return wrapper


def role_restrict(role):
    """
    Restrict request by the user's role
    Role is a string or list/tuple
    """
    def wrapper(func):
        def _restrict(request, *args, **kwargs):
            expect_roles = obj2list(role)
            if request.session.get(SESSION_LOGIN_USER).get('role') in expect_roles:
                return func(request, *args, **kwargs)
            else:
                if request.method == 'GET':
                    if 'admin' in expect_roles:
                        messages.add_message(request, messages.ERROR, NOT_ALLOWED_TO_ACCESS)
                        return HttpResponseRedirect(reverse('accounts:login_page'))
                else:
                    raise UserRoleVerificationFailed

        return _restrict
    return wrapper
