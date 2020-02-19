import re

from django import template
from django.utils.safestring import mark_safe

from tool.html_helper import clean_all_tags

register = template.Library()


@register.filter(name='clean')
def clean(content, length=None):
    """
    content截短
    :param length:
    :type length:
    :param content:
    :type content: str
    :return:
    :rtype:
    """
    content = content.replace('&nbsp;', ' ')
    content = re.sub('&lt;.*?&gt;', '', content)
    if length:
        length = int(length)
        return clean_all_tags(content)[:length] + '...'
    else:
        return clean_all_tags(content)
