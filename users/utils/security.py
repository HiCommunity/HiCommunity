# coding=utf-8
import hashlib
from django.core.urlresolvers import reverse
from django.shortcuts import HttpResponseRedirect, Http404
from common.exception import HiHttp404
from users.exception import LoginRequired, UserRoleVerificationFailed
from common.utils.string_ import obj2iter
from django.contrib import messages
from common.constants.messages import Privileges
from users.utils.session import get_login_session


def md5_encode(string):
    """
    Hash a string with MD5
    """
    assert isinstance(string, str)
    m2 = hashlib.md5()
    m2.update(string)
    return m2.hexdigest()


def request_method(method):
    """
    A decoration to ensure the request run in a designated way.
    You need pass a string argument in 'POST', 'GET', 'PUT', 'DELETE'
    All methods are 'get', 'post', 'put', 'patch', 'delete', 'head',
        'options', 'trace'
    """
    method = method.upper()
    assert method in ('POST', 'GET', 'PUT', 'DELETE')

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


def login_required(role=None):
    """
    Restrict request by the
    Role is a string or list/tuple.

    """
    def wrapper(func):
        def _restrict(request, *args, **kwargs):
            expect_roles = obj2iter(role)
            login_user = get_login_session(request)
            if login_user:
                if role:
                    if login_user.get('role') in expect_roles:
                        return func(request, *args, **kwargs)
                    else:
                        # unsatisfied role
                        if request.method == 'GET':
                            messages.add_message(
                                request, messages.ERROR,
                                Privileges.NOT_ALLOWED_TO_ACCESS)
                            return HttpResponseRedirect(
                                reverse('users:accounts:login_page'))
                        else:
                            raise UserRoleVerificationFailed
                else:
                    return func(request, *args, **kwargs)
            else:
                # has not login
                if request.method == 'GET':
                    messages.add_message(request, messages.WARNING,
                                         Privileges.NEED_LOGIN_FIRST)
                    return HttpResponseRedirect(
                        reverse('users:accounts:login_page'))
                else:
                    raise LoginRequired

        return _restrict
    return wrapper
