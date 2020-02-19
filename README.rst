.. image:: https://github.com/gojuukaze/DeerU/blob/master/logo_black.png?raw=true
   :target: https://github.com/gojuukaze/DeerU
   :scale: 50%

`DeerU <https://github.com/gojuukaze/DeerU>`__ is a content management system, used for blogs.

DeerU 是一个开源博客系统


依赖
----

-  Python 3.6+ -- 安装教程 https://www.ikaze.cn/article/28
-  pip 10+
-  git
-  libjpeg，zlib -- pillow包的依赖

   -  ubuntu:
      ``apt-get install libjpeg8-dev zlib1g-dev libfreetype6-dev``
   -  centos:
      ``yum -y install python-devel zlib-devel libjpeg-turbo-devel``

目录
----

-  项目文档 ：\ https://deeru.readthedocs.io
-  `安装 <#安装>`__
-  `初始化 <#初始化>`__
-  `运行 <#运行>`__

安装
----

-  安装之前建议配置虚拟环境

.. code:: bash


        pip install virtualenv
        virtualenv --no-site-packages deeru_env
        source deeru_env/bin/activate

-  pip安装

.. code:: bash

        pip install DeerU
        deeru-admin install deeru

-  手动安装

.. code:: bash


        git clone -b dev https://github.com/gojuukaze/DeerU.git
        cd DeerU
        pip install -r requirements.txt

初始化
------

-  运行下面命令初始化项目，注意：如果你更改了数据库的配置，或者修改了主题的静态文件
   则需要再次运行初始化

.. code:: bash


        cd DeerU # 如果你没进入工程目录先进入
        python manage.py init_deeru

运行
----

-  以debug模式运行

.. code:: bash

        python manage.py runserver 0.0.0.0:8000

license
----------

DeerU使用 `GNU General Public License v3.0
协议 <https://github.com/gojuukaze/DeerU/blob/master/LICENSE>`__
，你可以在遵循此协议的情况下免费使用DeerU

.. note::

    需要注意的是，DeerU本身是免费的，但后台管理使用了富文本编辑器froala，其扩展插件并不免费，你可以在以下链接中查看收费信息：

    https://github.com/froala/django-froala-editor#license

    https://froala.com/wysiwyg-editor/pricing 
    
    （你可以自己更换其他编辑器，我也会在之后内置一些富文本编辑器的替代方案）

截图
----

首页

.. image:: https://github.com/gojuukaze/DeerU/blob/dev/docs/source/_static/home.png?raw=true
    :scale: 80%

.. image:: https://github.com/gojuukaze/DeerU/blob/dev/docs/source/_static/detail.png?raw=true
    :scale: 80%

.. image:: https://github.com/gojuukaze/DeerU/blob/dev/docs/source/_static/admin.png?raw=true
    :scale: 80%

.. image:: https://github.com/gojuukaze/DeerU/blob/dev/docs/source/_static/admin3.png?raw=true
    :scale: 80%

.. image:: https://github.com/gojuukaze/DeerU/blob/dev/docs/source/_static/p2.png?raw=true
    :scale: 50%
