from ast import literal_eval
from pprint import pprint

from app.app_models.config_model import Config
from app.consts import app_config_context
from app.db_manager.config_manager import get_config_by_name
from app.manager.config_manager import get_config_cache

Config_Schema_Dict = {
    'v2_common_config': '{"disable_collapse":true,"disable_edit_json":true,"disable_properties":true,"object_layout":"grid","schema":{"type":"object","title":" ","properties":{"_handler":{"type":"string","enum":["v2_kv_handler"],"options":{"hidden":true}},"data":{"title":"通用配置","format":"table","type":"array","items":{"title":"配置","$ref":"#/definitions/global"}}},"definitions":{"global":{"type":"object","title":"配置","properties":{"key":{"title":"配置名","type":"string"},"value":{"title":"值","type":"string"}}}}}}',
    'v2_iconbar_config': '{"disable_collapse":true,"disable_edit_json":true,"disable_properties":true,"object_layout":"grid","schema":{"type":"object","title":"顶部图标栏配置","format":"categories","properties":{"left":{"title":"左边部分","type":"object","format":"categories","properties":{"logo":{"$ref":"#/definitions/img"},"blog_name":{"title":"博客名","type":"object","properties":{"text":{"type":"string"},"_attrs":{"$ref":"#/definitions/attrs"}}}}},"right":{"title":"右边部分","type":"array","format":"tabs","items":{"title":"图标","$ref":"#/definitions/imgWithUrl2"}}},"definitions":{"attrs":{"title":"属性","type":"string","description":"html标签的属性（多个属性用 | 分隔）","options":{"inputAttributes":{"placeholder":"如：style=color:#ffffff; | herf=/"}}},"img":{"type":"object","options":{"keep_oneof_values":false},"oneOf":[{"title":"无","additionalProperties":false,"type":"object","properties":{" ":{"type":"string","options":{"hidden":true}}},"options":{"keep_oneof_values":false}},{"title":"图片链接","additionalProperties":false,"type":"object","properties":{"_handler":{"type":"string","enum":["v2_img_handler"],"options":{"hidden":true}},"type":{"type":"string","enum":["src"],"options":{"hidden":true}},"value":{"type":"string","title":"地址","options":{"inputAttributes":{"placeholder":"链接，如： /media/logo_white.png , http://xxx/xx"}}},"_attrs":{"$ref":"#/definitions/attrs"}},"options":{"keep_oneof_values":false}},{"title":"图片id","additionalProperties":false,"type":"object","properties":{"_handler":{"type":"string","enum":["v2_img_handler"],"options":{"hidden":true}},"type":{"type":"string","enum":["id"],"options":{"hidden":true}},"value":{"type":"string","title":"id","options":{"inputAttributes":{"placeholder":"1"}}},"_attrs":{"$ref":"#/definitions/attrs"}},"options":{"keep_oneof_values":false}},{"title":"图片名","additionalProperties":false,"type":"object","properties":{"_handler":{"type":"string","enum":["v2_img_handler"],"options":{"hidden":true}},"type":{"type":"string","enum":["name"],"options":{"hidden":true}},"value":{"type":"string","title":"name","options":{"inputAttributes":{"placeholder":"logo.png"}}},"_attrs":{"$ref":"#/definitions/attrs"}},"options":{"keep_oneof_values":false}},{"title":"fontawesome图标","additionalProperties":false,"type":"object","properties":{"_handler":{"type":"string","enum":["v2_img_handler"],"options":{"hidden":true}},"type":{"type":"string","enum":["fa"],"options":{"hidden":true}},"value":{"type":"string","title":"图标","options":{"inputAttributes":{"placeholder":"fontawesome图标的class值，如：fab fa-github"}}},"_attrs":{"$ref":"#/definitions/attrs"}},"options":{"keep_oneof_values":false}},{"title":"svg图片","additionalProperties":false,"type":"object","properties":{"_handler":{"type":"string","enum":["v2_img_handler"],"options":{"hidden":true}},"type":{"type":"string","enum":["svg"],"options":{"hidden":true}},"value":{"type":"string","title":"svg","options":{"inputAttributes":{"placeholder":"<svg>...</svg>"}}},"_attrs":{"$ref":"#/definitions/attrs"}},"options":{"keep_oneof_values":false}}]},"imgWithUrl2":{"type":"object","options":{"object_layout":"normal"},"properties":{"img":{"$ref":"#/definitions/img"},"url":{"type":"string","options":{"inputAttributes":{"placeholder":"跳转链接"}}}}}}}}',

    'v2_navbar_config': '{"disable_collapse":true,"disable_edit_json":true,"disable_properties":true,"schema":{"type":"object","title":" ","properties":{"menu":{"title":"顶部导航栏配置","type":"array","format":"tabs","options":{"disable_collapse":false},"items":{"title":"导航","$ref":"#/definitions/menu"}}},"definitions":{"url":{"type":"object","options":{"keep_oneof_values":false},"oneOf":[{"title":"链接","options":{"keep_oneof_values":false},"additionalProperties":false,"properties":{"_handler":{"type":"string","enum":["v2_url_handler"],"options":{"hidden":true}},"type":{"type":"string","enum":["url"],"options":{"hidden":true}},"value":{"title":"地址","type":"string","options":{"inputAttributes":{"placeholder":"跳转链接"}}}}},{"title":"分类链接","options":{"keep_oneof_values":false},"additionalProperties":false,"properties":{"_handler":{"type":"string","enum":["v2_url_handler"],"options":{"hidden":true}},"type":{"type":"string","enum":["cat"],"options":{"hidden":true}},"value":{"title":"id/名称","type":"string","description":"优先匹配id","options":{"inputAttributes":{"placeholder":"分类id或者名称"}}}}},{"title":"tag链接","options":{"keep_oneof_values":false},"additionalProperties":false,"properties":{"_handler":{"type":"string","enum":["v2_url_handler"],"options":{"hidden":true}},"type":{"type":"string","enum":["tag"],"options":{"hidden":true}},"value":{"title":"id/名称","type":"string","description":"优先匹配id","options":{"inputAttributes":{"placeholder":"tag id或者名称"}}}}}]},"menu":{"type":"object","format":"categories","properties":{"name":{"title":"名字","type":"string","options":{"disable_collapse":true}},"url":{"$ref":"#/definitions/url","options":{"disable_collapse":true}},"img":{"$ref":"#/definitions/img","options":{"disable_collapse":true}},"children":{"title":"二级导航","type":"array","format":"tabs","options":{"disable_collapse":false},"items":{"title":"子导航","oneOf":[{"title":"分割线","type":"object","additionalProperties":false,"properties":{"line":{"type":"string","enum":["line"],"options":{"hidden":true}}}},{"title":"导航","additionalProperties":false,"options":{"disable_collapse":true},"$ref":"#/definitions/menuWithoutChildren"}]}}}},"attrs":{"title":"属性","type":"string","description":"html标签的属性（多个属性用 | 分隔）","options":{"inputAttributes":{"placeholder":"如：style=color:#ffffff; | herf=/"}}},"img":{"type":"object","options":{"keep_oneof_values":false},"oneOf":[{"title":"无","additionalProperties":false,"type":"object","properties":{" ":{"type":"string","options":{"hidden":true}}},"options":{"keep_oneof_values":false}},{"title":"图片链接","additionalProperties":false,"type":"object","properties":{"_handler":{"type":"string","enum":["v2_img_handler"],"options":{"hidden":true}},"type":{"type":"string","enum":["src"],"options":{"hidden":true}},"value":{"type":"string","title":"地址","options":{"inputAttributes":{"placeholder":"链接，如： /media/logo_white.png , http://xxx/xx"}}},"_attrs":{"$ref":"#/definitions/attrs"}},"options":{"keep_oneof_values":false}},{"title":"图片id","additionalProperties":false,"type":"object","properties":{"_handler":{"type":"string","enum":["v2_img_handler"],"options":{"hidden":true}},"type":{"type":"string","enum":["id"],"options":{"hidden":true}},"value":{"type":"string","title":"id","options":{"inputAttributes":{"placeholder":"1"}}},"_attrs":{"$ref":"#/definitions/attrs"}},"options":{"keep_oneof_values":false}},{"title":"图片名","additionalProperties":false,"type":"object","properties":{"_handler":{"type":"string","enum":["v2_img_handler"],"options":{"hidden":true}},"type":{"type":"string","enum":["name"],"options":{"hidden":true}},"value":{"type":"string","title":"name","options":{"inputAttributes":{"placeholder":"logo.png"}}},"_attrs":{"$ref":"#/definitions/attrs"}},"options":{"keep_oneof_values":false}},{"title":"fontawesome图标","additionalProperties":false,"type":"object","properties":{"_handler":{"type":"string","enum":["v2_img_handler"],"options":{"hidden":true}},"type":{"type":"string","enum":["fa"],"options":{"hidden":true}},"value":{"type":"string","title":"图标","options":{"inputAttributes":{"placeholder":"fontawesome图标的class值，如：fab fa-github"}}},"_attrs":{"$ref":"#/definitions/attrs"}},"options":{"keep_oneof_values":false}},{"title":"svg图片","additionalProperties":false,"type":"object","properties":{"_handler":{"type":"string","enum":["v2_img_handler"],"options":{"hidden":true}},"type":{"type":"string","enum":["svg"],"options":{"hidden":true}},"value":{"type":"string","title":"svg","options":{"inputAttributes":{"placeholder":"<svg>...</svg>"}}},"_attrs":{"$ref":"#/definitions/attrs"}},"options":{"keep_oneof_values":false}}]},"menuWithoutChildren":{"type":"object","format":"categories","properties":{"name":{"type":"string","options":{"disable_collapse":true}},"url":{"$ref":"#/definitions/url","options":{"disable_collapse":true}},"img":{"$ref":"#/definitions/img","options":{"disable_collapse":true}}}}}}}',

    'v2_blog_config': '''{"disable_collapse":true,"disable_edit_json":true,"disable_properties":true,"schema":{"type":"object","title":"博客配置","properties":{"title":{"type":"string","description":"title标签的值","default":"Deeru - 开源博客系统"},"blog_name":{"title":"博客名","type":"string","default":"Deeru - 开源博客系统"},"nickname":{"title":"你的昵称","type":"string","default":"gojuukaze"},"theme":{"title":"主题","type":"string","default":"base_theme"},"baidu_auto_push_show":{"title":"百度自动推送","format":"radio","type":"string","enum":["是","否"],"description":"使用百度提供的js自动推送文章地址"},"baidu_auto_push":{"type":"integer","watch":{"a":"root.baidu_auto_push_show"},"template":"{% if a == '是' %}1{% else %}0{% endif %}","options":{"hidden":true}}}}}''',
}
Config_JS = {
    'v2_navbar_config': r'''function changeName(obj) {let menu = obj.menu;for (let i = 0; i < menu.length; i++) {let name = menu[i].name;if (!name) {name = '导航' + (i + 1)}$('a#root\\.menu\\.' + i).text(name);$('div#root\\.menu\\.' + i).children('h4').children('label').text(name);let children = menu[i].children;for (let j = 0; j < children.length; j++) {if ('line' in children[j]) {name = '分割线';} else {name = children[j].name;}if (!name) {name = '子导航' + (j + 1);}$('a#root\\.menu\\.' + i + '\\.children\\.' + j).text(name);$('div#root\\.menu\\.' + i + '\\.children\\.' + j).children('label').text(name);}}}editor.on('change', function () {changeName(editor.getValue());});changeName(editor.getValue());''',

}


def _get_config(name):
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
        v2_config=v2_config,
        v2_script=Config_JS['v2_navbar_config']
    ).save()


def config_v1_to_v2():
    _create_v2_blog_config()
    _create_v2_common_config()
    _create_v2_iconbar_config()
    _create_v2_navbar_config()
