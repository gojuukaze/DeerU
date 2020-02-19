============
升级
============

你可以用升级命令进行升级，然后重启DeerU项目:: 
    
    # 建议升级前更新deeru命令主体
    pip install -U deeru
    deeru-admin upgrade

upgrade命令参考：:ref:`升级命令<cmd-upgrade>`

DeerU采用git仓库进行升级，因此改动源码可能导致升级失败，需要手动解决冲突。项目中 ``deeru/settings_local.py`` , ``deeru/urls_local.py`` 可以任意修改

1.0升级到2.0指南
======================

2.0版本对配置进行了可视化升级，所有需要而外多一些步骤。另外建议先把博客备份到本地，先在本地尝试升级，

1. 备份:: 

    # 备份工程
    cp -r deeru deeru.bk
    # 备份数据库，也可以使用数据库自带的备份命令
    cd deeru
    python manage.py dumpdata > ../deeru-v1bk.json

2. 升级:: 

    pip install -U deeru
    deeru-admin upgrade

3. 在 ``settings_local.py`` 中添加你自己的SECRET_KEY，可以使用命令 ``gen_secret_key`` 随机生成:: 

    python manage.py gen_secret_key

4. 同步数据库修改:: 

    python manage.py init_deeru

  这步最后会把v1配置升级到v2，如果v1的配置不符合规范或者其他原因有可能会失败。

  如果失败建议，把v1的配置回复到初始的状态再升级。或者也可以尝试修改 ``tool/version_upgrade/v1_config_to_v2.py`` 脚本
