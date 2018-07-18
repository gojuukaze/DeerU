.. _theme:

==============
开发主题
==============

你可以使用django的模板开发主题，
如果你不想用django模板，你可以新建一个独立的前端工程，然后使用 `api插件 <https://github.com/gojuukaze/deeru-api>`_ 从后端获取数据。


如果你需要使用django的模板开发，下面给出了一些必要说明


* 创建django app:: 

    python manage.py start theme m_theme
|

    和插件不同，主题的目录下多了两个文件夹:: 

        m_theme/
            templates/
                m_theme

            static/
                m_theme

    编写代码时，你的html文件应放在 ``templates/m_theme`` 下，静态文件应放在 ``static/m_theme`` 下。

* 编写html

    你需要编写5个html模板，分别是（注意，模板名不能改变）：

        - home.html : 博客首页
        - detail_article.html : 文章页面
        - category.html : 分类下的文章列表页
        - tag.html : 标签下的文章列表页
        - detail_flatpage.html :  单页面

* url与html的对应关系

    - ``/`` : home.html
    - ``/article/<int:article_id>`` : detail_article.html
    - ``/category/<int:category_id>``  : category.html
    - ``/tag/<int:tag_id>`` : tag.html
    - ``/你的单页面前缀/<path:flatpage_url>`` : detail_flatpage.html

* view传递的context结构

    查看 :ref:`context` , :ref:`url-view`

* 在模板中使用软连接

    如果你需要在模板中引入静态文件，你应该这样做:: 

        {% load static %}
        <link href="{% static '/m_theme/css/m_theme.css' %}" />
        <script src="{% static '/m_theme/js/m_theme.js' %}"></script>

    如果你需要使用文章url或者其他url，你应该这样做:: 

        <a href="{% url 'app:detail_article' article.id %}>
        <a href="{{ article.url }}>

        <a href="{% url 'app:tag' 23 %}>
        <a href="{{ tag.url }}>

        <form action="{% url 'app:create_comment' %}" method="post"></form>



* 如何使用ui配置？

    如果你看了使用者指南你应该清楚，DeerU内置了"顶部导航栏"、"顶部图标栏"两个配置，你可以在view传到的context['config']中找到他们

    如果你的主题还需要其他配置，你可以把配置放到"通用配置"中，你也可以新建一个自己的配置。

    
* 如何新建配置？

    内置的配置满足不了你的需要，想增加一个"侧边栏配置"？

    首先你需要在 ``consts.py`` 的 ``m_theme_config_context`` 中加入你的配置:: 

        m_theme_config_context = {
            'm_theme_aside_config' : 'M_Theme侧边栏配置'
        }
    
    然后在admin中添加名为"M_Theme侧边栏配置"的配置，这样context就会传递你的配置，位置在 ``context['config']['m_theme_aside_config']`` 

* 关于评论的form

    文章详情页面传了一个 CommentForm ,但并不建议直接用它来生成form。另外，该form评论内容content生成的 ``<textarea>`` 并不是富文本编辑器。

    下面给了一个form的示例:: 

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