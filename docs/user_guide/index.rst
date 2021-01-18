=========================
使用指南
=========================


快速入门
=========
你阅读以下文档，帮你快速熟悉DeerU，部署你的博客

   * 第一步 ： 安装与运行

     - :ref:`installation` ： 安装deeru
     - :ref:`init-deeru` ： 配置并运行deeru

-----

   * 第二步 ： 发布文章与配置

      - 现在你可以登录后台管理页面（http://127.0.0.1:8000/admin）发布文章
      - :ref:`配置简介 <config-summary>` ： v2版对配置进行了可视化化改造，现在配置更简单，你可以在这里查看配置的说明


   现在你已经学会如何自定义你的博客了，接下来就把你的博客部署放到网上吧

------

   * 第三步 ： 部署

      - :ref:`deployment`  |  :ref:`gunicorn-d`： 参考这两篇部署项目，或者按你的喜好自行部署

-------

   * 其他

      - :ref:`settings` ： 项目的一些配置项，数据库默认使用sqlite如果你想改用mysql，参考里面的说明
      - :ref:`backup-restore` ：如果你需要备份博客，参考这篇文章
      - :ref:`import-wordpress`
      - :ref:`sitemap`
      - :ref:`rich-text-editor` ： 关于富文本编辑器的说明

|

.. toctree::
   :maxdepth: 3
   :caption: 目录

   getting_started
   configuration/index
   deployment/index
   settings
   backup_and_restore
   management_commands
   sitemap
   
   