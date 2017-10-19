# coding=utf-8
from common.exception import HiException

"""
Post exceptions
2000 - 2999
"""


class PostException(HiException):
    desc = 'Undefined post exception'
    code = 2000


class CreatePostFailed(HiException):
    desc = 'Create post failed'
    code = 2002


class RegionOrBoardNotExist(HiException):
    desc = 'Region or board not exist'
    code = 2901

