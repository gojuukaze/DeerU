from django import template
from django.utils.safestring import mark_safe

from theme.manager.base_theme_manager import get_top_menu_htmltag_list, get_aside_category_htmltag, \
    get_aside_tag_htmltag_list, get_comment_tree, get_top_ico_htmltag_list
from tool.kblog_math import shuffle

register = template.Library()


@register.filter(name='top_menu')
def top_menu(menu_config):
    return get_top_menu_htmltag_list(menu_config)


@register.filter(name='top_ico')
def top_ico(ico_config, key):
    if key == 'logo':
        return get_top_ico_htmltag_list([ico_config[key]])

    return get_top_ico_htmltag_list(ico_config[key])


@register.filter(name='aside_category')
def aside_category(category):
    t = get_aside_category_htmltag(category)

    return t.format_html()


@register.filter(name='aside_tags')
def aside_tags(tags):
    if not tags:
        return []
    # l=['acm','dijkstra','elasticsearch','freopen','ik','multiprocessing','pool','poj','python','typedef','中文搜索','八数码','多进程','快排','指针','排序','搜索','最短路','翻译','计蒜客','进程池','迪杰斯特拉']
    # import random
    # t=[[random.randint(1,10),i] for i in l]
    # print(t)
    t = get_aside_tag_htmltag_list(tags)

    return shuffle(t)


@register.filter(name='comment_tree')
def comment_tree(comments):
    """
    返回排序后的评论树
    以下说的 评论、回复 其实是一个东西，方便区分用了两个词，具体看类Comment的说明

    child：包含评论的回复，和对这条评论下回复的回复，child不会再有child

    [ { 'comment' : Comment , 'child': [ {'comment' : Comment, 'to_nickname':'xx'} ] } ,{...}]
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
