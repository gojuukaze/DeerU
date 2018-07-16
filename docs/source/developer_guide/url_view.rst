.. _url-view:

====================
Url View接口文档
====================

下面每个context中都包含 :ref:`基础context <context>` ，下面文档中不再重复说明，
另外，context中对象的方法参考 :ref:`context` ，:ref:`model`


首页
==============

    * url : ``/`` 
    * view : ``views_class.Home`` 
    * name : ``index`` 
    * template : ``home.html`` 
    * 请求方式 : ``GET`` 
    * 参数 : 
        - page : 页码，默认： 1
        - pre_page : 每页文章数，默认：7
    * context :: 
        
        {
            'paginator' : DeerUPaginator,
            'article_list' : [ Article, Article ]
        }

文章列表 -- 根据分类筛选
========================

    * url : ``category/<int:category_id>`` 
    * view : ``views_class.CategoryArticle`` 
    * name : ``category_article`` 
    * template : ``category.html`` 
    * 请求方式 : ``GET`` 
    * 参数 : 
        - page : 页码，默认： 1
        - pre_page : 每页文章数，默认：7
    * context :: 
        
        {
            'paginator' : DeerUPaginator,
            'article_list' : [ Article, Article ]
        }
    
文章列表 -- 根据标签筛选
==========================

    * url : ``tag/<int:tag_id>`` 
    * view : ``views_class.TagArticle`` 
    * name : ``tag_article`` 
    * template : ``tag.html`` 
    * 请求方式 : ``GET`` 
    * 参数 : 
        - page : 页码，默认： 1
        - pre_page : 每页文章数，默认：7
    * context :: 
        
        {
            'paginator' : DeerUPaginator,
            'article_list' : [ Article, Article ]
        }

文章详情
==============

    * url : ``article/<int:article_id>`` 
    * view : ``views_class.DetailArticle`` 
    * name : ``detail_article`` 
    * template : ``detail_article.html`` 
    * 请求方式 : ``GET`` 
    * 参数 : 
    * context :: 
        
        {
            'article' : Article
            'comments' : [ Comment, Comment, ]
            'comment_form' : CommentForm, # 评论的form
            'form_error' : 'xx' # 提交comment_form的错误信息
        }

创建评论
==============

    需要注意，创建评论接口返回的html是文章详情的html，如果有错误，会添加 ``form_error`` 中

    * url : ``comment/create`` 
    * view : ``views.create_comment`` 
    * name : ``create_comment`` 
    * template : ``detail_article.html`` 
    * 请求方式 : ``POST`` 
    * 参数 : 
        - anchor : 锚，如果需要评论后跳转到相关的地方，则带上这个参数，如 "#comment"
        - content : 内容
        - email : 可不填
        - nickname : nickname
        - type : 类型，可选项如下：

            + 201 : 对文章评论
            + 202 : 对评论评论
        - to_id : 回复的评论id，具体说明参见 :ref:`Comment <model-comment>` model说明，以及DeerU源码
        - root_id : 根评论id，具体说明参见 :ref:`Comment <model-comment>` model说明，以及DeerU源码

    * context :: 
        
        {
            'article' : Article
            'comments' : [ Comment, Comment, ]
            'comment_form' : CommentForm, # 评论的form
            'form_error' : 'xx' # 提交comment_form的错误信息
        }

单页面
==============

    * url : ``你的单页面前缀/<path:url>`` 
    * view : ``views_class.DetailFlatPage`` 
    * name : ``detail_flatpage`` 
    * template : ``detail_flatpage.html`` 
    * 请求方式 : ``GET`` 
    * 参数 : 
    * context :: 
        
        {
            'flatpage' : FlatPage,
        }
