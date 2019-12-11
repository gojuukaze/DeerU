from ast import literal_eval
from app.consts import app_config_context, V2_Config_Schema, V2_Config_JS
from app.manager.config_manager import get_config_cache
from app.manager.config_manager_v2 import get_real_config


def _get_config(Config, name, suffix=''):
    name = app_config_context[name] + suffix
    config = Config.objects.get(name=name)
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
    if not img or len(img) == 0 or not isinstance(img, dict):
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


def _create_v2_blog_config(Config):
    config, config_cache = _get_config(Config, 'global_value')
    config.name = '%s.v1.old' % config.name
    config.save()
    v2_config = config_cache

    config, config_cache = _get_config(Config, 'common_config', suffix='.v1.old')
    config.name = '%s.v1.old' % config.name
    config.save()

    v2_config.update(config_cache)
    v2_config['host'] = ''
    v2_config['email'] = {'is_open': False}

    Config.objects.create(
        name=app_config_context['v2_blog_config'],
        v2_schema=V2_Config_Schema['v2_blog_config'],
        v2_config=v2_config,
        v2_real_config=get_real_config(v2_config))


def _create_v2_common_config(Config):
    config, config_cache = _get_config(Config, 'common_config')
    config.name = '%s.v1.old' % config.name
    config.save()

    Config.objects.create(
        name=app_config_context['v2_common_config'],
        v2_schema=V2_Config_Schema['v2_common_config'],
        v2_config={'_handler': 'v2_kv_handler', 'data': []},
        v2_real_config={})


def _create_v2_iconbar_config(Config):
    config, config_cache = _get_config(Config, 'top_ico')
    config.name = '%s.v1.old' % config.name
    config.save()

    v2_config = {'left': {'logo': {}, 'blog_name': {}}, 'right': []}

    v2_config['left']['logo'] = v1_img_to_v2(config_cache['left']['logo'])
    blog_name = config_cache['left']['blog_name']
    if not isinstance(blog_name, dict):
        blog_name = {}
    v2_config['left']['blog_name'] = blog_name
    v2_config['left']['blog_name']['_attrs'] = v1_attrs_to_v2(blog_name.get('attrs', {}))
    v2_config['right'] = config_cache['right']
    try:
        v2_config['left']['blog_name'].pop('attrs')
    except:
        pass

    for i, img in enumerate(v2_config['right']):
        v2_config['right'][i]['img'] = v1_img_to_v2(config_cache['right'][i]['img'])

    Config.objects.create(
        name=app_config_context['v2_iconbar_config'],
        v2_schema=V2_Config_Schema['v2_iconbar_config'],
        v2_config=v2_config,
        v2_real_config=get_real_config(v2_config))


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


def _create_v2_navbar_config(Config):
    config, config_cache = _get_config(Config, 'top_menu')
    config.name = '%s.v1.old' % config.name
    config.save()

    v2_config = {'menu': []}
    for old in config_cache:
        v2_config['menu'].append(v1_menu_to_v2(old))

    Config.objects.create(
        name=app_config_context['v2_navbar_config'],
        v2_schema=V2_Config_Schema['v2_navbar_config'],
        v2_config=v2_config,
        v2_script=V2_Config_JS['v2_navbar_config'],
        v2_real_config=get_real_config(v2_config)
    )


def config_v1_to_v2(Config):
    _create_v2_common_config(Config)
    _create_v2_iconbar_config(Config)
    _create_v2_navbar_config(Config)
    _create_v2_blog_config(Config)
