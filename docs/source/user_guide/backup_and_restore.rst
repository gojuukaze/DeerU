.. _backup-restore:

=============
备份和恢复
=============

备份deeru你只需要备份数据库， ``deeru/settings_local.py`` , ``deeru/urls_local.py`` 以及上传的媒体文件

你可以使用django内置命令备份、恢复数据库

* 备份命令：
.. code-block:: bash

    python manage.py dumpdata >mybk.json

* 恢复命令：
.. code-block:: bash

    python manage.py loaddata  mybk.json

