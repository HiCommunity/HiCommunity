# coding=utf-8
from django import template
import datetime

register = template.Library()


@register.filter(expects_localtime=True, is_safe=True)
def auto_date_format(origin_date):
    """
    Turn default date to self-defined format
    :param origin_date: default datetime format from templates
    :return:
    """
    cur_day = datetime.date.today()
    origin_day = origin_date.date()
    past_days = (cur_day - origin_day).days
    if 0 <= past_days <= 2:
        if past_days == 0:
            prefix = ''
        elif past_days == 1:
            prefix = '昨天 '
        else:
            prefix = '前天 '
        result = prefix + origin_date.strftime('%H:%M')
    else:
        # earlier than 3 days
        this_year = cur_day.year
        origin_year = origin_day.year
        if this_year == origin_year:
            result = origin_date.strftime('%m-%d %H:%M')
        else:
            result = origin_date.strftime('%Y-%m-%d %H:%M')
    return result
