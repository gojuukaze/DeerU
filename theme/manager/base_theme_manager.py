from django.urls import reverse

from tool.kblog_expression.expressions import BaseExpression
from tool.kblog_expression.manager import format_expression
from tool.kblog_html import Tag
from tool.kblog_math import var, sta


def get_img_tag(img):
    if not img:
        return None
    if isinstance(img, BaseExpression) and isinstance(img.get_result(), Tag):
        return img.get_result()
    src = img.get('src', '')
    width = img.get('width', '')
    height = img.get('height', '')
    alt = img.get('alt', '')
    img_tag = Tag('img', attrs={'src': src, 'width': width, 'height': height, 'alt': alt})
    if height:
        img_tag.set_attr('style', 'max-height:' + height)
    return img_tag


def format_ico_config(config):
    img = format_expression(config.get('img'))
    url = format_expression(config.get('url', '#'))
    print(img)
    img_tag = get_img_tag(img)
    a_tag = Tag('a', attrs={'href': url, 'class': 'navbar-item'})
    a_tag.append(img_tag)
    return a_tag


def get_top_ico_htmltag_list(config):
    result = []
    for c in config:
        result.append(format_ico_config(c))
    return result


def format_menu_config(config):
    img = format_expression(config.get('img'))
    name = format_expression(config.get('name', ''))
    url = format_expression(config.get('url', ''))
    line = config.get('line')
    children = config.get('children')

    if line:
        return Tag('hr', attrs={'class': "navbar-divider"})

    img_tag = get_img_tag(img)

    if children:

        children_tag = Tag('div', attrs={'class': 'navbar-dropdown is-boxed'})
        for c in children:
            children_tag.append(format_menu_config(c))

        name_tag = Tag('a', attrs={'class': 'navbar-link', 'href': url})
        name_tag.append(img_tag)
        name_tag.append(Tag('span', text=name))
        div_tag = Tag('div', attrs={'class': 'navbar-item has-dropdown is-hoverable'})
        div_tag.append(name_tag)
        div_tag.append(children_tag)
        return div_tag

    else:
        div_tag = Tag('a', attrs={'class': 'navbar-item', 'href': url})
        div_tag.append(img_tag)
        div_tag.append(Tag('span', text=name))
        return div_tag


def get_top_menu_htmltag_list(menu):
    menu_html = []
    for m in menu:
        menu_html.append(format_menu_config(m))
    return menu_html


def category_to_aside_category_htmltag(id, name, has_child, is_child=False):
    div = Tag('div', attrs={'class': 'panel-block'})
    name = Tag('a', name, attrs={'class': 'red_child_a' if is_child else 'red_a',
                                 'href': reverse('app:category_article', args=(id,))})

    if not has_child:
        div.append(name)
        return div
    else:
        inner_div = Tag('div', attrs={'class': 'control'})
        but = Tag('span', attrs={'class': 'icon', 'style': 'position: absolute;right: 0;'})
        but.append(Tag('i', attrs={'class': 'fas fa-chevron-down', 'aria-hidden': 'true'}))
        inner_div.append(name)
        inner_div.append(but)
        div.append(inner_div)
        return div


def get_aside_category_htmltag(category):
    nav = Tag('nav', attrs={'class': 'panel mpanel has-shadow'})
    head = Tag('p', attrs={'class': 'panel-heading'})
    head.append(Tag('strong', '分类'))
    nav.append(head)

    for id, v in category.items():
        child = v.get('children')
        nav.append(category_to_aside_category_htmltag(id, v['name'], child))
        if child:
            outer_div = Tag('div', attrs={'class': 'panel-child'})
            for id2, v2 in child.items():
                outer_div.append(category_to_aside_category_htmltag(id2, v2['name'], False, True))
            nav.append(outer_div)
    return nav


def get_aside_tag_htmltag_list(aside_tags):
    article_num = [at[1] for at in aside_tags]

    article_var = var(article_num)

    for t in aside_tags:
        if t[1] > article_var:
            t.append('25px')
        else:
            t.append('')
    return aside_tags


def get_comment_tree(comments):
    """
        返回排序后的评论树
        以下说的 评论、回复 其实是一个东西，方便区分用了两个词，具体看类Comment的说明

        child：包含评论的回复，和对这条评论下回复的回复，child不会再有child

        [ { 'comment' : Comment , 'child': [ {'comment' : Comment, 'to_nickname':'xx'} ] } ,{...}]
        :return:
    """
    result = []
    # 根评论在result中的位置,id:pos
    root_comment_id_to_pos = {}

    # 评论在queryset中的位置,id:pos
    comment_id_to_pos = {}

    r_pos = 0
    c_pos = 0
    for c in comments:
        if c.type == 201:
            # 根评论
            result.append({'comment': c, 'child': []})
            root_comment_id_to_pos[c.id] = r_pos
            r_pos += 1
        else:
            to_pos = comment_id_to_pos[c.to_id]
            to_comment = comments[to_pos]

            root_pos = root_comment_id_to_pos[c.root_id]

            result[root_pos]['child'].append({'comment': c, 'to_nickname': to_comment.nickname})

        comment_id_to_pos[c.id] = c_pos
        c_pos += 1

    return result
