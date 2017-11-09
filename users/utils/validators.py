# coding=utf-8
import re
from common.utils.string_ import string_len
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

USERNAME_PAT = '^[^!@#$%^&*()\[\]{}<>,.?\\\\|/`~-]+$'
PASSWORD_PAT = '^[^\\\]{8,32}$'
EMAIL_PAT = '^[a-zA-Z0-9_-]+\@[a-zA-Z0-9_-]+\.[a-zA-Z0-9]{2,4}$'


def validate_username(username):
    if not all((
            username,
            isinstance(username, str),
            4 <= string_len(username) <= 16,
            re.match(USERNAME_PAT, username),)):
        raise ValidationError(
            _('%(username)s is not a valid username'),
            code='invalid',
            params={'username': username},
        )


def validate_password(password):
    if not all((password,
                isinstance(password, str),
                re.match(PASSWORD_PAT, password))):
        raise ValidationError(
            _('%(password)s is not a valid password'),
            code='invalid',
            params={'password': password},
        )


def validate_email(email):
    if not all((email,
                isinstance(email, str),
                re.match(EMAIL_PAT, email))):
        raise ValidationError(
            _('%(email)s is not a valid email'),
            params={'email': email},
        )
