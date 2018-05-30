===============
解析表达式
===============

``tool.deeru_expression.manager`` 定义了一个解析表达式的函数

**format_expression(value)**

  参数value是一个表达式字符串，否则将返回value

  全局变量表达式将返回全局变量值

  代码表达式将返回代码表达式的实例化对象，你需要调用 ``get_result()`` 获取解析结果

