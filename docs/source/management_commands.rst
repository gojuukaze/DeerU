==========
相关命令
==========

初始化 - init_deeru
-------------------

`python manage.py init_deeru`

初始化数据库，收集静态文件

从wordprees导入 - import_wordpress
----------------------------------

`python manage.py import_wordpress xml_path`

你可以用这个命令从wordprees的xml文件导入内容

Arguments
~~~~~~~~~

  xml_path : 从wordprees导出的xml文件路径
  --model : default:a; 想要导入的内容 ( a:article+comment+category+tag, c:category, t:tag )
  --cover : default:ask; 是否用xml文件的内容覆盖数据库中的相同内容（ y: 覆盖; n: 不覆盖; ask:询问我 ）

备份数据库
------------

`python manage.py dumpdata >mybk.json`

你可以用Django的dumpdata命令备份数据库


恢复数据库
------------

`python manage.py loaddata  mybk.json`

你可以用Django的loaddata命令恢复数据库

