# coding=utf-8
from __future__ import unicode_literals

import json

from django.contrib import messages
from django.core.urlresolvers import reverse
from django.db.models import Max
from django.db.models import Q
from django.shortcuts import render, HttpResponse
from django.template.response import TemplateResponse

from common.constants.common import RET_FORMAT
from common.constants.messages import Privileges
from common.utils.js_ import js_str2bool
from users import forms as users_form
from users.exception import *
from users.models import Account
from users.forms import *
from users.utils.security import request_method, login_required
from users.utils.session import *
from users.view_helper import generate_avatar


@request_method('GET')
def register_page(request):
    return render(request, 'users/register.html')


@request_method('POST')
def register(request):
    ret = RET_FORMAT
    password = request.POST.get('password')
    username = request.POST.get('username', '').strip()
    email = request.POST.get('email', '').strip().lower()
    # validation
    # if (not validation.validate_username(username)
    #         or not validation.validate_email(email)):
    #     raise InvalidUsernameOrEmailFormat
    # elif not validation.validate_password(password):
    #     raise InvalidPasswordFormat

    # uniqueness check
    user_objects = Account.objects.filter(Q(username=username) |
                                          Q(email=email))
    if user_objects.count() > 0:
        raise UsernameOrEmailAlreadyExist

    # unique user uuid
    # _uuid = uuid.uuid5(uuid.NAMESPACE_OID, email)

    _id = Account.objects.values('id').aggregate(Max('id'))
    if _id:
        new_id = _id['id__max'] + 1
    else:
        new_id = 1

    # Try to create an avatar for user
    try:
        avatar, thumb_big, thumb_small = generate_avatar(new_id)
    except Exception as e:
        print('generate avatar failed: %s' % str(e))
        raise UserAccountCreateFailed

    # create account
    try:
        Account.objects.create(password=password,
                               username=username,
                               email=email,
                               avatar=avatar,
                               avatar_thumb_big=thumb_big,
                               avatar_thumb_small=thumb_small)
    except Exception as e:
        print('create user account failed: %s' % str(e))
        raise UserAccountCreateFailed
    else:
        messages.add_message(request, messages.SUCCESS,
                             Privileges.PLEASE_LOGIN % username)

    ret['result'] = True
    ret['redirect'] = reverse('users:accounts:login_page')
    return HttpResponse(json.dumps(ret))


@request_method('GET')
def login_page(request):
    # login form
    form = users_form.LoginForm(auto_id=True)
    context = {
        'form': form
    }
    return TemplateResponse(request, 'users/login.html', context=context)


@request_method('POST')
def login(request):
    # handle login user
    user_is_login = get_login_session(request)
    if user_is_login:
        raise UserAlreadyLogin
    ret = RET_FORMAT
    # clean data
    data = {
        'email': request.POST.get('email').strip(),
        'password': request.POST.get('password'),
        'keep_login': js_str2bool(request.POST.get('keep_login')),
        'password_length': request.POST.get('password_length'),
    }
    f = LoginForm(data=data, error_class=DivErrorList)
    if f.is_valid():
        email = f.cleaned_data['email']
        password = f.cleaned_data['password']
        keep_login = f.cleaned_data['keep_login']
        account_objects = Account.objects.filter(email=email)
        if account_objects.count() == 1:
            account_object = account_objects[0]
            if account_object.password == password:
                # login successfully
                if not keep_login:
                    request.session.set_expiry(0)
                set_login_session(request, account_object)
                ret['result'] = True
            else:
                raise InvalidPassword
        else:
            raise UsernameOrEmailNotExist
    else:
        err_data = f.errors.as_data()
        if err_data.get('email'):
            raise InvalidEmailFormat
        elif err_data.get('password') or err_data.get('password_length'):
            raise InvalidPasswordFormat
        # ret['message']['desc'] = errs[item][0].__str__
    return HttpResponse(json.dumps(ret))


@login_required()
@request_method('POST')
def logout(request):
    """
    Note Django does not provide automatic purging of expired sessions.
    Therefore we should call "django-admin clearsessions" command
    on a regular basis, for example as a daily cron job.
    """
    ret = RET_FORMAT
    del_login_session(request)
    ret['result'] = True
    return HttpResponse(json.dumps(ret))
