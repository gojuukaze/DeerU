from django import template

from tool.html_helper import clean_all_tags

register = template.Library()


@register.filter(name='clear_tag')
def clear_tag(s):
    """
    queryset.count()
    :return:
    """

    s= clean_all_tags(s).replace('&nbsp;', ' ').replace('\n', ' ')
    return s
