.. _context:

==============
Context
==============

渲染html时view会把context传给html模板，context包含了模板需要的变量，数据等。

如果你要开发主题，那么阅读这篇文档，可以帮您了解context中都包含了些什么


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

        'global' : {
            'category' : [ 
    
                {
                    'category' : Category, # Category - Category model的实例化对象
                    'children' :[
                        {
                            'category':Category
                        },
                        { ... }
                    ]
            
                },
    
                { ... }
            
            ]
    
            'tags' :[ Tag, Tag ,] # Tag - Tag model的实例化对象
        }
    }

* config : 需要添加在context中的所有配置，默认返回的配置有 'v2_iconbar_config'，'v2_navbar_config'，'v2_common_config'，'v2_blog_config'
* global : 里面包含了博客的分类，标签
  - category : 按父子结构整理后的分类
  - tag : 按文章数量排序的tag list，返回20个

context中的对象
==================

context中返回的article,category,tag等都是对应model的实例化对象，你可以直接在模板中使用对象的成员变量及函数，如:: 

    # 假设context =  { 'article':Article }

    # html:
    <h1>Article.title</h1>
    <div>Article.content</div>

    # 获取文章的分类
    {% for c in Article.category %}
        <span>c.name</span> | 
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

