# coding=utf-8
from common.exception import HiException

"""
Question exceptions
2000 - 2999
"""


class QuestionException(HiException):
    desc = 'Undefined question exception'
    code = 2000


class CreateQuestionFailed(HiException):
    desc = 'Create question failed'
    code = 2002


class CreateAnswerFailed(HiException):
    desc = 'Create answer failed'
    code = 2003


class RegionOrBoardNotExist(HiException):
    desc = 'Region or board not exist'
    code = 2901

