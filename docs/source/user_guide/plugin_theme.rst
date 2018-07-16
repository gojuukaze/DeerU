.. _plugin-theme:

===================
插件与主题
===================

你可以用pip安装插件或主题:: 

    pip install xxx
    
你也可以直接下载源码，放置项目目录下。不过如果你选择这种方式，你需要把你下载的源码目录加到 ``.gitignore`` 防止DeerU升级失败。

通常你下载插件、主题后需要将他们家人到 ``deeru/settings_local.py`` 的 ``CUSTOM_APPS`` 中，具体参照他们的文档。

安装插件后别忘了重启DeerU。

从哪里找插件、主题？

    * https://github.com/gojuukaze/deeru_plugin_theme