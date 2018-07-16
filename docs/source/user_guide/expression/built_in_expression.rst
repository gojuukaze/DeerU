===============
内置代码表达式
===============

你可以在 ``app/deeru_expression/expression.py`` 中找到内置代码表达式

img
-------------
.. py:class:: Img

    图片表达式，返回一个"type"为'img'的图片字典

    get_result():
        返回一个图片字典

        .. code-block:: python 

            {
                "type":'img',
                "src":'xxx',
                "attrs":{
                    "style":'xx',
                }
            }

    help:
        ``{% img| src/id/name = xx [|其他属性] %}``


        * src/id/name: **必须项** src或id或图片名，若为id,name将从上传的图片中查找

        * 其他属性: 可选，图片的属性

    例子:
        .. code-block:: python 

            {% img|src= xx %}

            {% img|id= 1 %}          --> 匹配 id

            {% img|name= xx %}          --> 匹配 name.startswith('xx')

            {% img|id=xx | style= height: 100px; width: 120px | alt= 图片 %}

fa
---------------
.. py:class:: Fa

    `fontawesome <https://fontawesome.com/icons?d=gallery&m=free>`_ 图标表达式，返回一个"type"为'fa'的图片字典，
    base_theme使用的是fontawesome5版本，你可以在其官网中获取需要的图片，其他主题使用的版本参照主题说明


    get_result():
        返回一个图片字典

        .. code-block:: python 

            {
                "type":'fa',
                "class_":'xxx',
                "attrs":{
                    "style":'xx',
                }
            }

    help:
        ``{% fa| xx [|其他属性] %}``


        * 第1个参数: **必须项** fontawesome图标<i>标签class的值, 如这个图标 `address-book <https://fontawesome.com/icons/address-book?style=solid>`_ 第二个参数就是 'fas fa-address-book'

        * 其他属性: 可选，其他属性

    例子:
        .. code-block:: python 

            {% fa|fas fa-address-book %}

            {% fa|fas fa-address-book | style=  color:red;font-size:16px; %}


svg
---------------
.. py:class:: Svg

    svg图片表达式，返回一个"type"为'svg'的图片字典

    get_result():
        返回一个图片字典

        .. code-block:: python 

            {
                "type":'fa',
                "svg":'xxx',
                "attrs":{
                    "style":'xx',
                }
            }

    help:
        ``{% svg| <svg>...</svg> [|其他属性] %}``


        * 第1个参数: **必须项** svg图片

        * 其他属性: 可选，其他属性

    例子:
        .. code-block:: python 

            {% svg| <svg width="100%" height="100%" version="1.1"xmlns="http://www.w3.org/2000/svg"><path d="M250 150 L150 350 L350 350 Z" /></svg> %}


cat
---------------
.. py:class:: Cat

    分类表达式，返回分类的url或名字

    get_result():
        根据第2个参数，返回url，或名字

    help:
        ``{% cat| id_or_name | 返回值 name/url %}``

        * id_or_name: *必须项* id或分类名，若不指定id还是name，优先匹配id

        * name/url: *必须项* 指定返回值

    例子:
        .. code-block:: python 

            {% cat| xx | name %} --> 匹配 id=xx 或 name.startswith(xx) 返回name
    
            {% cat| name = xx | name %} --> 匹配name.startswith(xx) 返回name
    
            {% cat| id = xx | url %} --> 匹配id=xx 返回url



tag
---------------
.. py:class:: Tag

    标签表达式，返回标签的url或名字

    get_result():
        根据第2个参数，返回url，或名字

    help:
        ``{% tag| id_or_name | 返回值 name/url %}``

        * id_or_name: *必须项* id或标签名，若不指定id还是name，优先匹配id

        * name/url: *必须项* 指定返回值

    例子:
        .. code-block:: python 

            {% tag| xx | name %} --> 匹配 id=xx 或 name.startswith(xx) 返回name

            {% tag| name = xx | name %} --> 匹配name.startswith(xx) 返回name

            {% tag| id = xx | url %} --> 匹配id=xx 返回url


text
---------------
.. py:class:: Text

    text表达式，返回text字典

    get_result():
        返回一个text字典

        .. code-block:: python 

            {
                "text":'xx',
                "attrs":{
                    "style":'xx',
                }

            }

    help:
       ``{% text| 值 [| 其他属性] %}``

        * 第一个参数: *必须项* text内容
        * 其他属性: 可选

    例子:
        .. code-block:: python 

            {% text| 1122 %}
    
            {% text| 1122 | style="color:red;" %}


