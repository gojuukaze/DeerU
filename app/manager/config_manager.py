from django.core.cache import cache

from app.consts import Config_Name, Config_Default, Global_value_cache_key
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
    default = Config_Default.get(name, '')

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
