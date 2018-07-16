from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils import timezone

from app.consts import Comment_Type
from app.manager import get_rich_text_filed
from tool.html_helper import clean_all_tags, get_safe_comment_html

deeru_rich_editor = settings.DEERU_RICH_EDITOR

DeerURichFiled = get_rich_text_filed(deeru_rich_editor['filed'])

__all__ = ['Article', 'ArticleMeta', 'Category', 'ArticleCategory', 'Tag', 'ArticleTag']


class Article(models.Model):
    class Meta:
        verbose_name = '文章'
        verbose_name_plural = '文章'

    title = models.CharField(verbose_name='标题', max_length=100, db_index=True, null=False, blank=False)
    summary = models.CharField(verbose_name='摘要', max_length=200, null=True, blank=True, editable=False)
    image = models.CharField(verbose_name='图片', max_length=200, null=True, blank=True, editable=False)

    content = DeerURichFiled(verbose_name='正文', null=False, blank=False, **deeru_rich_editor['article_kwargs'])

    created_time = models.DateTimeField(verbose_name="创建时间", default=timezone.now, editable=False)
    modified_time = models.DateTimeField(verbose_name="修改时间", auto_now=True)

    def __str__(self):
        if len(self.title) <= 15:
            return '文章-%d<%s>' % (self.id, self.title)
        else:
            return '文章-%d<%s...%s>' % (self.id, self.title[:7], self.title[-8:])

    def url(self):
        return reverse('app:detail_article', args=(self.id,))

    def get_absolute_url(self):
        return self.url()

    def last_article(self):
        try:
            a = Article.objects.filter(id__lt=self.id).values('id', 'title').order_by('-id')[0]
            a['url'] = reverse('app:detail_article', args=(a['id'],))
            return a
        except:
            return None

    def next_article(self):
        try:
            a = Article.objects.filter(id__gt=self.id).values('id', 'title').order_by('-id')[0]
            a['url'] = reverse('app:detail_article', args=(a['id'],))
            return a
        except:
            return None

    def meta_data(self):
        from app.db_manager.content_manager import get_article_meta_by_article
        return get_article_meta_by_article(self.id)

    def category(self):
        from app.db_manager.content_manager import filter_category_by_article
        return filter_category_by_article(self.id)

    def tags(self):
        from app.db_manager.content_manager import filter_tag_by_article
        return filter_tag_by_article(self.id)

    def comments(self):
        from app.db_manager.content_manager import filter_comment_by_article
        return filter_comment_by_article(self.id)

    def format_comments(self):
        """
        返回按父子结构整理后的评论
        以下说的 评论、回复 其实是一个东西，方便区分用了两个词，具体看类Comment的说明

        child：包含评论的回复，和对这条评论下回复的回复，children不会再有children

        [ { 'comment' : Comment , 'children': [ {'comment' : Comment, 'to_nickname':'xx'} ] } ,{...}]
        :return:
        """
        from app.db_manager.content_manager import filter_comment_by_article
        result = []
        # 根评论在result中的位置,id:pos
        root_comment_id_to_pos = {}

        comments = filter_comment_by_article(self.id)
        # 评论在queryset中的位置,id:pos
        comment_id_to_pos = {}

        r_pos = 0
        c_pos = 0
        for c in comments:
            if c.type == 201:
                # 根评论
                result.append({'comment': c, 'children': []})
                root_comment_id_to_pos[c.id] = r_pos
                r_pos += 1
            else:
                to_pos = comment_id_to_pos[c.to_id]
                to_comment = comments[to_pos]

                root_pos = root_comment_id_to_pos[c.root_id]

                result[root_pos]['children'].append({'comment': c, 'to_nickname': to_comment.nickname})

            comment_id_to_pos[c.id] = c_pos
            c_pos += 1

        return result


class ArticleMeta(models.Model):
    class Meta:
        verbose_name = '文章meta'
        verbose_name_plural = '文章meta'

    article_id = models.IntegerField(verbose_name='article_id', db_index=True, unique=True)

    read_num = models.IntegerField(verbose_name='阅读量', default=0)
    comment_num = models.IntegerField(verbose_name='评论量', default=0)

    created_time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    modified_time = models.DateTimeField(verbose_name="修改时间", auto_now=True)


class Category(models.Model):
    class Meta:
        verbose_name = '分类'
        verbose_name_plural = '分类'
        ordering = ['-m_order']

    name = models.CharField(verbose_name='名称', max_length=30, unique=True)
    father_id = models.IntegerField(verbose_name='父级目录', default=-1)
    m_order = models.PositiveIntegerField(verbose_name='排序', default=0, blank=False, null=False)

    created_time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    modified_time = models.DateTimeField(verbose_name="修改时间", auto_now=True)

    def __str__(self):
        return '分类-%d<%s>' % (self.id, self.name,)

    def url(self):
        return reverse('app:category_article', args=(self.id,))

    def get_absolute_url(self):
        return self.url()

    def get_article_category_list(self):
        from app.db_manager.content_manager import filter_article_category_by_category
        return filter_article_category_by_category(self.id)

    def get_article_list(self):
        from app.db_manager.content_manager import filter_article_by_category
        return filter_article_by_category(self.id)


class ArticleCategory(models.Model):
    class Meta:
        verbose_name = '文章分类'
        verbose_name_plural = '文章分类'

    article_id = models.IntegerField(verbose_name='article_id')
    category_id = models.IntegerField(verbose_name='分类id')

    created_time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    modified_time = models.DateTimeField(verbose_name="修改时间", auto_now=True)


class Tag(models.Model):
    class Meta:
        verbose_name = '标签'
        verbose_name_plural = '标签'

    name = models.CharField(verbose_name='名称', max_length=20, unique=True)

    created_time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    modified_time = models.DateTimeField(verbose_name="修改时间", auto_now=True)

    def __str__(self):
        return '标签-%d<%s>' % (self.id, self.name,)

    def url(self):
        return reverse('app:tag_article', args=(self.id,))

    def get_absolute_url(self):
        return self.url()

    def get_article_tag_list(self):
        from app.db_manager.content_manager import filter_article_tag_by_tag
        return filter_article_tag_by_tag(self.id)

    def get_article_list(self):
        from app.db_manager.content_manager import filter_article_by_tag
        return filter_article_by_tag(self.id)


class ArticleTag(models.Model):
    class Meta:
        verbose_name = '文章标签'
        verbose_name_plural = '文章标签'

    article_id = models.IntegerField(verbose_name='article_id')
    tag_id = models.IntegerField(verbose_name='标签id')

    created_time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    modified_time = models.DateTimeField(verbose_name="修改时间", auto_now=True)

    def tag(self):
        from app.db_manager.content_manager import get_tag_by_id

        return get_tag_by_id(self.tag_id)


class Comment(models.Model):
    """
    以下说的 评论、回复 其实是一个东西，方便区分用了两个词

    评论：对文章的评论称作 "评论";
    回复：对评论的评论称作 "回复"，对回复的回复也叫 "回复";


    """

    class Meta:
        verbose_name = '评论'
        verbose_name_plural = '评论'

    nickname = models.CharField(verbose_name='昵称', max_length=20, null=True, blank=True)
    email = models.EmailField(verbose_name='邮箱', null=True, blank=True)
    content = models.TextField(verbose_name='内容',
                               # options={
                               #     'height': 300,
                               #     'toolbarButtons': ['fontSize', 'color', '|', 'bold', 'italic', 'underline',
                               #                        'strikeThrough',
                               #                        '|', 'emoticons', 'insertLink', 'quote', ],
                               #     'imageUpload': False,'quickInsertButtons':[],
                               #     'imageManagerLoadURL':'/','imageManagerDeleteURL':'/'
                               # }
                               )

    article_id = models.IntegerField(verbose_name='article_id')

    """
    注意区分root_id和to_id，
    回复才有to_id
    如：

    文章-0
       |__ 评论-1
              |__ 回复-2
              |__ 回复-3
                     |__ 回复-3-1

    评论-1   ：root_id是 文章-0 的id
    回复-2   ：root_id是 评论-1 的id; to_id是 评论-1 的id;
    回复-3   ：root_id是 评论-1 的id; to_id是 评论-1 的id;
    回复-3-1 ：root_id是 评论-1 的id; to_id是 回复-3 的id;
    """

    # 根id，评论的root_id就是article_id，回复的root_id就是 评论id
    root_id = models.IntegerField(verbose_name='root_id')
    # 对评论的回复, to_id是-1
    # 对回复的回复,to_id是回复的id
    to_id = models.IntegerField(verbose_name='to_id', default=-1)

    type = models.IntegerField(verbose_name='type', choices=Comment_Type)

    created_time = models.DateTimeField(verbose_name="创建时间", default=timezone.now, editable=False)
    modified_time = models.DateTimeField(verbose_name="修改时间", auto_now=True)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.nickname = clean_all_tags(self.nickname)
        if self.email:
            self.email = clean_all_tags(self.email)
        self.content = get_safe_comment_html(self.content)
        super().save(force_insert, force_update, using, update_fields)


class FlatPage(models.Model):
    class Meta:
        verbose_name = '单页面'
        verbose_name_plural = '单页面'

    title = models.CharField(verbose_name='标题', max_length=100, null=False, blank=False)
    url = models.CharField(verbose_name='url', max_length=100, null=False, blank=False)
    content = DeerURichFiled(verbose_name='正文', null=False, blank=False, **deeru_rich_editor['article_kwargs'])

    created_time = models.DateTimeField(verbose_name="创建时间", default=timezone.now, editable=False)
    modified_time = models.DateTimeField(verbose_name="修改时间", auto_now=True)

    def __str__(self):
        if len(self.title) <= 15:
            return '单页面-%d<%s>' % (self.id, self.title)
        else:
            return '单页面-%d<%s...%s>' % (self.id, self.title[:7], self.title[-8:])

    def get_absolute_url(self):
        return reverse('app:detail_flatpage', args=(self.url,))
