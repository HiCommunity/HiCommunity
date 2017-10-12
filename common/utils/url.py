# coding=utf-8
import re


def get_from_url(request, rel=True):
    """
    Get last history url
    :param request:
    :param rel: relative url
    :return:
    """
    from_url = request.META.get('HTTP_REFERER')
    if not from_url:
        return
    from_url = re.sub(r'^https?://.*?(/.*?/)\?.*$', r'\1', from_url)
    rel_from_url = re.sub(r'^https?://.*?(/.*?)', r'\1', from_url)
    return rel_from_url if rel else from_url
