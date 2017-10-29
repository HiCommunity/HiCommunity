# coding=utf-8
import sys
import re

"""
字符串处理工具
"""


def string_len(string):
    """
    中文/其他非ASCII字符按照2个英文字符算
    :param string:
    :return:
    """
    length = None
    encoding = sys.getdefaultencoding()
    if encoding == 'utf-8':
        # Linux liked system
        length = len(string.encode('gbk'))
    else:
        # TODO: 系统编码不为utf-8时
        pass
    return length


def str2int(string, default):
    """
    String to Integer, like parseInt() in JavaScript
    :param string:
    :param default:
    :return:
    """
    if isinstance(string, int):
        return string
    else:
        res = re.findall(r'^([0-9]+)', string)
        if res:
            return int(res[0])
        else:
            if default and isinstance(default, int):
                return default
            else:
                return


def obj2list(obj):
    """
    Translate an common object to an iteration object
    :param obj: str, int, float, list, tuple
    :param res:
    :return:
    """
    return obj if isinstance(obj, (list, tuple, dict)) else [obj]
