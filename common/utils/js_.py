# coding=utf-8


def js_str2bool(string):
    if isinstance(string, str):
        # '0' is recognized as True
        return (False if not string or
                string in ('false', 'null', 'undefined') else True)
