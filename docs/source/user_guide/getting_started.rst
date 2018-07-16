==========
运行DeerU
==========

安装完成后下面我们测试一下DeerU是否能正常运行

.. _init-deeru:

初始化
=========

1. 运行下面命令初始化项目，注意：如果你更改了数据库的配置，或者修改了主题的静态文件 则需要再次运行初始化

.. code-block:: bash

    cd DeerU # 如果你没进入工程目录先进入
    python manage.py init_deeru

2. 在 ``deeru/urls_local.py`` 中修改后台管理的url，
这一步可以跳过，但使用默认url会把你的登录界面暴露在网络中，造成一些安全隐患

.. code-block:: python

    urlpatterns = [
        path('admin123/', admin.site.urls),
    ]


.. _runserver-debug:

debug模式运行
=================

* 在正式部署前，先用debug模式运行看看

.. code-block:: bash

    python manage.py runserver 0.0.0.0:8000

.. warning::

    不要生产环境中使用 ``python manage.py runserver`` 运行项目，这是不安全的。  
    在生产环境中部署参考 :ref:`部署DeerU<deployment>`


如果一切正常你可以打开浏览器访问 `http://127.0.0.1:8000 <http://127.0.0.1:8000>`_ ,正常情况下你将看到如下页面。

如果你使用的是服务器ip访问，某些服务商默认的防火墙规则里可能不允许8000端口，你需要修改一下

.. image:: ../_static/home.png



