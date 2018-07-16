=========================
使用指南
=========================


快速入门
=========
你阅读以下文档，帮你快速熟悉DeerU，部署你的博客

   * 第一步 ： :ref:`installation`  | :ref:`init-deeru`  | :ref:`runserver-debug`

   完成了第一步，现在你可以先试试你的博客了，不过你可能会发现一些问题，为什么我的文章作者是gojuukaze? 如何修改博客标题？
   下面让我们开始第二步。

   * 第二步 ： :ref:`配置简介 <config-summary>` | :ref:`global-config` |  :ref:`ui-config` |  :ref:`配置的值类型 <config-type-img>`

      
      - 首先你应该先了解一下DeerU的 :ref:`配置简介 <config-summary>`  

      - 下面我们在 :ref:`global-config` 中修改作者名，博客名

      - 接下来我们来学习如何自定义界面 ： :ref:`ui-config`

      - 看了ui配置文档后你是不是很奇怪fa图片是什么？ 看看 :ref:`配置的值类型 <config-type-img>` 吧


   现在你已经学会如何自定义你的博客了，接下来就把你的博客部署放到网上吧

   * 第三步 ： :ref:`deployment`  |  :ref:`gunicorn-d`
   
      - 该如何部署DeerU呢？来，看这里 :ref:`deployment` 
      - 完成基本的设置，静态文件部署后，让我们用Gunicorn运行你的项目吧 ！:ref:`gunicorn-d` 。
        什么Oo0？你不想用Gunicorn！ 没关系，这一步你可以自由发挥


   * 其他 ：:ref:`expression` | :ref:`settings` | :ref:`backup-restore` | :ref:`import-wordpress` | 
           :ref:`plugin-theme` | :ref:`sitemap` | :ref:`rich-text-editor` | 

      - 是不是觉得配置要写很多东西，很麻烦。那就用 :ref:`expression` 简化一下你的配置吧！
      - 默认的sqlite拖累了你的性能，想改用mysql？当然没问题，看看 :ref:`settings` 
      - 担心数据丢失，那就来备份一下吧 :ref:`backup-restore` 
      - 你以前使用的是wordpress？那还不快换成DeerU! :ref:`import-wordpress` 
      - 没有你想要的功能？去插件里找找看 :ref:`plugin-theme` 
      - 差点吧这个小东西忘了0.0 :ref:`sitemap`
      - 关于富文本编辑器 :ref:`rich-text-editor`

|

.. toctree::
   :maxdepth: 4
   :caption: 网站目录:

   getting_started
   configuration/index
   expression/index
   deployment/index
   deployment/gunicorn
   settings
   backup_and_restore
   management_commands
   sitemap
   
   