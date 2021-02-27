.. _context:

==============
Context
==============

context是什么？
====================
渲染html时view会把context传给html模板，context包含了模板需要的变量，数据等（如：文章、分类）。


基础context格式
===================
每个view都返回了一个基础的context，他的格式如下:: 

    context = {
    
        'config' : {
            'v2_iconbar_config' : { ... },
            'v2_navbar_config' : { ... },
            'v2_common_config' : [ ... ],
            'v2_blog_config' : { ... }
        }

        'extend_data' : {
            'category' : [ 
    
                {
                    'category' : Category, # Category model的实例化对象
                    'children' :[
                        {
                            'category':Category
                        },
                        { ... }
                    ]
            
                },
    
                { ... }
            
            ]
    
            'tags' :[ Tag, Tag ,] # Tag model的实例化对象
        }
    }

* config : 后台的配置，默认返回的配置有 'v2_iconbar_config'，'v2_navbar_config'，'v2_common_config'，'v2_blog_config'
* extend_data : 里面包含了博客的分类，标签
  - category : 按父子结构整理后的分类
  - tag : 按文章数量排序的tag list，返回20个

在html中使用context
========================

在html中使用context实例

.. code-block:: html

   <title>博客名: {{ config.v2_blog_config.title }}</title>

   <div>
   {% for t in tags %}
      <span>{{ t.name }}</span>
   {% endfor %}
   </div>

context 中返回的 article, category, tag 等都是对应model的实例化对象，你可以直接在模板中使用对象的成员变量及函数，如

.. code-block:: html

    # 假设context =  { 'article':Article }

    # html:
    <h1>{{ article.title }}</h1>
    <div>{{ article.content }}</div>

    # 获取文章的分类
    {% for c in article.category %}
        <span>{{ c.name }}</span> |
    {% end for %}

DeerU为每个model都提供了丰富的成员函数，你轻易从对象中获取你需要的数据。
每个model的变量、函数说明参照 :ref:`model` 这里不再叙述。

除了model里的对象，context还有一些特殊的对象：


    .. py:class:: DeerUPaginator
    
        deeru的Paginator
    
        .. py:attribute:: end_index
    
            末尾页码
            
        .. py:attribute:: current_page_num
    
            当前页码


    .. py:class:: CommentForm
    
        评论的form


在html中读取配置
=========================

如果你看了使用者指南你应该清楚，DeerU内置了"顶部导航栏"、"顶部图标栏"两个配置，你可以在view传到的context['config']中找到他们。

在前端代码中，你可以通过 ``config.v2_xxx`` 获取配置（v2.0+的配置以v2_开头），如 ::

   <div>博客名： {{ config.v2_blog_config.title }}</div>

如果你还需要其他配置，你可以把配置放到"通用配置"中，你也可以新建一个自己的配置。


每个页面单独的context
========================

每个页面单独的 context 见 :ref:`page-c-t` 。
