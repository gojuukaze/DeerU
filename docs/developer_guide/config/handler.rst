.. _handler:

=================
配置handler
=================

有时候还需要对保存的配置进行进一步处理，以获得最终需要的配置，因此引入了handler的概念。

保存配置时会把 ``v2_config`` 中的类型为dict且含有 ``_handler`` 这个key的那部分，经过handler处理后整个替换掉。  
如果存在多层嵌套，会先处理最里层的数据。  

如：

.. code-block:: python 

   {
      "url":{
          "_handler":"v2_url_handler",
          "type":"tag",
          "value":"1"
      }
   }

经v2_url_handler处理后，变成：

.. code-block:: json 

   // 注意这里替换的是与"_handler"同级的整个结构
   {
      "url" : "/tag/1"
   }


自带handler
------------------

自带了3个handler，分别是 :

* v2_url_handler ：返回分类、标签的url
* v2_img_handler : 返回生成图片标签所以的结构
* v2_kv_handler : 把数组的k-v结构解析为字典结构

自定义handler
-----------------

1. 新建一个python包，以及py文件，

.. code-block:: python

    my_ex/
        __init__.py
        custom_handler.py

2. 把你的py文件加入 ``settings_local.py`` 的 ``CUSTOM_CONFIG_HANDLER`` 中

.. code-block:: python

    CUSTOM_CONFIG_HANDLER=['my_ex.custom_handler']

3. 编写一个你的handler类，继承 ``app.deeru_config_handler.base.BaseHandler``，并重写 ``calculate()``

   装饰器 ``deeru_config_handler()`` 用于定义handler的名字，防止冲突建议格式为：``你的名字:handler名字``


.. code-block:: python

    from app.deeru_config_handler.base import BaseHandler, deeru_config_handler

    @deeru_config_handler('gojuukaze:textHandler')
    class TextHandler(BaseHandler):
    """
    args:
    {
       '_handler':'gojuukaze:textHandler',
       'text':'xxx'
    }
    
    返回
    {
        'text':'xx',
    }
    """
    def calculate(self):
        text = self.args['text']
    
        return {
            'text': text,
        }


至此你已经成功编写了一个handler，载入handler需要重启工程

.. note::

    函数 ``calculate()`` 并没有限制返回的数据类型，你可以返回字符串、字典等

要测试你写的handler，可以用 ``get_real_config()`` 函数

.. code-block::  

   In [1]: from app.manager.config_manager_v2 import get_real_config
   In [2]: get_real_config({'_handler':'gojuukaze:textHandler','text':'123'})

   Out[2]: {'text': '123'}