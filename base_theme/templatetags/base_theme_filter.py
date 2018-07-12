from django import template
from django.utils.safestring import mark_safe

from base_theme.manager.base_theme_manager import get_top_menu_htmltag_list, get_aside_category_htmltag, \
    get_aside_tag_htmltag_list, get_comment_tree, get_page_html_list, get_img_tag

register = template.Library()


@register.filter(name='top_menu')
def top_menu(menu_config):
    return get_top_menu_htmltag_list(menu_config)


@register.filter(name='get_img')
def get_img(img_config):
    return mark_safe(get_img_tag(img_config))


@register.filter(name='type')
def get_type(arg):
    return type(arg)


@register.filter(name='aside_category')
def aside_category(category):
    t = get_aside_category_htmltag(category)

    return t.format_html()


@register.filter(name='aside_tags')
def aside_tags(tags):
    if not tags:
        return []
    t = get_aside_tag_htmltag_list(tags)
    return t

    # return shuffle(t)


@register.filter(name='page_list')
def page_list(paginator):
    return get_page_html_list(paginator)


@register.filter(name='comment_tree')
def comment_tree(comments):
    """
    返回排序后的评论树
    以下说的 评论、回复 其实是一个东西，方便区分用了两个词，具体看类Comment的说明

    child：包含评论的回复，和对这条评论下回复的回复，child不会再有child

    [ { 'comment' : Comment , 'children': [ {'comment' : Comment, 'to_nickname':'xx'} ] } ,{...}]
    :return:
    """
    t = get_comment_tree(comments)

    return t


@register.filter(name='q_count')
def q_count(q):
    """
    queryset.count()
    :return:
    """
    try:
        return q.count()
    except:
        return 0
