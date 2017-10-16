# coding=utf-8
import sys

"""
字符串处理工具
"""


def count_string_len(string):
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
