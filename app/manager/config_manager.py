from django.core.cache import cache

from app.consts import app_config_context, Global_Value_Default, Global_value_cache_key, Theme_config_cache_key, \
    Theme_cache_key
from app.db_manager.config_manager import get_config_by_name
from ast import literal_eval


def get_global_value_by_key(name):
    global_value = get_global_value()

    default = Global_Value_Default.get(name, '')

    return global_value.get(name, default)


def get_global_value():
    try:
        global_value = cache.get(Global_value_cache_key, None)
        assert global_value is not None
    except:
        config = get_config_by_name(app_config_context['global_value'])
        global_value = literal_eval(config.cache)
        cache.set(Global_value_cache_key, global_value, 3600)

    return global_value


def get_theme_config():
    try:
        theme_config = cache.get(Theme_config_cache_key, None)
        assert theme_config is not None
    except:
        config = get_config_by_name(app_config_context['common_config'])
        theme_config = literal_eval(config.config)
        cache.set(Theme_config_cache_key, theme_config, 3600)

    return theme_config


def get_theme():
    try:
        theme = cache.get(Theme_cache_key, None)
        assert theme is not None

    except:
        config = get_config_by_name(app_config_context['common_config'])
        try:
            theme = literal_eval(config.cache)['theme']
        except:
            theme = 'base_theme'
        cache.set(Theme_config_cache_key, theme, 3600)

    return theme


from app.deeru_expression.expressions import BaseExpression
from app.deeru_expression.manager import format_expression


def cache_config(config, is_init=False):
    """

    :param config: Config object
    :return:
    """

    temp_config = literal_eval(config.config)

    result = get_config_cache(temp_config)

    config.cache = str(result)
    if not is_init:
        config.set_post_save_flag(False)
    config.save()


def get_expression_result(s):
    if not s:
        return s
    result = format_expression(s)
    if isinstance(result, BaseExpression):
        result = result.get_result()
    return result


def get_config_cache(config):
    if isinstance(config, list):
        result = []
        for item in config:
            item_cached = get_config_cache(item)
            result.append(item_cached)
    elif isinstance(config, dict):
        result = {}
        for k, v in config.items():
            v_cached = get_config_cache(v)
            result[k] = v_cached
    elif isinstance(config, str):
        result = get_expression_result(config)
    else:
        result = config
    return result
