# coding=utf-8

from common.exception import HiException

"""
code: 1000 - 1999
"""


class UserException(HiException):
    desc = 'Undefined user exception'
    code = 1000


class InvalidUsernameOrEmailFormat(HiException):
    desc = 'Invalid username or email format'
    code = 1001


class InvalidPasswordFormat(HiException):
    desc = 'Invalid password format'
    code = 1002


class InvalidPassword(HiException):
    desc = 'Invalid password'
    code = 1003


class UsernameOrEmailNotExist(HiException):
    desc = 'Username or email not exist'
    code = 1004


class UserAlreadyLogin(HiException):
    desc = 'User already login'
    code = 1005


class UserAccountCreateFailed(HiException):
    desc = 'User account create failed'
    code = 1006


class UserLogoutFailed(HiException):
    desc = 'User logout failed'
    code = 1007