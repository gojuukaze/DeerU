<h1 align="center">
 <a href="https://github.com/gojuukaze/DeerU" title="DeerU">DeerU</a>
</h1>
<p align="center">
  <a href="https://github.com/gojuukaze/DeerU" title="DeerU">
  <img alt="DeerU Logo" src="https://github.com/gojuukaze/DeerU/blob/master/logo_black.png?raw=true" width="180">
  </a>
</p>

[DeerU](https://github.com/gojuukaze/DeerU) is a content management system, used for blogs.

DeerU 是一个开源博客系统
___

目录
---

* 项目文档 ：[https://deeru.readthedocs.io](https://deeru.readthedocs.io)

开发进度
----

2018.05.28  --  第一个apha版完成  
2018.05.30  --  dev项目文档完成  
2018.06.04  --  单页面功能  
2018.06.19  --  重新设计了表达式  
2018.06.25  --  编写内置命令


安装
---

* 安装之前建议配置虚拟环境

``` bash

    pip install virtualenv
    virtualenv --no-site-packages deeru_env
    source deeru_env/bin/activate
```

* Linux/Mac OS 可以使用自动安装脚本安装

```bash

    wget https://raw.githubusercontent.com/gojuukaze/DeerU/dev/install.py -O - | python -
```

* 手动安装

```bash

    git clone -b dev https://github.com/gojuukaze/DeerU.git
    cd DeerU
    pip install -r requirements.txt
```

初始化
---


* 运行下面命令初始化项目，注意：如果你更改了数据库的配置，或者修改了主题的静态文件 则需要再次运行初始化

```bash

    cd DeerU # 如果你没进入工程目录先进入
    python manage.py init_deeru
```

运行
---

* 以debug模式运行
```bash

    python manage.py runserver 0.0.0.0:8000

```

从初始版本升级
-------
如果你在提交`fb8d0cd3da89c1`之前就已经使用了DeerU（即重新设计表达式之前的版本）

升级到最新版时老版的配置会无法正常解析。
你可以有两个方法解决：

1. 用`git pull origin` 拉取最新代码，然后进入后台管理，修改每个配置使其符合新的规则，并点保存（就算配置没有修改也要点保存）

2. 单独备份文章`python manage.py dumpdata app.article >back.json `，然后删除原来的数据库，拉取最新代码并运行初始化命令，
然后进后台管理修改配置，添加分类。运行`python manage.py loaddata back.json` 恢复文章

license
-------
DeerU使用 [GNU General Public License v3.0 协议](https://github.com/gojuukaze/DeerU/blob/master/LICENSE)
，你可以在遵循此协议的情况下免费使用DeerU

**重要！！**

> 需要注意的是，DeerU本身是免费的，但后台管理使用了富文本编辑器froala，其扩展插件并不免费，你可以在以下链接中查看收费信息：
> https://github.com/froala/django-froala-editor#license
> https://froala.com/wysiwyg-editor/pricing
>（ 我会在之后尝试更换其他富文本编辑器，不过这貌似有点困难，开发时试了好多编辑器，这个是最好用 ）


todo
----
* 提供单页面支持 [ok]
* 整理代码
* 优化表达式  [ok]
* 侧边栏扩展 (放弃，这个功能交给主题自由扩展)
* 尝试支持插件  [ok]
* 在支持插件的情况下支持主题扩展  [ok]
* 邮件通知回复
* 头像
* 尝试其他富文本编辑器
* 完善部署文档

截图
---
首页

<img alt="DeerU Logo" src="https://github.com/gojuukaze/DeerU/blob/dev/docs/source/_static/home.png?raw=true" width="80%">
文章详情

<img alt="DeerU Logo" src="https://github.com/gojuukaze/DeerU/blob/dev/docs/source/_static/detail.png?raw=true" width="80%">
admin
<img alt="DeerU Logo" src="https://github.com/gojuukaze/DeerU/blob/dev/docs/source/_static/admin.png?raw=true" width="80%">
admin2
<img alt="DeerU Logo" src="https://github.com/gojuukaze/DeerU/blob/dev/docs/source/_static/admin3.png?raw=true" width="80%">
手机1
<img alt="DeerU Logo" src="https://github.com/gojuukaze/DeerU/blob/dev/docs/source/_static/p1.png?raw=true" width="50%">
手机2
<img alt="DeerU Logo" src="https://github.com/gojuukaze/DeerU/blob/dev/docs/source/_static/p2.png?raw=true" width="50%">

