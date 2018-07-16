=============
配置的值类型
=============

DeerU规定了两种配置的值类型，并为每种类型都提供了返回对应结构的表达式

.. _config-type-img:

图片类型
===========

图片类型有三个type: 

* img : 对应img标签

* svg : 对应svg标签

* fa  : 对应fontawesome的图标

img类型
--------

    结构:: 

        {
            "type":'img',
            "src":'/media/logo_white.png',
            "attrs":{
                "style":'xx',
                "hight":'xx',
            }

        }

    * src : 图片地址 

    * attrs : 其他属性 

svg类型
--------

    结构:: 

        {
            "type":'svg',
            "svg":'xxx',
            "attrs":{
                "style":'xx',
                "hight":'xx',
            }

        }

    * svg : svg图片标签 

    * attrs : 其他属性 

fa类型
--------

    fa类型使用的是 `fontawesome <https://fontawesome.com/icons?d=gallery&m=free>`_ 图标,
    base_theme使用的是fontawesome5版本，你可以在其官网中获取需要的图片，其他主题使用的版本参照主题说明

    结构:: 

        {
            "type":'fa',
            "class_":'fa xx',
            "attrs":{
                "style":'xx',
                "hight":'xx',
            }

        }

    * class_ : fontawesome图标<i>标签class的值，如这个图标 `address-book <https://fontawesome.com/icons/address-book?style=solid>`_ ，其内容就是 ``fas fa-address-book`` 
    
    * attrs : 其他属性 


.. _config-type-text:

文本类型
===========

文本类型结构如下:: 

    {
        "text":'xx',
        "attrs":{
            "style":'xx',
        }

    }

* text : 文本值 

* attrs : 其他属性 
