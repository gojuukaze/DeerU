==========
运行DeerU
==========


.. note::

    在这之前先确保你运行了初始化命令 ``python manage.py init_deeru`` ，并进入了工程目录.

debug模式运行
==============

* 在正式部署前，先用debug模式运行看看

.. code-block:: bash

    python manage.py runserver 0.0.0.0:8000

.. warning::

    ``python manage.py runserver`` 命令只能用于测试，不要在生成环境下使用这个命令部署项目

如果一切正常你可以打开浏览器访问 `http://127.0.0.1:8000 <http://127.0.0.1:8000>`_ ,正常情况下你将看到如下页面

.. image:: _static/home.png


正式部署
============

* 正式部署前先把 derru/settings_local.py 中的 ``DEBUG`` 改为 ``False`` ，``ALLOWED_HOSTS`` 改为你的ip或域名

.. code-block:: python

    DEBUG = False
    ALLOWED_HOSTS = ['www.xxx.com','xxx.com']

* 部署静态文件以及媒体文件

django 非debug模式下并不会返回静态文件，你可以用下面两个方法部署静态文件：

1. 用 nginx , apache 部署
   如：nginx 配置为

   .. code-block:: nginx

       location ~ ^/static/(.*)$ {
       alias  /home/username/DeerU/static/$1;
       # 静态文件返回需要增加跨域头，以便支持http访问https
       add_header Access-Control-Allow-Origin *;
       expires 864000;
       }

       location ~ ^/media/(.*)$ {
       alias  /home/username/DeerU/media/$1;
       # 静态文件返回需要增加跨域头，以便支持http访问https
       add_header Access-Control-Allow-Origin *;
       expires 864000;
       }
   .. note::

       如果你没修改过静态文件，媒体文件配置，

       则默认的静态文件url是 ``/static/`` ,保存在工程目录下的 ``static/`` 文件夹，

       默认的媒体文件url是 ``/media/`` ,保存在工程目录下的 ``media/`` 文件夹，

       关于静态文件，媒体文件配置参考Setting中的 STATIC, MEDIA


2. 把静态、媒体文件上传到七牛或其他cdn服务商，然后修改 ``STATIC_URL`` , ``MEDIA_URL`` 为对应的url（自动上传功能将在之后的版本加入）

* 部署工程

部署参考django的部署方法，dev版本暂不赘述

1. `Apache + mod_wsgi 部署 <https://docs.djangoproject.com/zh-hans/2.0/howto/deployment/wsgi/modwsgi/>`_

2. `uWSGI 部署 <https://docs.djangoproject.com/zh-hans/2.0/howto/deployment/wsgi/uwsgi/>`_

3. `其他 <https://docs.djangoproject.com/zh-hans/2.0/howto/deployment/>`_

