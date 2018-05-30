=============
ui配置
=============

DeerU把界面分为5大块，如图

.. image:: _static/ui_config.png


目前可配置的只有 顶部导航栏，顶部图标栏

顶部导航栏
-----------

顶部图标栏 的配置是一个数组，每部分是一个字典，它的结构如下

.. code-block:: python

    [
        {
            "name" : "首页",
            "url" : "/",
            "img": {
                        "src" : "/media/xx.png",
                        "width" : "36px",
                        "height" : "36px",
                        "alt" : "首页"
                   }
        },

        {
            "name" : "首页2",
            "url" : "/",
            "img": {
                        "src" : "/media/xx.png",
                        "width" : "36px",
                        "height" : "36px",
                        "alt" : "首页"
                   }

            "children" : [
                            {
                                "name":'xx',
                                ...
                            },
                            {
                                "line":'line',
                            },
                            {
                                "name":'xx',
                                ...
                            }
                         ]
        },
    ]


其中：

- name : 显示的名字 `【支持全局变量表达式 ， 返回字符串的代码表达式】`

- url  : 跳转链接  `【支持全局变量表达式 ， 返回字符串的代码表达式】`

- img  : 图片，是一个字典，里面支持的选项有 src，width，height，alt  `【支持代码表达式： img、fa】`

- children : 子目录 （children中不再支持children）`【不支持表达式】`

- line : 分割线，只有在children才支持 `【不支持表达式】`

.. note::

    如果你看了初始化的配置文件会发现其中有一些特殊的表达式，

    比如这个 `{% fa|fas fa-home %}` 表达式将返回生成一个svg图片的html 标签，

    表达式分为 全局变量表达式 `{{}}` 和 代码表达式 `{% %}`

    全局变量表达式返回全局变量中配置的值，代码表达式返回一个字符串或html 标签 等

    不是所有配置都支持表达式

    表达式的使用你可以在表达式章节中查看


顶部图标栏
------------

顶部图标栏分为左右两块，结构如下

.. code-block:: python

    {

    "left": {
        "logo": "{%img|logo_white %}",
        "blog_name": "{%text| 文字标题 | style=font-size:18px %}"
    },

    "right": [
        {
            "img": "{%fa|svg= fab fa-github|style=color:#ffffff;font-size:24px %}",
            "url": "https://github.com/gojuukaze/DeerU"
        }
    ]

    }

- left : 左边部分 logo 和 blog_name 都不是必须的，不需要可以为空 `【不支持表达式】`

 + logo : logo在最左边显示， 配置参照上面的img 配置 `【支持代码表达式： img、fa】`

 +  blog_name : 在log右边 `【支持全局变量表达式 ， 返回字符串的代码表达式 ， 以及代码表达式: text】`

- right : 右边部分，是一个数组 `【不支持表达式】`

 + img : 参照前面的img `【支持代码表达式： img、fa】`

 + url : url `【支持全局变量表达式 ， 返回字符串的代码表达式】`