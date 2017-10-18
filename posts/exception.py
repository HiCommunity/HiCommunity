# coding=utf-8
from common.exception import HiException

"""
System common exceptions
2000 - 2999
"""


class PostException(HiException):
    desc = 'Undefined post exception'
    code = 2000


class BlankContent(HiException):
    desc = 'Content can not be blank'
    code = 2001
