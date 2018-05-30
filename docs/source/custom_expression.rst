==============
自定义代码表达式
==============

DeerU只提供了几个简单的代码表达式，你可以根据需要自定义你的表达式，

不过对于返回html标签的表达式，需要注意你使用的主题不一定支持你自定义的返回值，

另外：表达式的名字最终会转为小写，因此IMG和Img是重名的，为了防止重名，自定义的表达式建议以自己的名字开头

.. note::

    为了方便，以下所说的表达式特指代码表达式

------------

编写自定义表达式
------------


下面我们开始创建自定义表达式：

1. 新建一个python包，以及py文件，

.. code-block:: python

    my_ex/
        __init__.py
        custom_expression.py

2. 把你的py文件加入 ``settings_local.py`` 的 ``CUSTOM_EXPRESSION`` 中

.. code-block:: python

    CUSTOM_EXPRESSION=['my_ex.custom_expression']

3. 编写一个你的表达式类，继承 ``tool.deeru_expression.expressions.BaseExpression``，并重写 ``calculate()``

函数 ``format_expression()`` 解析表达式时会把表达式分为 表达式名、参数 两部分，

这里再次强调以下，表达式名（也就是类名）最终会转为小写

参数 会放到类的成员变量 args 里

表达式名、参数 一定是用'|'分割开，如： ``{% ptext | some args %}``

参数部分没有限制，你可以仍然用'|'分割，也可自定义你的参数格式

``calculate()`` 的作用是解析参数，并返回需要的结果，它会在执行 ``get_result()``时调用。注意： ``calculate()`` 只会在第一次调用 `get_result()` 时执行，
后面将返回缓存的结果，因此同一个表达式实例不能重复使用


.. code-block:: python

    from tool.deeru_expression.expressions import BaseExpression
    from tool.deeru_html import Tag as HtmlTag


    class PText(BaseExpression):
    """
    分类表达式
    {% ptext| 值 | [style] %}

    返回<p>xxx</p>
    """

    def calculate(self):
        if not self.args:
            self.args = ''

        # 这里默认用'|'分割
        args = self.args.split('|')

        attrs = {}

        if len(args) == 2:
            k, v = args[1].split('=')
            k=k.strip()

            if k != 'style':
                raise ExpressionTypeError('表达式 text 可选项只支持style')
            attrs['style'] = v

        return HtmlTag('p', text=args[0], attrs=attrs)


至此你已经成功编写了一个表达式，载入表达式需要重启工程

在这里用来一个新的东西 ``tool.deeru_html.Tag`` 这是DeerU内置的html标签类，关于它的使用你可以在对应章节里找到
