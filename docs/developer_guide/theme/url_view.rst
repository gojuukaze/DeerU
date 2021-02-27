.. _page-c-t:

========================
页面的context与template
========================

下面每个context中都包含 :ref:`基础context <context>` ，
template中都包含 :ref:`基础template <templates>` ，
文档中不再重复说明，



首页
==============

    * url : ``/`` 
    * view : ``views_v2.home_view``
    * name : ``index`` 
    * 请求方式 : ``GET``
    * 参数 : 
        - page : 页码，默认： 1
        - pre_page : 每页文章数，默认：7
    * context :: 
        
        {
            'paginator' : DeerUPaginator,
            'article_list' : [ Article, Article ]
        }

    * templates ::

       {
           # 文章列表模板
           'article_list_template': 'base_theme2/article_list.html',
           # 文章列表前的导航，如：（首页/分类/默认分类）；分类页，标签页用到
           'article_list_breadcrumb_template': 'base_theme2/article_list_breadcrumb.html',
           # 单个文章item
           'article_list_item_template': 'base_theme2/article_list_item.html',
           'article_list_empty_item_template': 'base_theme2/article_list_empty_item.html',
           # 文章列表页的侧边栏
           'article_list_sidebar_template': 'base_theme2/body_section_sidebar.html',
       }

文章列表 -- 根据分类筛选
========================

    * url : ``category/<int:category_id>`` 
    * view : ``views_v2.category_article_list_view``
    * name : ``category_article`` 
    * 请求方式 : ``GET``
    * 参数 : 
        - page : 页码，默认： 1
        - pre_page : 每页文章数，默认：7
    * context :: 
        
        {
            'paginator' : DeerUPaginator,
            'article_list' : [ Article, Article ],
            'breadcrumbs' : [ '分类', Category ]
        }

    * templates ::

       {
           # 文章列表模板
           'article_list_template': 'base_theme2/article_list.html',
           # 文章列表前的导航，如：（首页/分类/默认分类）；分类页，标签页用到
           'article_list_breadcrumb_template': 'base_theme2/article_list_breadcrumb.html',
           # 单个文章item
           'article_list_item_template': 'base_theme2/article_list_item.html',
           'article_list_empty_item_template': 'base_theme2/article_list_empty_item.html',
           # 文章列表页的侧边栏
           'article_list_sidebar_template': 'base_theme2/body_section_sidebar.html',
       }

文章列表 -- 根据标签筛选
==========================

    * url : ``tag/<int:tag_id>`` 
    * view : ``views_v2.tag_article_list_view``
    * name : ``tag_article`` 
    * 请求方式 : ``GET``
    * 参数 : 
        - page : 页码，默认： 1
        - pre_page : 每页文章数，默认：7
    * context :: 
        
        {
            'paginator' : DeerUPaginator,
            'article_list' : [ Article, Article ],
            'breadcrumbs' : [ '标签', Tag ]

        }

    * templates ::

       {
           # 文章列表模板
           'article_list_template': 'base_theme2/article_list.html',
           # 文章列表前的导航，如：（首页/分类/默认分类）；分类页，标签页用到
           'article_list_breadcrumb_template': 'base_theme2/article_list_breadcrumb.html',
           # 单个文章item
           'article_list_item_template': 'base_theme2/article_list_item.html',
           'article_list_empty_item_template': 'base_theme2/article_list_empty_item.html',
           # 文章列表页的侧边栏
           'article_list_sidebar_template': 'base_theme2/body_section_sidebar.html',
       }

文章详情
==============

    * url : ``article/<int:article_id>`` 
    * view : ``views_v2.detail_article_view``
    * name : ``detail_article`` 
    * 请求方式 : ``GET``
    * 参数 : 
    * context :: 
        
        {
            'article' : Article
            # 不再返还comment，通过 article.comments 获取
            # 'comments' : [ Comment, Comment, ]
            'comment_form' : CommentForm, # 评论的form
            'form_error' : 'xx' # 提交comment_form的错误信息
        }

    * templates ::

       {
           # 文章页模板
           'detail_article_template': 'base_theme2/detail_article.html',
           # 文章内容
           'detail_article_content_template': 'base_theme2/detail_article_content.html',
           # 文章评论
           'detail_article_comment_template': 'base_theme2/detail_article_comment.html',
           # 文章页侧边栏
           'detail_article_sidebar_template': 'base_theme2/body_section_sidebar.html',
      }

创建评论
==============

    这个view其实是返回302重定向，重地下到文章详情页，如果有错误，会添加get参数的 ``form_error`` 中

    * url : ``comment/create`` 
    * view : ``views.create_comment`` 
    * name : ``create_comment`` 
    * 请求方式 : ``POST``
    * 参数 : 
        - anchor : 锚，如果需要评论后跳转到相关的地方，则带上这个参数，如 "#comment"
        - content : 内容
        - email : 可不填
        - nickname : nickname
        - article_id : article_id
        - type : 类型，可选项如下：

            + 201 : 对文章评论
            + 202 : 对评论评论
        - to_id : 回复的评论id，具体说明参见 :ref:`Comment <model-comment>` model说明，以及DeerU源码
        - root_id : 根评论id，具体说明参见 :ref:`Comment <model-comment>` model说明，以及DeerU源码

单页面
==============

    * url : ``你的单页面前缀/<path:url>``
    * view : ``views_v2.detail_flatpage_view``
    * name : ``detail_flatpage`` 
    * template : ``detail_flatpage.html`` 
    * 请求方式 : ``GET`` 
    * 参数 : 
    * context :: 
        
        {
            'flatpage' : FlatPage,
        }

    * templates ::

       {
          # 单页面页模板
          'detail_flatpage_template': 'base_theme2/detail_flatpage.html',
          # 单页面页侧边栏
          'detail_flatpage_sidebar_template': 'base_theme2/body_section_sidebar.html',
       }

404面
==============

    * view : ``views_v2.page_not_found_view``
    * 请求方式 : ``GET``
    * 参数 :
    * templates ::

       {
          # 404页模板
          '404_template': 'base_theme2/404.html',
          # 404页侧边栏
          '404_sidebar_template': 'base_theme2/empty.html',
       }
