====================
第三方模块开发
====================

DeerU为第三方开发者提供了一个 ``start`` 命令，用于快速生成Django app以及一些必要的文件，
这个命令也一样可以用于开发其他Django项目的app，不过在DeerU项目外运行这个命令你需要这样使用 ``deeru-admin start xxx``


下面将用一个敏感词屏蔽示例说明如何开发第三方模块，已经开发DeerU第三方模块的一些约定

1. 新建项目:: 

    deeru-admin install m_deeru

1. 运行start命令:: 
    
    python manage.py start plugin content_detection