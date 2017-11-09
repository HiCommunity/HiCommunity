# coding=utf-8

__all__ = [
    'set_login_session',
    'get_login_session',
    'del_login_session'
]

SESSION_LOGIN_USER = 'login_user'


def set_login_session(request, account_object):
    request.session[SESSION_LOGIN_USER] = {
        'id': account_object.id,
        'name': account_object.username,
        'email': account_object.email,
        'role': account_object.role,
        'avatar': {
            'origin': str(account_object.avatar),
            'thumb_big': str(account_object.avatar_thumb_big),
            'thumb_small': str(account_object.avatar_thumb_small)
        }
    }


def get_login_session(request):
    return request.session.get(SESSION_LOGIN_USER)


def del_login_session(request):
    try:
        del request.session[SESSION_LOGIN_USER]
    except KeyError:
        pass
