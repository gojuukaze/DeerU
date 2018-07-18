# -*- coding:utf-8 -*-
from cache_utils.decorators import cached

from app.consts import FLAT_PAGE_URL_CACHE_KEY
from app.db_manager.content_manager import all_flatpage, get_article_by_id, get_comment_by_id_and_article


@cached(86400, key=FLAT_PAGE_URL_CACHE_KEY)
def get_flatpage_url_dict():
    pages = all_flatpage().values_list('url', 'id')
    urld = {}
    for k, v in pages:
        urld[k] = v
    return urld


def is_valid_comment(comment_form):
    to_id = comment_form.cleaned_data['to_id']
    article_id = comment_form.cleaned_data['article_id']
    root_id = comment_form.cleaned_data['root_id']
    type = comment_form.cleaned_data['type']

    article = get_article_by_id(article_id)
    if not article:
        return False, '错误id'

    if type == 202:
        to_comment = get_comment_by_id_and_article(to_id, article_id)
        if not to_comment:
            return False, '错误to_id'

        if to_comment.root_id == -1:
            if root_id != to_id:
                return False, '错误to_id'
        else:
            if to_comment.root_id != root_id:
                return False, '错误root_id'

    return True, ''
