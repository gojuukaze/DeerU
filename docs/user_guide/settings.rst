.. _settings:

================
Settings
================

下面只是列举了一些常见配置，以及DeerU的特殊配置，完整配置参考django文档 https://docs.djangoproject.com/en/2.2/ref/settings

DeerU所有的配置请在 ``deeru/settings_local.py`` 中添加或修改

数据库配置
-----------
    
    DeerU默认使用sqlite，如果你需要使用mysql，需要安装mysql连接库  `mysqlclient <https://pypi.org/project/mysqlclient/>`_  ，并在 ``settings_local.py`` 中添加
    
    .. code-block:: python 
    
        # settings_local.py
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.mysql',
                'OPTIONS': {
                   'charset': 'utf8mb4', # 使用mysql必须设置此项
                   'read_default_file': '/path/to/my.cnf',
                },
            }
        }
    
    
        # my.cnf 文件
        [client]
        host = 127.xx.xx.xx
        port = 3306
        database = NAME
        user = USER
        password = PASSWORD
    
    注意：如果你使用mysql，需要手动创建mysql database，并指定字符集为utf8mb4，否则无法初始化。
    
    如果你更改了数据库配置需要再次初始化项目
    
    其他说明以及数据库支持参考
    
    https://docs.djangoproject.com/en/2.2/ref/settings/#databases
    
    https://docs.djangoproject.com/en/3.0/ref/databases

    mac上旧版的mysql无法安装 ``mysqlclient`` ，需要修改 ``mysql_config`` ，具体参考：https://pypi.org/project/mysqlclient/1.4.5/

SECRET_KEY
---------------

    SECRET_KEY，v2版本开始需要在 ``settings_local.py`` 中配置（ 使用deeru-admin命令安装时会随机生成 ）

CACHES
-------------

    默认使用文件缓存，
    
    .. code-block:: python 
    
        CACHES = {
            'default': {
                'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
                'LOCATION': '/var/tmp/django_cache',
            }
        }
    
    你也可以使用内存、数据库、redis等作为缓存，参考 https://docs.djangoproject.com/zh-hans/2.0/ref/settings/#caches

FLATPAGE_URL
--------------

    默认: /p/
    
    单页面url前缀

ALLOWED_HOSTS
-------------
    
    默认: ['*']
    
    允许的hosts

DEBUG
----------------
    
    默认：True
    
    debug模式下会返回错误信息，不要在生产环境开启

CUSTOM_APPS
-------------------

    就是INSTALLED_APPS ，如果你添加了新的app，在 ``CUSTOM_APPS`` 中加入

CUSTOM_CONFIG_HANDLER
--------------------------

    v2配置的自定义handler，用于把配置进行二次处理。

    比如：配置图片时选择了图片id，配置保存时会经过handler处理，把图片id变为url。更多说明，参考:  :ref:`handler`

.. _settings-static:

STATIC_URL
-------------

    默认：/static/
    
    静态文件的url

STATIC_ROOT
--------------

    默认：工程目录下的 static 文件夹
    
    静态文件保存目录，如果你更改了这一项需要再次初始化项目，或者运行 ``python manage.py collectstatic`` 收集静态文件

.. _settings-media:

MEDIA_URL
-------------
    
    默认：/media/
    
    媒体文件的url

MEDIA_ROOT
--------------
    
    默认：工程目录下的 media 文件夹
    
    媒体文件保存目录

jet配置
-------------

    `jet <https://github.com/geex-arts/django-jet>`_ 是django的后台管理界面扩展
    
    相关配置有：
      * JET_DEFAULT_THEME : 主题
      * JET_INDEX_DASHBOARD : 仪表盘配置
    
    其他配置参考： http://jet.readthedocs.io/en/latest/

.. _DEERU-RICH-EDITOR:

DEERU_RICH_EDITOR
-----------------------

    默认:: 
    
        DEERU_RICH_EDITOR = {
            'filed': 'app.ex_fields.fields.MFroalaField',
            'article_kwargs': {
                ...
            },
            'flatpage_kwargs': {
                ...
            }
        }

    admin使用的富文本编辑器配置

        * filed : 富文本编辑器filed路径
        * article_kwargs : 文章filed的参数
        * flatpage_kwargs : 单页面filed的参数

froala编辑器配置
------------------

    DeerU后台富文本编辑器使用 `froala编辑器 <https://github.com/froala/django-froala-editor>`_
    
    相关配置有：
      * FROALA_EDITOR_PLUGINS : 插件
      * FROALA_EDITOR_OPTIONS : 编辑器默认选项，包括语言、上传目录等
    
    具体说明参考： https://github.com/froala/django-froala-editor

验证码
-------------
    评论的验证码，使用 `django-simple-captcha <https://django-simple-captcha.readthedocs.io/en/latest/>`_

    相关配置有：
      * CAPTCHA_CHALLENGE_FUNCT : 生成验证码的规则。默认使用自定义的算数验证码 ``tool.captcha.math_challenge``
      * CAPTCHA_FONT_PATH : 字体文件路径。默认使用精简的阿里字体。

        如果你修改了验证码的生成规则，需要注意默认字体中很可能不包含你的字符，你需要下载字体，并修改这项值。

        免费的字体，精简字体的方法你可以在这里找到： https://www.ikaze.cn/article/47

    其他说明参考： https://django-simple-captcha.readthedocs.io/en/latest/advanced.html#configuration-toggles


弃用配置
-------------

CUSTOM_EXPRESSION
^^^^^^^^^^^^^^^^^^^^^^^

    v1配置的自定义表达式