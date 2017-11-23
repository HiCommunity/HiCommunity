# coding=utf-8
from common.constants.common import RET_FORMAT

__all__ = [
    'ret_format'
]


def ret_format(result=False, message=None, redirect='', data=None):
    if message is None:
        message = {}
    if data is None:
        data = {}
    assert (isinstance(message, dict) and
            isinstance(data, dict)), 'A dict object is expected'
    res = RET_FORMAT
    if result:
        res['result'] = result
    if message:
        res['message'] = message
    if redirect:
        res['redirect'] = redirect
    if data:
        res['data'] = data
    return res

