__author__ = 'nani'
from datetime import date
from django.template.defaulttags import register


@register.simple_tag
def site_age(start):
    today__year = date.today().year
    if today__year == start:
        return start
    else:
        return "{0} - {1}".format(start, today__year)

