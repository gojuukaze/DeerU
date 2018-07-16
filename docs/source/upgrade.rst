============
升级
============

你可以用升级命令进行升级，然后重启DeerU项目:: 

    python manage.py upgrade

upgrade命令参考: :ref:`升级命令<cmd-upgrade>`

DeerU采用git仓库进行升级，因此改动源码可能导致升级失败，项目中 ``deeru/settings_local.py`` , ``deeru/urls_local.py`` 可以任意修改