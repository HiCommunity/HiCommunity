# coding=utf-8

RET_FORMAT = {'result': False, 'msg': None}


class RetMsg(object):
    # Common
    class Common:
        ILLEGAL_ARGUMENTS = {'code': 1001, 'desc': 'illegal arguments'}

    # Users
    class Users:
        # account
        LOGIN_REQUIRED = {'code': 2001, 'desc': 'login required'}
        WRONG_PASSWORD = {'code': 2002, 'desc': 'wrong password'}
        USER_NOT_EXIST = {'code': 2003, 'desc': 'user not exist'}
        CREATE_USER_FAILED = {'code': 2004, 'desc': 'create user failed'}
        USER_ALREADY_LOGIN = {'code': 2005, 'desc': 'user already login'}

    # HTTP
    class HTTP:
        HTTP_404 = {'code': 404, 'desc': 'http 404 error'}