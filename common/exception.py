# coding=utf-8

"""
Exceptions codes:
1 - 999: Http
1000 - 1999: users
2000 - 2999: posts
...

9000 - 9999: common
"""


class HiException(Exception):
    # Base view exception
    # level: error, warning, info, default
    level = 'error'
    desc = 'Undefined exception'
    code = 0


"""
System common exceptions
9000 - 9999
"""


class CommonException(HiException):
    desc = 'Undefined common exception'
    code = 9000


"""
Http exceptions
1 - 999
"""


class HiHttp404(HiException):
    desc = 'http 404'
    code = 404
