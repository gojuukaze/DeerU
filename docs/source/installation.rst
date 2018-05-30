============
安装
============

* 安装之前建议配置虚拟环境

.. code-block:: bash

    pip install virtualenv
    virtualenv --no-site-packages deeru_env
    source deeru_env/bin/activate

* Linux/Mac OS 可以使用自动安装脚本安装

.. code-block:: bash

    wget https://raw.githubusercontent.com/gojuukaze/DeerU/dev/install.py -O - | python -

* 手动安装

.. code-block:: bash

    git clone -b dev git@github.com:gojuukaze/DeerU.git
    cd DeerU
    pip install requirements.txt


初始化
=============

* 运行下面命令初始化项目，注意：如果你更改了数据库的配置，或者修改了主题的静态文件 则需要再次运行初始化

.. code-block:: bash

    cd DeerU # 如果你没进入工程目录先进入
    python manage.py init_deeru