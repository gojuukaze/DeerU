.. _deployment:

==========
部署DeerU
==========

部署DeerU和部署Django项目一样，你可以自选查阅网上的Django部署文档。
这里提供一个部署方法。

部署一共有3步：

    * :ref:`deploying-settings` 

    * :ref:`部署静态、媒体文件<deploying-static>` 

    * :ref:`deploying-project` 

.. _deploying-settings:

修改settings
=================

把 ``derru/settings_local.py`` 中的 ``DEBUG`` 改为 ``False`` ，``ALLOWED_HOSTS`` 改为你的ip或域名

.. code-block:: python

    DEBUG = False
    ALLOWED_HOSTS = ['www.xxx.com','111.xx.xx.xx']


.. _deploying-static:

部署静态、媒体文件
=========================

django 非debug模式下并不会返回静态、媒体文件，你可以用下面两个方法部署他们文件：

1. 使用nginx/apache 代理，这里给出nginx的配置示例：

    .. code-block:: nginx

        location ~ ^/(static|media)/   {
            root /home/xxx/project/DeerU;
            # 静态文件返回需要增加跨域头，以便支持http访问https
            add_header Access-Control-Allow-Origin *;
            expires 864000;
        }

    .. note::

       如果你没修改过静态文件，媒体文件配置，

       则默认的静态文件url是 ``/static/`` ,保存在工程目录下的 ``static/`` 文件夹，

       默认的媒体文件url是 ``/media/`` ,保存在工程目录下的 ``media/`` 文件夹，

       关于静态文件，媒体文件配置参考Setting中的 :ref:`settings-static` , :ref:`settings-media`

2. 你也可以选择把静态、媒体文件上传到七牛或其他cdn服务商，然后修改 ``STATIC_URL`` , ``MEDIA_URL`` 为对应的url

    推荐有两个插件自动上传到七牛的插件：


    * deeru-qiniu :   |github-deeru-qiniu|

        .. |github-deeru-qiniu| image:: https://img.shields.io/badge/github--blue.svg?longCache=true&style=social
                        :target: https://github.com/gojuukaze/deeru-qiniu

    * django-qiniu-storage :   |github-django-qiniu-storage|   |doc-django-qiniu-storage| 
    
        .. |github-django-qiniu-storage| image:: https://img.shields.io/badge/github--blue.svg?longCache=true&style=social
                        :target: https://github.com/glasslion/django-qiniu-storage

        .. |doc-django-qiniu-storage| image:: https://img.shields.io/badge/doc--blue.svg?longCache=true&style=social
                        :target: http://django-qiniu-storage.readthedocs.io

.. note::

    什么是静态文件、媒体文件？  


    *静态文件* : 前端的js、css等文件  

    *媒体文件* : 你上传的图片、视频、音频文件  

.. _deploying-project:

部署项目
=========

你可以使用下面三种方法部署项目：

    * `Apache + mod_wsgi 部署 <https://docs.djangoproject.com/zh-hans/2.0/howto/deployment/wsgi/modwsgi/>`_

    * `Nginx + uWSGI 部署 <https://docs.djangoproject.com/zh-hans/2.0/howto/deployment/wsgi/uwsgi/>`_

    * `Gunicorn <https://docs.djangoproject.com/zh-hans/2.0/howto/deployment/wsgi/gunicorn/>`_

django官方推荐使用Apache + mod_wsgi的方式部署，因为个人喜好的原因这里介绍的是使用Gunicorn部署的方法，详见：:ref:`gunicorn-d`

