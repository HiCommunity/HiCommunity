# coding=utf-8
"""
user exception codes: 1000 - 1999

"""

from common.exception import HiException


class UserException(HiException):
    desc = 'Undefined user exception'
    code = 1000


""" 
login, register, logout
1001 - 1099
"""


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


class UsernameOrEmailAlreadyExist(HiException):
    desc = 'Username or email already exist'
    code = 1007


"""
Users' privileges
1901 - 1999
"""


class LoginRequired(HiException):
    desc = 'Login required'
    code = 1901


class UserRoleVerificationFailed(HiException):
    desc = 'Authority verification failed'
    code = 1902
