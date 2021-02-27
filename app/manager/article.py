from app.db_manager.content_manager import all_article_order_by_id, filter_article_by_category, filter_article_by_tag
from app.ex_paginator import DeerUPaginator


def get_article_list_and_paginator(page, per_page):
    paginator = DeerUPaginator(all_article_order_by_id(), per_page, page)

    article_list = paginator.page(page).object_list
    return article_list, paginator


def get_article_list_and_paginator_by_category(category_id, page, per_page):
    paginator = DeerUPaginator(filter_article_by_category(category_id), per_page, page)

    article_list = paginator.page(page).object_list
    return article_list, paginator


def get_article_list_and_paginator_by_tag(tag_id, page, per_page):
    paginator = DeerUPaginator(filter_article_by_tag(tag_id), per_page, page)

    article_list = paginator.page(page).object_list
    return article_list, paginator
