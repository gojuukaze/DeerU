from app.forms import CommentForm
from app.manager import get_config_context
from app.manager.article import get_article_list_and_paginator, get_article_list_and_paginator_by_category, \
    get_article_list_and_paginator_by_tag
from base_theme2.theme import HomeTemplate, DetailArticleTemplate, DetailFlatpageTemplate, Page404Template


def get_extend_data():
    from app.manager.uiconfig_manager import get_aside_category2, get_aside_tags
    return {
        'category': get_aside_category2(),
        'tags': get_aside_tags()
    }


def get_home_template(page, per_page=7):
    article_list, paginator = get_article_list_and_paginator(page, per_page)
    return HomeTemplate(get_config_context(), article_list, paginator, None, get_extend_data())


def get_category_template(category, page, per_page=7):
    article_list, paginator = get_article_list_and_paginator_by_category(category.id, page, per_page)
    return HomeTemplate(get_config_context(), article_list, paginator, ['分类', category.name], get_extend_data())


def get_tag_template(tag, page, per_page=7):
    article_list, paginator = get_article_list_and_paginator_by_tag(tag.id, page, per_page)
    return HomeTemplate(get_config_context(), article_list, paginator, ['标签', tag.name], get_extend_data())


def get_detail_article_template(article, form_error):
    comment_form = CommentForm()
    return DetailArticleTemplate(get_config_context(), article, comment_form, form_error, get_extend_data())


def get_detail_flatpage_template(flatpage):
    return DetailFlatpageTemplate(get_config_context(), flatpage, get_extend_data())


def get_404_template():
    return Page404Template(get_config_context(), get_extend_data())
