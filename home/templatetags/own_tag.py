from django import template
register = template.Library()


def datetime_format(date_str):
    # format the datetime
    return date_str.strftime('%Y-%m-%d %H:%M:%S')

register.filter('datetime_format', datetime_format)
