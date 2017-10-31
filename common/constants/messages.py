# coding=utf-8
"""
Messages for Django message framework
"""


class Privileges(object):
    # privileges

    NEED_LOGIN_FIRST = '请先登录再进行下一步操作'
    NOT_ALLOWED_TO_ACCESS = '你的账号未被授权访问该页面'
    PLEASE_LOGIN = '%s，欢迎加入，请登录'
