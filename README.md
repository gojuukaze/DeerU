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


* 项目文档 ：[deeru.readthedocs.io](https://deeru.readthedocs.io)

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

    git clone -b dev git@github.com:gojuukaze/DeerU.git
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

