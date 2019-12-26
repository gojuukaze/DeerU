from django_choices_enums import DjangoChoicesEnum

Global_value_cache_key = 'Global_value_cache_key'

app_config_context = {
    'top_ico': '顶部图标栏',
    'top_menu': '顶部导航栏',
    'global_value': '全局变量',
    'common_config': '通用配置',

    'v2_iconbar_config': '顶部图标栏配置',
    'v2_navbar_config': '顶部导航栏配置',
    'v2_common_config': '通用配置',
    'v2_blog_config': '博客配置',
}
v2_app_config_context = {

    'v2_iconbar_config': '顶部图标栏配置',
    'v2_navbar_config': '顶部导航栏配置',
    'v2_common_config': '通用配置',
    'v2_blog_config': '博客配置',
}

Global_Value_Default = {
    "title": "Deeru - 开源博客系统",
    "blog_name": "Deeru - 开源博客系统",
    "nickname": "gojuukaze",
}

Theme_config_cache_key = 'Theme_config_cache_key'

Theme_cache_key = 'Theme_cache_key'

Comment_Type = (
    (201, '对文章的评论'),
    (202, '对评论的评论')
)

FLAT_PAGE_URL_CACHE_KEY = '1deeruflatpageurl_cache'


class CommentStatusChoices(DjangoChoicesEnum):
    Created = (0, '待审核')
    Failed = (1, '未通过')
    Passed = (2, '通过')

    @staticmethod
    def valid_choices():
        return [0, 2]


# v2配置的参数
V2_Config_Schema = {
    'v2_common_config': '{"disable_collapse":true,"disable_edit_json":true,"disable_properties":true,"object_layout":"grid","schema":{"type":"object","title":" ","properties":{"_handler":{"type":"string","enum":["v2_kv_handler"],"options":{"hidden":true}},"data":{"title":"通用配置","format":"table","type":"array","items":{"title":"配置","$ref":"#/definitions/global"}}},"definitions":{"global":{"type":"object","title":"配置","properties":{"key":{"title":"配置名","type":"string"},"value":{"title":"值","type":"string"}}}}}}',
    'v2_iconbar_config': '{"disable_collapse":true,"disable_edit_json":true,"disable_properties":true,"object_layout":"grid","schema":{"type":"object","title":"顶部图标栏配置","format":"categories","properties":{"left":{"title":"左边部分","type":"object","format":"categories","properties":{"logo":{"$ref":"#/definitions/img"},"blog_name":{"title":"博客名","type":"object","properties":{"text":{"type":"string"},"_attrs":{"$ref":"#/definitions/attrs"}}}}},"right":{"title":"右边部分","type":"array","format":"tabs","items":{"title":"图标","$ref":"#/definitions/imgWithUrl2"}}},"definitions":{"attrs":{"title":"属性","type":"string","description":"html标签的属性（多个属性用 | 分隔）","options":{"inputAttributes":{"placeholder":"如：style=color:#ffffff; | herf=/"}}},"img":{"type":"object","options":{"keep_oneof_values":false},"oneOf":[{"title":"无","additionalProperties":false,"type":"object","properties":{" ":{"type":"string","options":{"hidden":true}}},"options":{"keep_oneof_values":false}},{"title":"图片链接","additionalProperties":false,"type":"object","properties":{"_handler":{"type":"string","enum":["v2_img_handler"],"options":{"hidden":true}},"type":{"type":"string","enum":["src"],"options":{"hidden":true}},"value":{"type":"string","title":"地址","options":{"inputAttributes":{"placeholder":"链接，如： /media/logo_white.png , http://xxx/xx"}}},"_attrs":{"$ref":"#/definitions/attrs"}},"options":{"keep_oneof_values":false}},{"title":"图片id","additionalProperties":false,"type":"object","properties":{"_handler":{"type":"string","enum":["v2_img_handler"],"options":{"hidden":true}},"type":{"type":"string","enum":["id"],"options":{"hidden":true}},"value":{"type":"string","title":"id","options":{"inputAttributes":{"placeholder":"1"}}},"_attrs":{"$ref":"#/definitions/attrs"}},"options":{"keep_oneof_values":false}},{"title":"图片名","additionalProperties":false,"type":"object","properties":{"_handler":{"type":"string","enum":["v2_img_handler"],"options":{"hidden":true}},"type":{"type":"string","enum":["name"],"options":{"hidden":true}},"value":{"type":"string","title":"name","options":{"inputAttributes":{"placeholder":"logo.png"}}},"_attrs":{"$ref":"#/definitions/attrs"}},"options":{"keep_oneof_values":false}},{"title":"fontawesome图标","additionalProperties":false,"type":"object","properties":{"_handler":{"type":"string","enum":["v2_img_handler"],"options":{"hidden":true}},"type":{"type":"string","enum":["fa"],"options":{"hidden":true}},"value":{"type":"string","title":"图标","options":{"inputAttributes":{"placeholder":"fontawesome图标的class值，如：fab fa-github"}}},"_attrs":{"$ref":"#/definitions/attrs"}},"options":{"keep_oneof_values":false}},{"title":"svg图片","additionalProperties":false,"type":"object","properties":{"_handler":{"type":"string","enum":["v2_img_handler"],"options":{"hidden":true}},"type":{"type":"string","enum":["svg"],"options":{"hidden":true}},"value":{"type":"string","title":"svg","options":{"inputAttributes":{"placeholder":"<svg>...</svg>"}}},"_attrs":{"$ref":"#/definitions/attrs"}},"options":{"keep_oneof_values":false}}]},"imgWithUrl2":{"type":"object","options":{"object_layout":"normal"},"properties":{"img":{"$ref":"#/definitions/img"},"url":{"type":"string","options":{"inputAttributes":{"placeholder":"跳转链接"}}}}}}}}',

    'v2_navbar_config': '{"disable_collapse":true,"disable_edit_json":true,"disable_properties":true,"schema":{"type":"object","title":" ","properties":{"menu":{"title":"顶部导航栏配置","type":"array","format":"tabs","options":{"disable_collapse":false},"items":{"title":"导航","$ref":"#/definitions/menu"}}},"definitions":{"url":{"type":"object","options":{"keep_oneof_values":false},"oneOf":[{"title":"链接","options":{"keep_oneof_values":false},"additionalProperties":false,"properties":{"_handler":{"type":"string","enum":["v2_url_handler"],"options":{"hidden":true}},"type":{"type":"string","enum":["url"],"options":{"hidden":true}},"value":{"title":"地址","type":"string","options":{"inputAttributes":{"placeholder":"跳转链接"}}}}},{"title":"分类链接","options":{"keep_oneof_values":false},"additionalProperties":false,"properties":{"_handler":{"type":"string","enum":["v2_url_handler"],"options":{"hidden":true}},"type":{"type":"string","enum":["cat"],"options":{"hidden":true}},"value":{"title":"id/名称","type":"string","description":"优先匹配id","options":{"inputAttributes":{"placeholder":"分类id或者名称"}}}}},{"title":"tag链接","options":{"keep_oneof_values":false},"additionalProperties":false,"properties":{"_handler":{"type":"string","enum":["v2_url_handler"],"options":{"hidden":true}},"type":{"type":"string","enum":["tag"],"options":{"hidden":true}},"value":{"title":"id/名称","type":"string","description":"优先匹配id","options":{"inputAttributes":{"placeholder":"tag id或者名称"}}}}}]},"menu":{"type":"object","format":"categories","properties":{"name":{"title":"名字","type":"string","options":{"disable_collapse":true}},"url":{"$ref":"#/definitions/url","options":{"disable_collapse":true}},"img":{"$ref":"#/definitions/img","options":{"disable_collapse":true}},"children":{"title":"二级导航","type":"array","format":"tabs","options":{"disable_collapse":false},"items":{"title":"子导航","oneOf":[{"title":"分割线","type":"object","additionalProperties":false,"properties":{"line":{"type":"string","enum":["line"],"options":{"hidden":true}}}},{"title":"导航","additionalProperties":false,"options":{"disable_collapse":true},"$ref":"#/definitions/menuWithoutChildren"}]}}}},"attrs":{"title":"属性","type":"string","description":"html标签的属性（多个属性用 | 分隔）","options":{"inputAttributes":{"placeholder":"如：style=color:#ffffff; | herf=/"}}},"img":{"type":"object","options":{"keep_oneof_values":false},"oneOf":[{"title":"无","additionalProperties":false,"type":"object","properties":{" ":{"type":"string","options":{"hidden":true}}},"options":{"keep_oneof_values":false}},{"title":"图片链接","additionalProperties":false,"type":"object","properties":{"_handler":{"type":"string","enum":["v2_img_handler"],"options":{"hidden":true}},"type":{"type":"string","enum":["src"],"options":{"hidden":true}},"value":{"type":"string","title":"地址","options":{"inputAttributes":{"placeholder":"链接，如： /media/logo_white.png , http://xxx/xx"}}},"_attrs":{"$ref":"#/definitions/attrs"}},"options":{"keep_oneof_values":false}},{"title":"图片id","additionalProperties":false,"type":"object","properties":{"_handler":{"type":"string","enum":["v2_img_handler"],"options":{"hidden":true}},"type":{"type":"string","enum":["id"],"options":{"hidden":true}},"value":{"type":"string","title":"id","options":{"inputAttributes":{"placeholder":"1"}}},"_attrs":{"$ref":"#/definitions/attrs"}},"options":{"keep_oneof_values":false}},{"title":"图片名","additionalProperties":false,"type":"object","properties":{"_handler":{"type":"string","enum":["v2_img_handler"],"options":{"hidden":true}},"type":{"type":"string","enum":["name"],"options":{"hidden":true}},"value":{"type":"string","title":"name","options":{"inputAttributes":{"placeholder":"logo.png"}}},"_attrs":{"$ref":"#/definitions/attrs"}},"options":{"keep_oneof_values":false}},{"title":"fontawesome图标","additionalProperties":false,"type":"object","properties":{"_handler":{"type":"string","enum":["v2_img_handler"],"options":{"hidden":true}},"type":{"type":"string","enum":["fa"],"options":{"hidden":true}},"value":{"type":"string","title":"图标","options":{"inputAttributes":{"placeholder":"fontawesome图标的class值，如：fab fa-github"}}},"_attrs":{"$ref":"#/definitions/attrs"}},"options":{"keep_oneof_values":false}},{"title":"svg图片","additionalProperties":false,"type":"object","properties":{"_handler":{"type":"string","enum":["v2_img_handler"],"options":{"hidden":true}},"type":{"type":"string","enum":["svg"],"options":{"hidden":true}},"value":{"type":"string","title":"svg","options":{"inputAttributes":{"placeholder":"<svg>...</svg>"}}},"_attrs":{"$ref":"#/definitions/attrs"}},"options":{"keep_oneof_values":false}}]},"menuWithoutChildren":{"type":"object","format":"categories","properties":{"name":{"type":"string","options":{"disable_collapse":true}},"url":{"$ref":"#/definitions/url","options":{"disable_collapse":true}},"img":{"$ref":"#/definitions/img","options":{"disable_collapse":true}}}}}}}',

    'v2_blog_config': '''{"disable_collapse":true,"disable_edit_json":true,"disable_properties":true,"schema":{"type":"object","title":"博客配置","properties":{"host":{"type":"string","title":"博客域名或ip","format":"url","options":{"inputAttributes":{"placeholder":"http://xxx"}}},"title":{"type":"string","description":"head中的title标签值","default":"Deeru - 开源博客系统"},"blog_name":{"title":"博客名","type":"string","default":"Deeru - 开源博客系统"},"nickname":{"title":"你的昵称","type":"string","default":"gojuukaze"},"theme":{"title":"主题","type":"string","default":"base_theme"},"baidu_auto_push_show":{"title":"百度自动推送","format":"radio","type":"string","enum":["是","否"],"description":"使用百度提供的js自动推送文章地址"},"baidu_auto_push":{"type":"integer","watch":{"a":"root.baidu_auto_push_show"},"template":"{% if a == '是' %}1{% else %}0{% endif %}","options":{"hidden":true}},"email":{"type":"object","title":"邮箱配置","description":"评论有回复时发送邮件提醒","options":{"keep_oneof_values":false},"oneOf":[{"title":"不启用","type":"object","properties":{"is_open":{"type":"boolean","enum":[false],"options":{"hidden":true}}}},{"title":"启用","type":"object","properties":{"is_open":{"type":"boolean","enum":[true],"options":{"hidden":true}},"smtp":{"title":"smtp地址","type":"string"},"port":{"type":"string","default":"25","format":"number"},"username":{"title":"邮箱地址","type":"string","format":"email"},"password":{"title":"邮箱密码","type":"string","format":"password","description":"建议使用客户端专用密码"},"secure":{"title":"协议","type":"string","enum":["无","ssl","tls"]}}}]}}}}'''
}
V2_Config_JS = {
    'v2_navbar_config': r'''function changeName(obj) {let menu = obj.menu;for (let i = 0; i < menu.length; i++) {let name = menu[i].name;if (!name) {name = '导航' + (i + 1)}$('a#root\\.menu\\.' + i).text(name).css({overflow: 'hidden', 'text-overflow':'ellipsis'});$('div#root\\.menu\\.' + i).children('h4').children('label').text(name);let children = menu[i].children;for (let j = 0; j < children.length; j++) {if ('line' in children[j]) {name = '分割线';} else {name = children[j].name;}if (!name) {name = '子导航' + (j + 1);}$('a#root\\.menu\\.' + i + '\\.children\\.' + j).text(name).css({overflow: 'hidden', 'text-overflow':'ellipsis'});$('div#root\\.menu\\.' + i + '\\.children\\.' + j).children('label').text(name);}}}editor.on('change', function () {changeName(editor.getValue());});changeName(editor.getValue());''',

}
