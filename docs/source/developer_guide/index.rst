====================
开发指南
====================

给开发者的开发指南
=================

* 一些约定

    开发代码时请遵从以下约定 :ref:`role`

* model说明 
    
    :ref:`model`

* 代码表达式开发

    代码表达式用于把配置中的字符串解析为dict，str等，主要用于主题的界面配置中

        - :ref:`format-expression`

        - :ref:`custom-expression`

* 第三方模块开发

    开发DeerU的第三方模块和开发Django app没什么区别，不过DeerU对一些地方进行了规范

        - 基础： :ref:`概述<third-party-index>` 
        - 开发插件： :ref:`plugin` 
        - 开发主题： :ref:`theme` | :ref:`context` | :ref:`model` | :ref:`url-view`
            + 开发主题你首先要了解一下基本的东西 :ref:`theme`
            + 然后你需要知道 context 的结构 :ref:`context` ，context中model的方法 :ref:`model`
            + 然后每个view里都返回了什么 :ref:`url-view`
        - 提交插件、主题到DeerU的项目中： :ref:`提交插件、主题 <upload-plugin-theme>` 


.. toctree::
    :maxdepth: 5
    :caption: 目录:
    
    role
    model/index
    expression/index
    third_party/index
    context
    url_view
    contributing
    