# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

from django.core.urlresolvers import reverse
from django.shortcuts import (render, render_to_response, HttpResponse,
                              HttpResponseRedirect)
from common.constants.common import RET_FORMAT
from common.utils.security import request_method, login_required
from users import models as users_models
from users.constants.common import SESSION_LOGIN_USER_ID, SESSION_LOGIN_USER_NAME
from users.utils import validation
from users.exception import *


@request_method('GET')
def register_page(request):
    return render(request, 'users/register.html')


@request_method('POST')
def register(request):
    ret = RET_FORMAT
    password = request.POST.get('password')
    username = request.POST.get('username', '').strip()
    email = request.POST.get('email', '').strip()
    if (not validation.validate_username(username) or
        not validation.validate_email(email)):
        raise InvalidUsernameOrEmailFormat
    elif not validation.validate_password(password):
        raise InvalidPasswordFormat
    try:
        users_models.Profile.objects.create(password=password,
                                            username=username,
                                            email=email)
    except Exception as e:
        print('create user failed: %s' % str(e))
        raise UserAccountCreateFailed
    else:
        ret['result'] = True
        ret['msg']['redirect_url'] = reverse('users:login_page')
    return HttpResponse(json.dumps(ret))


@request_method('GET')
def login_page(request):

    return render(request, 'users/login.html')


@request_method('POST')
def login(request):
    # handle login user
    user_id = request.session.get(SESSION_LOGIN_USER_ID)
    if user_id:
        raise UserAlreadyLogin

    ret = RET_FORMAT
    username_or_email = request.POST.get('username_or_email')
    password = request.POST.get('password')
    valid_user_form = None
    if validation.validate_email(username_or_email) :
        valid_user_form = 'email'
    elif validation.validate_username(username_or_email):
        valid_user_form = 'username'
    # if not valid_user_form or not validation.validate_password(password):
    #     # RegEx filter first
    #     ret['msg'] = RetMsg.Common.ILLEGAL_ARGUMENTS
    if not valid_user_form:
        raise InvalidUsernameOrEmailFormat
    elif not validation.validate_password(password):
        raise InvalidPasswordFormat
    else:
        username_or_email = username_or_email.strip()
        if valid_user_form == 'email':
            user_objs = users_models.Profile.objects.filter(
                email=username_or_email)
        else:
            user_objs = users_models.Profile.objects.filter(
                username=username_or_email)
        if user_objs.count() == 1:
            user_obj = user_objs[0]
            if user_obj.password == password:
                # login successfully
                request.session[SESSION_LOGIN_USER_ID] = user_obj.id
                request.session[SESSION_LOGIN_USER_NAME] = user_obj.username
                ret['result'] = True
            else:
                raise InvalidPassword
        else:
            raise UsernameOrEmailNotExist
    return HttpResponse(json.dumps(ret))


@login_required
@request_method('DELETE')
def logout(request, *args, **kwargs):
    ret = RET_FORMAT
    try:
        del request.session[SESSION_LOGIN_USER_ID]
    except Exception as e:
        raise UserLogoutFailed
    ret['result'] = True
    return HttpResponse(json.dumps(ret))