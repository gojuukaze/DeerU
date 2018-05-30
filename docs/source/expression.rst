==========
表达式
==========


表达式可以帮你更快的配置界面，表达式分为：

全局变量表达式 `{{ }}` ，返回全局变量中的配置

代码表达式 `{% %}` ，返回一个字符串或html 标签 等 ，打吗表达式第一个参数以'|'分割

.. warning::
    代码表达式第一个参数是表达式名，一定是 小写

例子：

.. code-block:: python

    {{ title }} 返回title 的值

    {% fa|fas fa-home %} 返回svg图片的html 标签

    {% cat|name=默认分类|url%} 返回name=默认分类 的分类的url


解析表达式
------------

`tool.deeru_expression.manager` 定义了一个解析表达式的函数

`format_expression(value)`

  参数value是一个表达式字符串，否则将返回value

  全局变量表达式将返回全局变量值

  代码表达式将返回代码表达式的实例化对象，你需要调用 `get_result()` 获取解析结果


代码表达式
-------------
.. toctree::
   :maxdepth: 2

   built_in_expression
   custom_expression