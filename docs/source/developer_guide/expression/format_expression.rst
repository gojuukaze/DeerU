.. _format-expression:

===============
解析表达式
===============

``app.deeru_expression.manager`` 定义了一个解析表达式的函数


.. py:function:: format_expression(value)

    返回:
        全局变量表达式返回全局变量字符串，

        代码表达式返回对应的表达式对象

        非表达式返回value

    参数:
        value: 表达式字符串


    代码表达式返回的是代码表达式的实例化对象，需要在外部调用 ``get_result()`` 获取解析结果

