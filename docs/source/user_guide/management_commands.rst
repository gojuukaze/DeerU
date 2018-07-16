==========
内置命令
==========

所有内置命令放在 ``app/management/commands`` , ``deeru_cmd/management/commands `` 下

安装
--------
.. py:data:: install

    下载DeerU:: 

        deeru-admin install name [--branch master]

    name:
        项目的文件夹名称

    branch:
        从哪个分支下载，默认master

.. _cmd-upgrade:

升级
-----------
.. py:data:: upgrade

    升级DeerU:: 

        python manage.py upgrade
    
    DeerU使用的是git进行升级，因此改动源码可能会导致升级失败。如改动了源码你需要手动运行 ``git pull origin master`` 升级，并解决冲突。  

    另外升级后你需要手动重启DeerU

创建第三方模块
---------------
.. py:data:: start

    升级DeerU:: 

        python manage.py start type name
    
    给开发者用的命令，创建DeerU的第三方主题或插件，使用这个命令会自动生成 ``setup.py`` , ``README.md`` , ``.gitignore`` 等必要的文件，方便开发

    type:
        类型，可选项 theme、plugin

    name:
        第三方模块名

初始化
-------------------
.. py:data:: init_deeru

    初始化DeerU:: 

        python manage.py init_deeru

    初始化数据库，收集静态文件

.. _import-wordpress:

从wordprees导入
----------------------------------
.. py:data:: import_wordpress

    从wordprees的xml文件导入:: 

        python manage.py import_wordpress xml_path [--mode (a|c|t)] [--nwp ] [--ncontent] [--cover (y|n|ask)]


    xml_path:
        xml文件路径

    mode:
        导入的内容，默认:a

        * a : 文章、评论、分类、标签

        * c : 分类

        * t : 标签

    nwp:
        xml文件中 命名空间wp的内容，默认: ``{http://wordpress.org/export/1.2/}`` 

    ncontent:
        xml文件中 命名空间content的内容，默认: ``{http://purl.org/rss/1.0/modules/content/}`` 

    cover:
        是否使用xml文件中的内容覆盖数据库中的内容，默认:ask

        * y : 是

        * n : 否

        * ask : 询问我

    .. note::
        
        1.评论暂不支持审核，所有不会导入未审核的评论，如果需要去掉get_comment()中对应的部分  

        2.wordprees的日期格式必须为： 2018-05-02 15:23:22  

        3.对评论的回复会自动在内容前添加 "回复 xx："，如果不需要去掉save_comment()中对应部分  

        4.不会导入草稿  

备份数据库
------------
.. py:data:: dumpdata

    django自带的备份命令:: 

        python manage.py dumpdata >mybk.json



恢复数据库
------------
.. py:data:: loaddata

    django自带的恢复命令:: 

        python manage.py loaddata  mybk.json


