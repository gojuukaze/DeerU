from django.conf import settings
from django.urls import path
from django.contrib.sitemaps.views import sitemap
from django.contrib.sitemaps import GenericSitemap

from app.sitemap import article_dict
from app.views import views_class
from app.views import views
from app.views import views_v2

urlpatterns = [
    path('', views_v2.home_view, name='index'),
    path('article/<int:article_id>', views_v2.detail_article_view, name='detail_article'),
    path('article/set_top/<int:article_id>', views.set_article_top_view, name='set_article_top'),

    path('category/<int:category_id>', views_v2.category_article_list_view, name='category_article'),
    path('tag/<int:tag_id>', views_v2.tag_article_list_view, name='tag_article'),
    path('comment/create', views.create_comment_view, name='create_comment'),

    path('image/upload', views.upload_image_view, name='upload_image'),
    path('images', views.get_album_view, name='get_album'),
    path('image/delete', views.delete_image_view, name='delete_image'),
    path('sitemap.xml', sitemap, {'sitemaps':
                                      {'article': GenericSitemap(article_dict, priority=0.6), },
                                  },
         name='django.contrib.sitemaps.views.sitemap'),
    # path('p/<path:url>', views_class.DetailFlatPage.as_view(), name='detail_flatpage'),

    path('404', views.page_not_found_view),

    path('config/<int:config_id>/html', views.get_config_html_view),

]
