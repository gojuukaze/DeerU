<h1 align="center">
 <a href="https://github.com/gojuukaze/DeerU" title="DeerU">DeerU</a>
</h1>
<p align="center">
  <a href="https://github.com/gojuukaze/DeerU" title="DeerU">
  <img alt="DeerU Logo" src="https://github.com/gojuukaze/DeerU/blob/master/logo_black.png?raw=true" width="180">
  </a>
</p>
<p align="center">
  <a title="快速开始" href="http://deeru.readthedocs.io/zh_CN/master/user_guide/index.html"><strong>快速开始</strong></a>
  &#x2022;
  <a title="文档" href="http://deeru.readthedocs.io"><strong>文档</strong></a>
  &#x2022;
  <a title="插件与主题" href="https://github.com/gojuukaze/deeru_plugin_theme"><strong>插件与主题</strong></a>
  &#x2022;
  <a title="贡献代码" href="http://deeru.readthedocs.io/zh_CN/master/developer_guide/contributing.html"><strong>贡献代码</strong></a>
</p>

<p align="center">
  <a href="" title="version">
    <img src="https://img.shields.io/badge/version-v1.0.0-blue.svg" alt="version - v1.0.0">
  </a>

  <a href="https://github.com/gojuukaze/DeerU/blob/master/LICENSE" title="LICENSE">
    <img src="https://img.shields.io/badge/license-GPL%20V3-blue.svg" alt="license - GPL V3">
  </a>
</p>


[DeerU](https://github.com/gojuukaze/DeerU) is a content management system, used for blogs.

DeerU 是一个开源博客系统，它基于Django开发。  

它提供了丰富的json数据接口，前端开发人员可以不依赖Django模板，方便的开发主题，实现前后端分离。
___

依赖
---
* Python 3.5+ -- 安装教程 https://www.ikaze.cn/article/28
* pip 10+
* git
* libjpeg，zlib -- pillow包的依赖 
    - ubuntu: ``apt-get install libjpeg8-dev zlib1g-dev libfreetype6-dev`` 
    - centos: ``yum -y install python-devel zlib-devel libjpeg-turbo-devel`` 



目录
---

* 项目文档 ：[https://deeru.readthedocs.io](https://deeru.readthedocs.io)
* 插件与主题 ：[https://github.com/gojuukaze/deeru_plugin_theme](https://github.com/gojuukaze/deeru_plugin_theme)
* GITHUB ：[https://github.com/gojuukaze/DeerU](https://github.com/gojuukaze/DeerU)
* [安装](#安装)
* [初始化](#初始化)
* [运行](#运行)

安装
---

* 安装之前建议配置虚拟环境

``` bash

    pip install virtualenv
    virtualenv --no-site-packages deeru_env
    source deeru_env/bin/activate
```

* pip安装

```bash
    pip install DeerU
    deeru-admin install deeru

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

license
-------
DeerU使用 [GNU General Public License v3.0 协议](https://github.com/gojuukaze/DeerU/blob/master/LICENSE)
，你可以在遵循此协议的情况下免费使用DeerU

**重要！！**

> 需要注意的是，DeerU本身是免费的，但后台管理使用了富文本编辑器froala，其扩展插件并不免费，你可以在以下链接中查看收费信息：  
>
> https://github.com/froala/django-froala-editor#license  
>
> https://froala.com/wysiwyg-editor/pricing  
>
>（ 你可以自己更换其他编辑器，我也会在之后内置一些富文本编辑器的替代方案 ）


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

