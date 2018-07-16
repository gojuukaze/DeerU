.. _custom-expression:

=================
自定义代码表达式
=================

DeerU只提供了几个简单的代码表达式，你可以根据需要自定义你的表达式，

另外：表达式的名字最终会转为小写，因此IMG和Img是重名的，为了防止重名，自定义的表达式建议以自己的名字开头

.. note::

    为了方便，以下所说的表达式特指代码表达式

-----------------

编写自定义表达式
-----------------


下面我们开始创建自定义表达式：

1. 新建一个python包，以及py文件，

.. code-block:: python

    my_ex/
        __init__.py
        custom_expression.py

2. 把你的py文件加入 ``settings_local.py`` 的 ``CUSTOM_EXPRESSION`` 中

.. code-block:: python

    CUSTOM_EXPRESSION=['my_ex.custom_expression']

3. 编写一个你的表达式类，继承 ``app.deeru_expression.expressions.BaseExpression``，并重写 ``calculate()``

函数 ``format_expression()`` 解析表达式时会把表达式分为 表达式名、参数 两部分，

这里再次强调以下，表达式名（也就是类名）最终会转为小写

参数 会放到类的成员变量 args 里

表达式名、参数 一定是用'|'分割开，如： ``{% text | some args %}``

参数部分没有限制，你可以仍然用'|'分割，也可自定义你的参数格式

``calculate()`` 的作用是解析参数，并返回需要的结果，它会在执行 ``get_result()`` 时调用。注意： ``calculate()`` 只会在第一次调用 ``get_result()`` 时执行，
后面将返回缓存的结果，因此同一个表达式实例不能重复使用


.. code-block:: python

    from app.deeru_expression.expressions import BaseExpression,get_attrs


    class MText(BaseExpression):
    """
    字符表达式
    {% text| 值 [ | 其他属性] %}

    返回{
        'text':'xx',
        'attrs':{
            'style':'xx'
        }
    }
    """

    def calculate(self):
        if not self.args:
            self.args = ''

        # 这里默认用'|'分割
        args = self.args.split('|')

        if len(args) == 0:
            raise ExpressionTypeError('表达式 text 至少需要一个参数')

        text = args[0]
        if len(args) > 1:
            attrs = get_attrs(args[1:])
        else:
            attrs = {}

        return {
            'text': text,
            'attrs': attrs
        }


至此你已经成功编写了一个表达式，载入表达式需要重启工程

.. note::

    函数 ``calculate()`` 并没有限制返回的数据类型，你可以返回字符串、字典或者html标签（在最早版本的表达式中，就是这样做的）

    不过建议返回字典或字符串，这样更利于主题开发者使用你的表达式返回结果