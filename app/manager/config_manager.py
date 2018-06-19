from django.core.cache import cache

from app.consts import Config_Name, Global_Value_Default, Global_value_cache_key, Theme_config_cache_key
from app.db_manager.config_manager import get_config_by_name
from ast import literal_eval


def get_global_value_by_key(name):
    try:
        global_value = cache.get(Global_value_cache_key, None)
        assert global_value is not None
    except:
        config = get_config_by_name(Config_Name['global_value'])
        global_value = literal_eval(config.config)
        cache.set(Global_value_cache_key, global_value, 3600)
    default = Global_Value_Default.get(name, '')

    return global_value.get(name, default)


def get_global_value():
    try:
        global_value = cache.get(Global_value_cache_key, None)
        assert global_value is not None
    except:
        config = get_config_by_name(Config_Name['global_value'])
        global_value = literal_eval(config.config)
        cache.set(Global_value_cache_key, global_value, 3600)

    return global_value


def get_theme_config():
    try:
        theme_config = cache.get(Theme_config_cache_key, None)
        assert theme_config is not None
    except:
        config = get_config_by_name(Config_Name['theme_config'])
        theme_config = literal_eval(config.config)
        cache.set(Theme_config_cache_key, theme_config, 3600)

    return theme_config


from app.deeru_expression.expressions import BaseExpression
from app.deeru_expression.manager import format_expression
from tool.deeru_html import Tag


def cache_config(config):
    """

    :param config: Config object
    :return:
    """

    if config.name == Config_Name['top_ico']:
        result = format_top_ico_config(config)
    elif config.name == Config_Name['top_menu']:
        result = format_top_menu_config(config)
    else:
        return

    config.cache = str(result)
    config.set_post_save_flag(False)
    config.save()


def get_img_tag(img):
    src = img.get('src', '')
    width = img.get('width', '')
    height = img.get('height', '')
    alt = img.get('alt', '')
    img_tag = Tag('img', attrs={'src': src, 'width': width, 'height': height, 'alt': alt})
    if height:
        img_tag.set_attr('style', 'max-height:' + height)
    return img_tag


def get_expression_result(s):
    if not s:
        return s
    result = format_expression(s)
    if isinstance(result, BaseExpression):
        result = result.get_result()
    return result


def format_top_ico_config(config):
    config = literal_eval(config.config)
    logo = get_expression_result(config['left'].get('logo'))
    blog_name = get_expression_result(config['left'].get('blog_name'))

    right_result = []
    for right_item in config['right']:
        img = get_expression_result(right_item.get('img'))
        url = get_expression_result(right_item.get('url', '#'))
        right_result.append({'img': img, 'url': url})
    return {
        'left': {'logo': logo, 'blog_name': blog_name},
        'right': right_result
    }


def format_top_menu_item(config):
    img = get_expression_result(config.get('img'))
    name = get_expression_result(config.get('name', ''))
    url = get_expression_result(config.get('url', ''))
    line = config.get('line')
    children = config.get('children')

    if line:
        return {'line': 'line'}

    result = {
        'img': img,
        'name': name,
        'url': url,
    }

    if children:

        children_result = []
        for c in children:
            children_result.append(format_top_menu_item(c))
        result['children'] = children_result

    return result


def format_top_menu_config(config):
    config = literal_eval(config.config)
    result = []
    for item in config:
        result.append(format_top_menu_item(item))
    return result
