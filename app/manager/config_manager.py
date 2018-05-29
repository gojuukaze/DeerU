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
