# coding=utf-8
import re
from common.utils.string import count_string_len

EMAIL_PAT = '^[a-zA-Z0-9_-]+\@[a-zA-Z0-9_-]+\.[a-zA-Z0-9]{2,4}$'


def validate_username(username):
    return True if (username
                    and isinstance(username, str)
                    and 4 <= count_string_len(username) <= 16) else False


def validate_password(password):
    return True if (password
                    and isinstance(password, str)
                    and re.match('\w{8,}', password)) else False


def validate_email(email):
    return True if (email
                    and isinstance(email, str)
                    and re.match(EMAIL_PAT, email)) else False