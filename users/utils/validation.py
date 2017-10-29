# coding=utf-8
import re
from common.utils.string_ import string_len

USERNAME_PAT = '^[^!@#$%^&*()\[\]{}<>,.?\\\\|/`~-]+$'
PASSWORD_PAT = '^[^\\\]{8,32}$'
EMAIL_PAT = '^[a-zA-Z0-9_-]+\@[a-zA-Z0-9_-]+\.[a-zA-Z0-9]{2,4}$'


def validate_username(username):
    return True if (username
                    and isinstance(username, str)
                    and 4 <= string_len(username) <= 16
                    and re.match(USERNAME_PAT, username)) else False


def validate_password(password):
    return True if (password
                    and isinstance(password, str)
                    and re.match(PASSWORD_PAT, password)) else False


def validate_email(email):
    return True if (email
                    and isinstance(email, str)
                    and re.match(EMAIL_PAT, email)) else False
