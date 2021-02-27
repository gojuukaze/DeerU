.. _theme-start:

==============
快速开始
==============

跟随这篇教程，帮助你快速对主题进行修改。

开始之前需要新建个app ( **注意，app名必须是custom_开头**) ::

   python manage.py starttheme custom_theme

执行之后会 custom_theme app, 目录结构如下 ::

    custom_theme/
        templates/
            custom_theme
        static/
            custom_theme
        admin.py
        apps.py

* html 代码应放在 ``custom_theme/templates/custom_theme`` 下; 静态文件应放在 ``custom_theme/static/custom_theme`` 下。


在底部增加备案号
====================

1. 在 ``templates/custom_theme`` 下新建html文件 ``footer.html`` ::

   <p>京备： xxxx </p>

2. 在 ``settings_local.py`` 中添加app与模板配置

  .. code-block:: python

      CUSTOM_APPS = [
          ...
          'custom_theme',
      ]

       BASE_THEME2_TEMPLATES={
           ...

           # key为模板名，value为html文件路径 （app名+html文件名）
           'body_footer_end_template':'custom_theme/footer.html'
       }


  .. note::

     v2.1把html分为不同模块，每个模块对应不同模板，方便对主题进行修改。
     所有页面对应的模块见 ： :ref:`templates`


添加静态文件
====================

想要在代码中引入新的css,js文件有两种方法：

1. 通过修改html引入

   新建html文件，并在 settings 的 BASE_THEME2_TEMPLATES 下添加 ``head_end_template`` ，指向新建的html文件。

2. 重写 static 方法

   在 ``custom_theme/admin.py`` 中添加下列代码 ::

        from base_theme2.theme import Theme
        from django.templatetags.static import static as static_url

        def _static(theme):
            static = theme._static()

            static.append_css('http://xx')
            static.append_js(['http://xxx', {'type': 'text/javascript', 'defer': True}])

            url = static_url('/custom_theme/my.css')
            static.add_css([
                url,
                ['http://xxx', {'media': 'all'}]
            ])

            return static

        Theme.static = _static

   * 使用 append_css，append_js 添加单个url； add_css，add_js 添加一组url。
   * url可以是字符串或者list。list的第一个参数为url地址，第二个参数是个字典，为标签的属性。

      如 ::

         ['http://xxx', {'type': 'text/javascript', 'defer': True}]

      对应的html代码是 ::

         <script defer type="text/javascript" src="http://xxx"></script>
   * 如果你的静态文件在本地，你需要用 ``static_url`` 函数获取真实 url


修改主题颜色、样式
====================
如果你只需要修改颜色、样式，更方便的方法是新建个新的 css 文件，修改对应的css类。

所有css见 ``base_theme2/static/base_theme2/css/base_theme2.css``

修改404页
==============

编写html，并在 ``BASE_THEME2_TEMPLATES`` 中添加 ``404_template``

下一步
===========

至此你已经学会了如何开发主题，接下来你需要了解如何在html中读取view传递的数据，以及每个页面对应的模板。

阅读 :ref:`context` 与 :ref:`templates` 。

