# -*- coding:utf-8 -*-
from cache_utils.decorators import cached

from app.consts import FLAT_PAGE_URL_CACHE_KEY
from app.db_manager.content_manager import all_flatpage


@cached(86400, key=FLAT_PAGE_URL_CACHE_KEY)
def get_flatpage_url_dict():
    pages = all_flatpage().values_list('url', 'id')
    urld = {}
    for k, v in pages:
        urld[k] = v
    return urld
