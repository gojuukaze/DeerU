# -*- coding:utf-8 -*-

from django.urls import path

from app.views import views_class

urlpatterns = [
    path('<path:url>', views_class.DetailFlatPage.as_view(), name='detail_flatpage'),

]
