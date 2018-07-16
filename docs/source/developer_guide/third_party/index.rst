.. _third-party-index:

====================
第三方模块开发
====================

DeerU为第三方开发者提供了一个 ``start`` 命令，用于快速生成Django app以及一些必要的文件，
这个命令也一样可以用于开发其他Django项目的app，不过在DeerU项目外运行这个命令你需要这样使用 ``deeru-admin start xxx``


下面将用一个示例说明开发第三方模块的基本流程

1. 新建项目:: 

    deeru-admin install m_deeru

2. 运行start命令 

    :: 

        python manage.py start plugin content_detection


    如果一切正常，那么你会看到下面的目录结构(这里只选取了重要的文件):: 

        m_deeru/
            content_detection/
                apps.py
                consts.py
                ...

            content_detection_setup.py
            README.rst
            MANIFEST.in
            git_add.sh

    
    .. py:data:: content_detection/apps.py

        在apps.py的中 ``AppConfig`` 中你可以看到一些专属的变量
        
            deeru_config_context: 
                config_context的路径

    .. py:data:: content_detection/consts.py

        在consts.py的中有一个dict ``content_detection_config_context`` ， 这个只有主题开发才用得到。
        在这个dict中的配置，会在访问页面时从数据库读取放入context中传给前端，

        这个dict的key为context中的名字，value为数据库中保存的名字，如::
        
            {
                'top_ico2' : '顶部图标栏2'
            }
        
        在 admin - 配置 - 新建 名为"顶部图标栏2" 的配置，此配置放入context中时名字为"top_ico2" 

    .. py:data:: content_detection_setup.py

        此命令自动生成了打包的setup.py文件，你需要填写里面空的地方

    .. py:data:: git_add.sh

        如果不想把DeerU的代码一同上传到git仓库，可以查看里面的add示例。

3. 编写你的代码

4. 打包发布:: 

    python content_detection_setup.py sdist bdist_wheel 
    
    twine upload dist/*

.. _upload-plugin-theme: 


5. 提交到DeerU插件、主题列表里

    fork项目 https://github.com/gojuukaze/deeru_plugin_theme 把你的插件、主题加到py、readme 中，提交 合并请求

.. toctree::
    :maxdepth: 5
    :caption: 其他:
    
    plugin
    theme
    
   