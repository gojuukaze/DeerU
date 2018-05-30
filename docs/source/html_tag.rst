================
HtmlTag
================

DeerU内置了一个html标签类，用于构建html标签


**class Tag(object):**

* __init__(name, text='', attrs=None)

  + `name` : 标签名
  + `text` : 标签的text
  + `attrs` : 标签属性，字典，如： `{'class':'icon', 'style':'color:red;'}`

* append(tag)

  添加子标签

* set_attr(name, value)

  设置属性

* append_attrs_value(name, value)

  追加属性

* format_html()

  返回html标签的文本代码