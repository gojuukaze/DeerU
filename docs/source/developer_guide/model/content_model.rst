==============
Content Model
==============

Article
==============

.. py:class:: Article

    文章

    .. py:attribute:: title
        
        标题

    .. py:attribute:: content
        
        正文

    .. py:attribute:: summary
        
        简介

    .. py:attribute:: image
        
        封面图片

    .. py:classmethod:: url

        返回文章url

    .. py:classmethod:: get_absolute_url

        返回文章url

    .. py:classmethod:: last_article

        上一篇，返回:: 

            {
                'title': 'xx',
                'id' : 12,
                'url' : '/article/12'
            }

    .. py:classmethod:: next_article

        下一篇，返回:: 

            {
                'title': 'xx',
                'id' : 12,
                'url' : '/article/12'
            }

    .. py:classmethod:: meta_data

        返回ArticleMeta

    .. py:classmethod:: category

        返回文章的分类

    .. py:classmethod:: tags

        返回文章的tag

    .. py:classmethod:: comments

        返回评论

    .. py:classmethod:: format_comments

        返回按父子关系整理后的评论:: 
            
            [ 
                {
                    'comment' : Comment , 
                    'children':[ 
                            {'comment' : Comment, 'to_nickname':'xx'} ,

                            { ... }
                    ] 
                },

                {...}
            ]
            
ArticleMeta
==============

.. py:class:: ArticleMeta


    .. py:attribute:: article_id
        
        article_id

    .. py:attribute:: read_num
        
        阅读量

    .. py:attribute:: comment_num
        
        评论数


Category
==============

.. py:class:: Category


    .. py:attribute:: name
        
        name

    .. py:attribute:: father_id
        
        父级目录

    .. py:attribute:: m_order
        
        排序

    .. py:classmethod:: url

        返回文章列表页的url

    .. py:classmethod:: get_absolute_url

        返回文章列表页的url

    .. py:classmethod:: get_article_category_list

        返回ArticleCategory queryset

    .. py:classmethod:: get_article_list

        返回分类下的文章 queryset

ArticleCategory
=======================

.. py:class:: ArticleCategory

    文章分类关系表

    .. py:attribute:: article_id

    .. py:attribute:: category_id
        

Tag
==============

.. py:class:: Tag


    .. py:attribute:: name
        
        name

    .. py:classmethod:: url

        返回文章列表页的url

    .. py:classmethod:: get_absolute_url

        返回文章列表页的url


    .. py:classmethod:: get_article_tag_list

        返回ArticleTag queryset

    .. py:classmethod:: get_article_list

        返回tag下的文章 queryset

ArticleTag
==============

.. py:class:: ArticleTag

    文章tag关系表

    .. py:attribute:: article_id

    .. py:attribute:: tag_id
        
Comment
==============

.. py:class:: Comment

    评论

    .. py:attribute:: nickname

    .. py:attribute:: email

    .. py:attribute:: content

        正文

    .. py:attribute:: type

        评论类型  

            * 201 : 对文章评论
            * 202 : 对评论评论

    .. py:attribute:: root_id

        根评论id。对文章评论时，这一项无意义。对评论回复时就是评论的id，对回复回复时，是最早的那条评论id。

    .. py:attribute:: to_id

        给谁的评论。对文章评论时，这一项无意义。

    .. note::

        :: 
    
            以下说的 评论、回复 其实是一个东西，方便区分用了两个词
    
            评论：对文章的评论称作 "评论";
            回复：对评论的评论称作 "回复"，对回复的回复也叫 "回复";
    
            注意区分root_id和to_id，

            评论 root_id必须是-1
            对评论的回复 root_id==to_id
            
            如：
    
            文章-0
                |__ 评论-1
                      |__ 回复-2
                      |__ 回复-3
                             |__ 回复-3-1
    
            评论-1   ：root_id是 文章-0 的id
            回复-2   ：root_id是 评论-1 的id; to_id是 评论-1 的id;
            回复-3   ：root_id是 评论-1 的id; to_id是 评论-1 的id;
            回复-3-1 ：root_id是 评论-1 的id; to_id是 回复-3 的id;


FlatPage
==============

.. py:class:: FlatPage

    单页面

    .. py:attribute:: title
        
        标题

    .. py:attribute:: content
        
        正文

    .. py:attribute:: url
        
        url

    .. py:classmethod:: get_absolute_url

        返回文章url
