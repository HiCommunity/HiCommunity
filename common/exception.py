# coding=utf-8

"""
Exceptions codes:
1 - 999: Http
1000 - 1999: users

...

9000 - 9999: common
"""


class HiException(Exception):
    # Base view exception
    desc = ''
    code = 0


"""
System common exceptions
9000 - 9999
"""


class CommonException(HiException):
    desc = 'Undefined common exception'
    code = 9000


class LoginRequired(HiException):
    desc = 'error:login required'
    code = 9001


"""
Http exceptions
1 - 999
"""


class HiHttp404(HiException):
    desc = 'error:http 404'
    code = 404
