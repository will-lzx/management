from django import template
from home.models import *
register = template.Library()


def datetime_format(date_str):
    # format the datetime
    return date_str.strftime('%Y-%m-%d %H:%M:%S')


def get_lendcount(mobile_number):
    count = 0
    lendhistories = LendHistory.objects.all()
    for lend in lendhistories:
        if lend.mobile_number == mobile_number:
            count += 1
    return str(count)

register.filter('datetime_format', datetime_format)
register.filter('get_lendcount', get_lendcount)
