# -*- coding:utf-8 -*-
from cache_utils.decorators import cached
from django.conf import settings
from django.template.loader import render_to_string

from app.consts import FLAT_PAGE_URL_CACHE_KEY, v2_app_config_context
from app.db_manager.config_manager import get_config_by_name
from app.db_manager.content_manager import all_flatpage, get_article_by_id, get_valid_comment_by_id_and_article, \
    get_comment_by_id
from app.manager.email import send_mail


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
        to_comment = get_valid_comment_by_id_and_article(to_id, article_id)
        if not to_comment:
            return False, '错误to_id'

        if to_comment.root_id == -1:
            if root_id != to_id:
                return False, '错误to_id'
        else:
            if to_comment.root_id != root_id:
                return False, '错误root_id'

    return True, ''


def send_reply_email(comment):
    """

    :param comment:
    :type comment: app.app_models.content_model.Comment
    :return:
    :rtype:
    """

    if comment.type != 202:
        return

    to_comment = get_comment_by_id(comment.to_id)
    if not to_comment or not to_comment.email:
        return

    blog_config = get_config_by_name(v2_app_config_context['v2_blog_config']).v2_real_config
    blog_name = blog_config.get('blog_name', '')
    article = comment.article()
    comment_url = article.url() + '#comment-' + str(comment.id)
    email = blog_config['email']
    send_mail(
        '你在《%s》下的评论有新回复 (来自于：%s)' % (article.title, blog_name),
        '',
        [to_comment.email],
        email_config=email,
        html_message=render_to_string('app/email/comment_email.html',
                                      {'nickname': blog_config.get('nickname', ''), 'article': article,
                                       'comment': comment, 'comment_url': comment_url,
                                       'host': blog_config['host']})
    )
