from django.urls import path
from django.contrib.sitemaps.views import sitemap
from django.contrib.sitemaps import GenericSitemap

from app.sitemap import article_dict
from .views import views_class
from .views import views

app_name = 'app'
urlpatterns = [
    path('', views_class.Home.as_view(), name='index'),
    path('article/<int:article_id>', views_class.DetailArticle.as_view(), name='detail_article'),

    path('category/<int:category_id>', views_class.CategoryArticle.as_view(), name='category_article'),
    path('tag/<int:tag_id>', views_class.TagArticle.as_view(), name='tag_article'),
    path('comment/create', views.create_comment, name='create_comment'),

    path('image/upload', views.upload_image, name='upload_image'),
    path('images', views.get_album, name='get_album'),
    path('image/delete', views.delete_image, name='delete_image'),
    path('sitemap.xml', sitemap, {'sitemaps':
                                      {'article': GenericSitemap(article_dict, priority=0.6), },
                                  },
         name='django.contrib.sitemaps.views.sitemap'),
    #path('<path:url>', views_class.DetailFlatPage.as_view(), name='detail_flatpage'),

]
