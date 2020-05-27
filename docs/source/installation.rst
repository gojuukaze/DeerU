.. _installation:

============
安装
============

安装前先确保你已经安装了以下程序：

* Python 3.6+
* pip 10+
* git
* libjpeg，zlib -- pillow包的依赖

    - ubuntu: ``apt-get install libjpeg8-dev zlib1g-dev libfreetype6-dev`` 
    - centos: ``yum -y install python-devel zlib-devel libjpeg-turbo-devel`` 



另外安装之前建议配置虚拟环境

.. code-block:: bash

    python3 -m venv deeru_env
    source deeru_env/bin/activate
    # in windows, run this:
    # deeru_env/Scripts/activate

使用pip安装
-----------

.. code-block:: bash

    pip install deeru
    deeru-admin install DeerU

从git仓库安装(不推荐)
---------------------------

.. code-block:: bash

    git clone https://github.com/gojuukaze/DeerU.git
    cd DeerU
    pip install -r requirements.txt

从git安装需要手动创建两个文件：

* ``deeru/urls_local.py`` ，内容如下:

.. code-block:: python 

    from django.contrib import admin
    from django.urls import path, include

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('app.urls')),
    ]

* ``deeru/settings_local.py`` ，内容如下:

.. code-block:: python 

    # v2版本开始需要配置
    SECRET_KEY = 'xxx'
    
    DEBUG = True
    
    ALLOWED_HOSTS = ['*']
    
    CUSTOM_EXPRESSION = []
    
    CUSTOM_APPS = []
    
    CUSTOM_CONFIG_HANDLER = []

v2版本需要设置你自己的 ``SECRET_KEY`` ，可以使用命令 ``python manage.py gen_secret_key`` 生成
