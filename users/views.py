# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

from django.core.urlresolvers import reverse
from django.shortcuts import (render_to_response, HttpResponse,
                              HttpResponseRedirect)
from common.constants.common import RET_FORMAT, RetMsg
from common.utils.security import request_method, login_required
from users import models as users_models
from users.constants.common import SESSION_LOGIN_USER_ID
from users.utils import validation


@request_method('GET')
def register_page(request, *args, **kwargs):
    return render_to_response('users/register.html')


@request_method('POST')
def register(request):
    ret = RET_FORMAT
    password = request.POST.get('password')
    username = request.POST.get('username')
    email = request.POST.get('email')
    if not all((validation.validate_username(username),
                validation.validate_password(password),
                validation.validate_email(email))):
        ret['msg'] = RetMsg.Common.ILLEGAL_ARGUMENTS
        return HttpResponse(json.dumps(ret))
    try:
        users_models.Profile.objects.create(password=password,
                                            name=username)
    except Exception as e:
        ret['msg'] = RetMsg.Users.CREATE_USER_FAILED
    else:
        ret['result'] = True
    return HttpResponse(json.dumps(ret))


@request_method('GET')
def login_page(request):
    ret = RET_FORMAT
    user_id = request.session.get(SESSION_LOGIN_USER_ID)
    if user_id:
        ret['msg'] = RetMsg.Users.USER_ALREADY_LOGIN
        return HttpResponse(json.dumps(ret))
    return render_to_response(reverse('users:login_page'))


@request_method('POST')
def login(request):
    ret = RET_FORMAT
    username = request.POST.get('username')
    password = request.POST.get('password')
    if (not validation.validate_username(username)
        or not validation.validate_password(password)):
        # RegEx filter first
        ret['msg'] = RetMsg.Users.WRONG_PASSWORD
    else:
        user_obj = users_models.Profile.objects.filter(username=username)
        if user_obj.count() == 1:
            if user_obj[0].password == password:
                request.session[SESSION_LOGIN_USER_ID] = user_obj.id
                ret['result'] = True
            else:
                ret['msg'] = RetMsg.Users.WRONG_PASSWORD
        else:
            ret['msg'] = RetMsg.Users.USER_NOT_EXIST
    return HttpResponse(json.dumps(ret))


@login_required
def do_logout(request):
    del request.session[SESSION_LOGIN_USER_ID]
    return HttpResponseRedirect(reverse('users:login'))