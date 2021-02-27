.. _templates:

==================
主题开发的其他说明
==================


在html中应使用软连接
=====================

如果你需要在html中引入本地静态文件，你应该这样做::

    {% load static %}
    <link href="{% static '/custom_theme/css/m_theme.css' %}" />
    <script src="{% static '/custom_theme/js/m_theme.js' %}"></script>

如果你需要使用文章url或者其他url，你应该这样做::

    <a href="{% url 'app:detail_article' article.id %}>
    <a href="{{ article.url }}>

    <a href="{% url 'app:tag' 23 %}>
    <a href="{{ tag.url }}>

    <form action="{% url 'app:create_comment' %}" method="post"></form>


如何在html中读取新建的配置？
==============================

在admin中新建的配置默认在html代码中是无法获取，你需要修改两个地方

1. 新建 ``custom_theme/consts.py`` 文件，并添加 ``custom_theme_config_context`` ::

    custom_theme_config_context = {
        'my_config' : '我的自定义配置'
    }

2. 在 ``custom_theme/app.py`` 中添加 ``deeru_config_context`` ::

   class CustomThemeConfig(AppConfig):
       ...
       deeru_config_context = 'custom_theme.consts.custom_theme_config_context'


关于评论的form
====================

文章详情页面传了一个 CommentForm ,但并不建议直接用它来生成form。另外，该form评论中content生成的 ``<textarea>`` 并不是富文本编辑器。

下面给了一个form的示例

.. code-block:: html

        {% csrf_token %}

        <div class="fieldWrapper">
            {{ comment_form.nickname }}
            {% if comment_form.nickname.help_text %}
                <p class="help">{{ comment_form.nickname.help_text|safe }}</p>
            {% endif %}
        </div>

        <div class="fieldWrapper">
            {{ comment_form.email }}
            {% if comment_form.email.help_text %}
                <p class="help">{{ comment_form.email.help_text|safe }}</p>
            {% endif %}
        </div>

        <div class="fieldWrapper">
            {{ comment_form.content }}
            {% if comment_form.content.help_text %}
                <p class="help">{{ comment_form.content.help_text|safe }}</p>
            {% endif %}
        </div>

        <input type="hidden" name="article_id" id="id_article_id" value="{{ article.id }}">
        <input type="hidden" name="root_id" id="id_root_id" value="-1">
        <input type="hidden" name="to_id" id="id_to_id" value="-1">
        <input type="hidden" name="type" id="id_type" value="201">
        <input type="hidden" name="anchor" value="#comment">
        <div class="field" style="margin-top: 10px;display: flex">
            {{ comment_form.captcha }}
        </div>

        <!-- v2.0新增了评论验证码，还需要添加下面js代码 -->
        <script>
            $('.captcha').click(function () {
                $.getJSON("/captcha/refresh/", function (result) {
                    $('.captcha').attr('src', result['image_url']);
                    $('#id_captcha_0').val(result['key'])
                });
            });
        </script>


如何对主题进行大改
====================

如果需要对主题进行大改，有两种方法：

1. 实现所有模块，并在 settings 中修改 ``BASE_THEME2_TEMPLATES`` 指向你的html文件

2. 只实现几个关键的模块。

   一般你只需要实现 ``head_static_template``, ``body_navbar_template``, ``body_footer_template``, ``article_list_template``, ``detail_article_template``, ``detail_flatpage_template``, ``404_template`` ，
