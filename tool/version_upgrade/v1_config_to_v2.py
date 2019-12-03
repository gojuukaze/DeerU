from ast import literal_eval
from pprint import pprint

from app.app_models.config_model import Config
from app.config_consts import Config_Schema_Dict
from app.consts import app_config_context
from app.db_manager.config_manager import get_config_by_name
from app.manager.config_manager import get_config_cache


def _get_config(name):
    print(app_config_context[name])
    config = get_config_by_name(app_config_context[name])
    temp_config = literal_eval(config.config)

    config_cache = get_config_cache(temp_config)
    return config, config_cache


def v1_attrs_to_v2(attrs: dict):
    r = ''
    i = 0
    for k, v in attrs.items():
        if i:
            r += '|'
        r += '%s=%s' % (k, v)
    return r


def v1_img_to_v2(img: dict):
    if len(img) == 0:
        return {" ": ""}
    r = {
        "_handler": "v2_img_handler",
    }
    if img['type'] == 'img':
        r['type'] = 'src'
        r['value'] = img['src']
        r['_attrs'] = v1_attrs_to_v2(img.get('attrs', {}))
    elif img['type'] == 'fa':
        r['type'] = 'fa'
        r['value'] = img['class']
        r['_attrs'] = v1_attrs_to_v2(img.get('attrs', {}))
    elif img['type'] == 'svg':
        r['type'] = 'svg'
        r['value'] = img['svg']
        r['_attrs'] = v1_attrs_to_v2(img.get('attrs', {}))

    return r


def _create_v2_blog_config():
    config, config_cache = _get_config('global_value')
    config.name = '%s.v1.old' % config.name
    config.save()
    v2_config = config_cache

    config, config_cache = _get_config('common_config')
    config.name = '%s.v1.old' % config.name
    config.save()

    v2_config.update(config_cache)

    Config.objects.create(
        name=app_config_context['v2_blog_config'],
        v2_schema=Config_Schema_Dict['v2_blog_config'],
        v2_config=v2_config).save()


def _create_v2_common_config():
    Config.objects.create(
        name=app_config_context['v2_common_config'],
        v2_schema=Config_Schema_Dict['v2_common_config'],
        v2_config={'_handler': 'v2_kv_handler', 'data': []}).save()


def _create_v2_iconbar_config():
    config, config_cache = _get_config('top_ico')
    config.name = '%s.v1.old' % config.name
    config.save()

    v2_config = {'left': {'logo': {}, 'blog_name': {}}, 'right': []}

    v2_config['left']['logo'] = v1_img_to_v2(config_cache['left']['logo'])
    v2_config['left']['blog_name'] = config_cache['left']['blog_name']
    v2_config['left']['blog_name']['_attrs'] = v1_attrs_to_v2(config_cache['left']['blog_name'].get('attrs', {}))
    v2_config['right'] = config_cache['right']
    v2_config['left']['blog_name'].pop('attrs')

    for i, img in enumerate(v2_config['right']):
        v2_config['right'][i]['img'] = v1_img_to_v2(config_cache['right'][i]['img'])

    Config.objects.create(
        name=app_config_context['v2_iconbar_config'],
        v2_schema=Config_Schema_Dict['v2_iconbar_config'],
        v2_config=v2_config).save()


def v1_menu_to_v2(old: dict, is_root=True):
    if 'line' in old:
        return old
    r = {
        'name': old['name'],
        "url": {
            "_handler": "v2_url_handler",
            "type": "url",
            "value": old.get('url', '')
        },
        'img': v1_img_to_v2(old.get('img', {})),
    }
    if is_root:
        r['children'] = []

        if 'children' in old:
            for c in old['children']:
                r['children'].append(v1_menu_to_v2(c, False))
    return r


def _create_v2_navbar_config():
    config, config_cache = _get_config('top_menu')
    config.name = '%s.v1.old' % config.name
    config.save()

    v2_config = {'menu': []}
    for old in config_cache:
        v2_config['menu'].append(v1_menu_to_v2(old))

    Config.objects.create(
        name=app_config_context['v2_navbar_config'],
        v2_schema=Config_Schema_Dict['v2_navbar_config'],
        v2_config=v2_config).save()


def config_v1_to_v2():
    _create_v2_blog_config()
    _create_v2_common_config()
    _create_v2_iconbar_config()
    _create_v2_navbar_config()
