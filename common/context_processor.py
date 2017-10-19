# coding=utf-8
from users.constants.common import SESSION_LOGIN_USER_ID


def common(request):
    user_id = request.session.get(SESSION_LOGIN_USER_ID)
    return {
        'is_login': True if user_id else False
    }
