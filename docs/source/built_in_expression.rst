===============
内置代码表达式
===============

你可以在 `tool/deeru_expression/expression.py` 中找到内置代码表达式


img
---------------

* 返回html 标签

图片表达式，从上传的图片中获取图片，

第二个参数： id或图片名，也可指定匹配id还是name
第三个参数： 可选，只支持style , 你可以指定返回图片标签的style

例子：

.. code-block:: python

    {% img|id_or_name %}     --> 匹配顺序 id>name

    {% img|id= 1 %}          --> 匹配 id

    {% img|name= xx %}          --> 匹配 name.startswith('xx')

    {% img|id=xx | style= xx %}  --> 你可以指定返回图片标签的style


fa
---------------

* 返回html 标签

svg表达式，返回的svg图片，deeru采用 `fontawesome5 <https://fontawesome.com/icons?d=gallery&m=free>`_ 提供的图片，你可以在其官网中获取需要的图片

第二个参数：fontawesome5图标<i>标签class的值， 如这个图标 `address-book <https://fontawesome.com/icons/address-book?style=solid>`_ 第二个参数就是 'fas fa-address-book'

第三个参数：可选，只支持style ，如果有第三个参数，第二个参数必须有'svg='

例子：

.. code-block:: python

    {% fa|fas xx %}

    {% fa|svg= fas xx|style=  color:red;font-size:16px; %}


cat
---------------

* 返回字符串

分类表达式，返回分类的name/url

第二个参数：id或分类名，也可指定匹配id还是name

第三个参数：必填，指定返回值

例子：

.. code-block:: python

    {% cat| 值 | 返回值(name/url) %}

    {% cat| xx | name %} --> 匹配：id=xx 或 name.startswith(xx) 返回name
    
    {% cat| name = xx | name %} --> 匹配name.startswith(xx) 返回name
    
    {% cat| id = xx | url %} --> 匹配id=xx 返回url


tag
---------------

* 返回字符串

标签表达式，返回分类的name/url

第二个参数：id或标签名，也可指定匹配id还是name

第三个参数：必填，指定返回值

例子：

.. code-block:: python

    {% tag| 值 | 返回值(name/url) %}

    {% tag| xx | name %} --> 匹配：id=xx 或 name.startswith(xx) 返回name
    
    {% tag| name = xx | name %} --> 匹配name.startswith(xx) 返回name
    
    {% tag| id = xx | url %} --> 匹配id=xx 返回url


text
---------------

* 返回html 标签

字符表达式，返回 <sapn></span>

第二个参数：字符值

第三个参数：可选，只支持style

例子：

.. code-block:: python

    {% text| 值 | [style] %}

    {% text| 1122 %} --> 返回：<span>1122</span>
    
    {% text| 1122 | style="color:red;" %} -->  返回：<span style="color:red;">1122</span>


