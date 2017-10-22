# coding=utf-8
from users.constants.common import SESSION_LOGIN_USER


def common(request):
    user = request.session.get(SESSION_LOGIN_USER)
    return {
        'is_login': True if user else False
    }
