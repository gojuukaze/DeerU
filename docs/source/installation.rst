.. _installation:

============
安装
============

安装前先确保你已经安装了以下程序：

* Python 3.5+ -- 安装教程 https://www.ikaze.cn/article/28
* pip 10+
* git
* libjpeg，zlib -- pillow包的依赖 
    - ubuntu: ``apt-get install libjpeg8-dev zlib1g-dev libfreetype6-dev`` 
    - centos: ``yum -y install python-devel zlib-devel libjpeg-turbo-devel`` 



另外安装之前建议配置虚拟环境

.. code-block:: bash

    pip3 install virtualenv
    virtualenv --no-site-packages deeru_env
    source deeru_env/bin/activate
    # in windows, run this:
    # deeru_env/Scripts/activate

使用pip安装
-----------

.. code-block:: bash

    pip install deeru

从git仓库安装
-------------

.. code-block:: bash

    git clone -b dev https://github.com/gojuukaze/DeerU.git
    cd DeerU
    pip install -r requirements.txt

手动创建 ``deeru/urls_local.py`` 文件，内容如下:

.. code-block:: python

    from django.contrib import admin
    from django.urls import path, include

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('app.urls')),
    ]

手动创建 ``deeru/settings_local.py`` 文件，内容如下:

.. code-block:: python

    DEBUG = True

    ALLOWED_HOSTS = ['*']

    CUSTOM_EXPRESSION = []

    CUSTOM_APPS = [

    ]

