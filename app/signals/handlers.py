from bs4 import BeautifulSoup
from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save

from app.app_models.content_model import Article, Tag, Comment
from app.app_models.other_model import Album
from app.db_manager.content_manager import get_or_create_article_meta, get_article_meta_by_article
from tool.kblog_expression.manager import format_expression


@receiver(pre_save, sender=Article, dispatch_uid="article_pre_save")
def article_pre_save(sender, **kwargs):
    soup = BeautifulSoup(kwargs['instance'].content)
    img = soup.find('img')
    if img:
        kwargs['instance'].image = img['src']
    kwargs['instance'].summary = soup.get_text()[:170] + "..."


@receiver(post_save, sender=Article, dispatch_uid="article_post_save")
def article_post_save(sender, **kwargs):
    get_or_create_article_meta(kwargs['instance'].id)


@receiver(post_save, sender=Comment, dispatch_uid="comment_post_save")
def comment_post_save(sender, **kwargs):
    a_meta = get_article_meta_by_article(kwargs['instance'].article_id)
    a_meta.comment_num += 1
    a_meta.save()


@receiver(pre_save, sender=Album, dispatch_uid="album_pre_save")
def album_pre_save(sender, **kwargs):
    if not kwargs['instance'].name:
        kwargs['instance'].name = kwargs['instance'].img.name
