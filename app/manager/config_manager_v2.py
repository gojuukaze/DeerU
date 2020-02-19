from copy import deepcopy

from app.deeru_config_handler.manager import parse_attrs, format_config_handler


def get_real_config(real_config):
    """

    :param real_config:
    :type real_config: dict
    :return:
    :rtype: dict
    """
    if not real_config:
        return {}
    r = deepcopy(real_config)
    for k, v in real_config.items():
        if isinstance(v, dict):
            v = get_real_config(v)

            r[k] = v
        if isinstance(v, list):
            r[k] = parse_list_config(v)
        # todo 后面有时间替换为用handler处理
        if k == '_attrs':
            r['attrs'] = parse_attrs(v)
    if '_handler' in r:
        r = format_config_handler(r)
    return r


def parse_list_config(l):
    """

    :param l:
    :type l: list
    :return:
    :rtype: list
    """
    r = deepcopy(l)
    for i, item in enumerate(l):
        if isinstance(item, dict):
            r[i] = get_real_config(item)
    return r
