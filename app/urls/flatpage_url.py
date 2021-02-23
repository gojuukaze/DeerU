# -*- coding:utf-8 -*-

from django.urls import path

from app.views import views_class, views_v2

urlpatterns = [
    path('<path:url>', views_v2.detail_flatpage_view, name='detail_flatpage'),

]
