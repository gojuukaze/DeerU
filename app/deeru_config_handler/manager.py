import re

from app.manager.config_manager import get_global_value_by_key
from django.conf import settings


def parse_attrs(attrs_str):
    """
    对attrs进行特殊处理
    "style=xx | href=xx"
    返回
    {
       'style':'xx',
       'href':'xx'
    }
    
    :param attrs_str: str
    :return:
    :rtype: dict
    """
    attrs_str = attrs_str.strip()
    if not attrs_str:
        return {}
    attrs = {}
    for temp in attrs_str.strip().split('|'):
        k, v = temp.split('=')
        attrs[k.strip()] = v.strip()
    return attrs


def format_config_handler(config):
    """

    :param config:
    :type config: dict
    :return:
    :rtype:
    """
    name = config.get('_handler', None)
    if not name:
        return config
    c = settings.CONFIG_HANDLER_DICT.get(name, None)
    if not c:
        return config
    return c(config).calculate()
