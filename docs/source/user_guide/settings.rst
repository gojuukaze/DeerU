.. _settings:

================
Settings
================

下面只是列举了一些常见配置，以及DeerU的特殊配置，完整配置参考django文档 https://docs.djangoproject.com/zh-hans/2.0/ref/settings/

DeerU所有的配置请在 ``deeru/settings_local.py`` 中添加或修改

数据库配置
-----------
    
    DeerU默认使用sqlite，如果你需要使用mysql，在 ``settings_local.py`` 中添加
    
    .. code-block:: python 
    
        # settings_local.py
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.mysql',
                'OPTIONS': {
                   'read_default_file': '/path/to/my.cnf',
                },
            }
        }
    
    
        # my.cnf
        [client]
        database = NAME
        user = USER
        password = PASSWORD
        default-character-set = utf8
    
    注意：如果你使用mysql，需要手动创建mysql database，django并不会帮你自动创建，
    
    如果你更改了数据库配置需要再次初始化项目
    
    其他说明以及数据库支持参考
    
    https://docs.djangoproject.com/zh-hans/2.0/ref/settings/#databases
    
    https://docs.djangoproject.com/zh-hans/2.0/ref/databases/

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

CUSTOM_EXPRESSION
-----------------------

    自定义表达式查找路径

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
    
