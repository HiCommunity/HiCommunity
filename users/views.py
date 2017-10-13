# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

from django.core.urlresolvers import reverse
from django.shortcuts import render, HttpResponse
from django.db.models import Q
from common.constants.common import RET_FORMAT
from common.utils.security import request_method, login_required
from users import models as users_models
from users.constants.common import SESSION_LOGIN_USER_ID, SESSION_LOGIN_USER_NAME
from users.utils import validation
from users.exception import *
from common.utils.js import js_str2bool


@request_method('GET')
def register_page(request):
    return render(request, 'users/register.html')


@request_method('POST')
def register(request):
    ret = RET_FORMAT
    password = request.POST.get('password')
    username = request.POST.get('username', '').strip()
    email = request.POST.get('email', '').strip()
    # validation
    if (not validation.validate_username(username)
            or not validation.validate_email(email)):
        raise InvalidUsernameOrEmailFormat
    elif not validation.validate_password(password):
        raise InvalidPasswordFormat

    # uniqueness check
    user_objects = users_models.Profile.objects.filter(Q(username=username) | Q(email=email))
    if user_objects.count() > 0:
        raise UsernameOrEmailAlreadyExist
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
    checked = js_str2bool(request.POST.get('checked'))

    # params validation
    if (not validation.validate_email(username_or_email) or not
            validation.validate_username(username_or_email)):
        raise InvalidUsernameOrEmailFormat
    elif not validation.validate_password(password):
        raise InvalidPasswordFormat
    else:
        username_or_email = username_or_email.strip()
        user_objects = users_models.Profile.objects.filter(
            Q(email=username_or_email) | Q(username=username_or_email))
        if user_objects.count() == 1:
            user_object = user_objects[0]
            if user_object.password == password:
                # login successfully
                if not checked:
                    request.session.set_expiry(0)
                request.session[SESSION_LOGIN_USER_ID] = user_object.id
                request.session[SESSION_LOGIN_USER_NAME] = user_object.username
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
        print('logout failed: %s' % str(e))
        raise UserLogoutFailed
    ret['result'] = True
    return HttpResponse(json.dumps(ret))
