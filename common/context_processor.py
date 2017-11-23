# coding=utf-8
from users.utils.session import get_login_session


def common(request):
    login_user = get_login_session(request)
    return {
        'is_login': True if login_user else False
    }
