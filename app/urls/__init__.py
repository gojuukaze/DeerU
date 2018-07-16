# -*- coding:utf-8 -*-
import re

from django.conf import settings
from django.urls import path, include, re_path

app_name = 'app'

urlpatterns = [
    path('', include('app.urls.urls')),
    path(settings.FLATPAGE_URL.lstrip('/').strip('/'), include('app.urls.flatpage_url')),

]
