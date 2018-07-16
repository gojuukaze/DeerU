.. _ui-config:

=============
ui配置
=============

DeerU把界面分为5大块，如图

.. image:: ../../_static/ui_config.png


DeerU为 **顶部导航栏** 、**顶部图标栏** 这两部分提供了一种通用的配置方式，不过并不强制要求主题一定要使用这两个配置。
有的主题可能会有自己的配置

顶部导航栏
-----------

``顶部导航栏`` 的配置是一个list，每部分是一个dict，它的结构如下

    .. code-block:: python

        [
            {
                'url': '/',
                'name': '首页',
                'img': {
                    'type': 'fa',
                    'class': 'fas fa-home ',
                    'attrs': {}
                }
            }, 
            {
                'name': '折叠菜单',
                'img': {
                    'type': 'fa',
                    'class': 'fas fa-list ',
                    'attrs': {}
                },
                'children': [
                    {
                        'name': '默认分类',
                        'url': '/category/1'
                    }, 
                    
                    {
                        'line': 'line'
                    },
                    {
                        'name': 'DeerU',
                        'url': '/tag/1'
                    }
                ]
            }
        ]

    list中item的结构：

        从上面的例子中可以看出item一共有两种结构  

        第一种结构:

            - name ( str | 必须项 ) : 显示的名字

            - url  ( str | 必须项 ) : 跳转链接  

            - img  ( dict )      : 图片，值是一种特殊的图片类型，默认的图片类型有3种type，详细在 :ref:`config-type-img` 中查看

            - children ( list )  : 子目录 ，（子目录中可以包含子目录，但你使用的主题不一定支持）
        
        第二种结构:

            - line         : 分割线，只能在children中


顶部图标栏
------------

顶部图标栏分为左右两块，结构如下

.. code-block:: python

    {
        'left': {
            'logo': {
                'type': 'img',
                'src': '/media/logo_white.png',
                'attrs': {}
            },
            'blog_name': {
                'text': ' 文字标题 ',
                'attrs': {
                    'style': 'font-size:18px'
                }
            }
        },
        
        'right': [
            {
                'url': 'https://github.com/gojuukaze/DeerU',
                
                'img': {
                    'type': 'fa',
                    'class': 'fab fa-github',
                    'attrs': {
                        'style': 'color:#ffffff;font-size:24px'
                    }
                } 
            },
        ]
    }

|

    - left ( dict | 必须项 ) : 
        
        左边部分，内容可为空，其结构为:
        
        + logo ( dict )       :   logo图片，值是为图片类型
        + blog_name ( dict )  :   文本标题，值是为文本类型，文本类型说明见 :ref:`config-type-text`

    - right ( list | 必须项 ) : 

        右边部分，内容可为空，每个item是一个dict，结构为:

            + img ( dict ) : 参照前面的img 

            + url ( str )  : url


.. note::

    如果你看了初始化的配置会发现其中有一些特殊的表达式，  

    比如这个 ``{% fa|fas fa-home %}`` 表达式将返回生成一个type为fa的图片，    

    表达式分为 全局变量表达式 ``{{}}`` 和 代码表达式 ``{% %}``  

    全局变量表达式返回全局变量中配置的值，代码表达式返回str或dict 等  

    所有的配置项都可以替换为表达式，不过值为str的只能用返回str的表达式替换

    表达式的使用你可以在表达式章节中查看: :ref:`expression`  