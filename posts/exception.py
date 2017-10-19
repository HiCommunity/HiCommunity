# coding=utf-8
from common.exception import HiException

"""
System common exceptions
2000 - 2999
"""


class PostException(HiException):
    desc = 'Undefined post exception'
    code = 2000


class EmptyContentIsNotAllowed(HiException):
    level = 'warning'
    desc = 'Empty content is not allowed'
    code = 2001


class CreateSubjectFailed(HiException):
    desc = 'Create subject failed'
    code = 2002

