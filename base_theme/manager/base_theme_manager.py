from django.urls import reverse
from django.utils.html import format_html

from tool.deeru_html import Tag
from tool.deeru_math import var


def get_img_tag(img_cofig, allow_none=False):
    if not img_cofig:
        if allow_none:
            return None
        else:
            return Tag('p', '[图片配置错误]')
    img_tag = None
    if img_cofig['type'] == 'img':
        img_tag = Tag('img')
        img_tag.set_attr('src', img_cofig['src'])

    elif img_cofig['type'] == 'svg':
        img_tag = Tag.get_tag_from_bs(img_cofig['svg'])

    elif img_cofig['type'] == 'fa':

        img_tag = Tag('span', attrs={'class': 'icon'})
        i_tag = Tag('i')
        i_tag.set_attr('class', img_cofig['class'])
        img_tag.append(i_tag)
    if not img_tag:
        return Tag('p', '图片配置错误')
    for k, v in img_cofig.get('attrs', {}).items():
        img_tag.set_attr(k, v)

    return img_tag


def format_menu_config(config):
    img = config.get('img')
    name = config.get('name', '')
    url = config.get('url', '')
    line = config.get('line')
    children = config.get('children')

    if line:
        return Tag('hr', attrs={'class': "navbar-divider"})

    img_tag = get_img_tag(img, allow_none=True)

    if children:

        children_tag = Tag('div', attrs={'class': 'navbar-dropdown is-boxed'})
        for c in children:
            children_tag.append(format_menu_config(c))

        name_tag = Tag('a', attrs={'class': 'navbar-link', 'href': url})
        if img_tag:
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


def get_page_html_list(paginator):
    number = paginator.current_page_num
    page = paginator.get_page_list()
    html1 = [{'text': format_html('<span class="icon is-small"><i class="fas fa-angle-double-left"></i></span>'),
              'disabled': '', 'is_current': '', 'href': ' '},
             {'text': format_html('<span class="icon is-small"><i class="fas fa-angle-left"></i></span>'),
              'disabled': '', 'is_current': '', 'href': ' '},
             {'text': format_html('<span class="icon is-small"><i class="fas fa-angle-right"></i></span>'),
              'disabled': '', 'is_current': '', 'href': ' '},
             {'text': format_html('<span class="icon is-small"><i class="fas fa-angle-double-right"></i></span>'),
              'disabled': '', 'is_current': '', 'href': ' '}]
    i = 0
    for p in page[:2] + page[-2:]:
        if p:
            html1[i]['href'] = '?page=%d' % (p,)
        else:
            html1[i]['href'] = 'javascript:void(0)'
            html1[i]['disabled'] = 'disabled'
        i += 1

    html2 = []
    for p in page[2]:
        html2.append({'text': '%d' % (p,), 'disabled': '',
                      'is_current': 'is-current' if p == number else '', 'href': '?page=%d' % (p,)})

    return html1[:2] + html2 + html1[-2:]


def get_comment_tree(comments):
    """
        返回排序后的评论树
        以下说的 评论、回复 其实是一个东西，方便区分用了两个词，具体看类Comment的说明

        child：包含评论的回复，和对这条评论下回复的回复，children不会再有children

        [ { 'comment' : Comment , 'children': [ {'comment' : Comment, 'to_nickname':'xx'} ] } ,{...}]
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
            result.append({'comment': c, 'children': []})
            root_comment_id_to_pos[c.id] = r_pos
            r_pos += 1
        else:
            to_pos = comment_id_to_pos[c.to_id]
            to_comment = comments[to_pos]

            root_pos = root_comment_id_to_pos[c.root_id]

            result[root_pos]['children'].append({'comment': c, 'to_nickname': to_comment.nickname})

        comment_id_to_pos[c.id] = c_pos
        c_pos += 1

    return result
