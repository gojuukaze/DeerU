from django.db.models import Count

from app.app_models.content_model import Tag, ArticleTag
from app.consts import app_config_context
from app.db_manager.config_manager import get_config_by_name
from app.db_manager.content_manager import get_tag_by_id
from app.manager.ct_manager import get_category_tree, get_category_tree2
from tool.deeru_exceptions import ConfigNotExistError
from ast import literal_eval


def get_top_ico():
    config = get_config_by_name(app_config_context['top_ico'])
    if not config:
        raise ConfigNotExistError("配置 '%s' 不存在" % app_config_context['top_ico'])
    top_ico = literal_eval(config.cache)
    return top_ico


def get_top_menu():
    config = get_config_by_name(app_config_context['top_menu'])
    if not config:
        raise ConfigNotExistError("配置 '%s' 不存在" % app_config_context['top_menu'])
    menu = literal_eval(config.cache)
    return menu


def get_aside_category():
    category_tree = get_category_tree()
    for k, v in category_tree.items():
        c_cat = v.get('children')
        if c_cat:
            for k2, v2 in c_cat.items():
                if v2.get('children'):
                    del v2['children']
    return category_tree


def get_aside_category2():
    return get_category_tree2()


def get_aside_tags():
    article_tag = ArticleTag.objects.values('tag_id').annotate(article_num=Count('id')).order_by('-article_num')[:20]
    aside_tags = [[get_tag_by_id(at['tag_id']), at['article_num']] for at in article_tag]
    fill_tags = []
    if len(aside_tags) != 20:
        fill_tags = Tag.objects.exclude(id__in=[at['tag_id'] for at in article_tag])[:20 - len(article_tag)]

        fill_tags = [[t, 0] for t in fill_tags]

    return aside_tags + fill_tags
