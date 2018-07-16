.. _expression:

==========
表达式
==========


表达式可以帮你更快的配置界面，表达式分为：

全局变量表达式 ``{{ }}`` ，返回全局变量中的配置

代码表达式 ``{% %}`` ，返回一个字符串或字典 等，代码表达式第一个参数以'|'分割

.. warning:: 

    代码表达式第一个参数是表达式名，一定是 **小写**

例子：

.. code-block:: python

    {{ title }} 返回全局变量中title 的值

    {% fa|fas fa-home %} 返回type为fa的图片

    {% cat|name=默认分类|url%} 返回name=默认分类 的分类的url






.. toctree::
   :maxdepth: 4
   :caption: 表达式相关:

   built_in_expression
