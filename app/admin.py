from ast import literal_eval

from adminsortable2.admin import SortableAdminMixin
from django.contrib import admin, messages
from django.template.loader import render_to_string

# Register your models here.
from django.core.cache import cache
from django.utils.safestring import mark_safe

from app.consts import Global_value_cache_key, app_config_context, Theme_config_cache_key, Theme_cache_key, \
    CommentStatusChoices, v2_app_config_context
from app.ex_admins.admin import FormInitAdmin
from app.forms import ArticleAdminForm, CategoryAdminForm, FlatpageAdminForm, ConfigAdminForm
from app.db_manager.content_manager import filter_category_by_article, create_tag, filter_tag_by_name_list, \
    filter_tag_by_article
from app.ex_admins.list_filter import CategoryFatherListFilter
from app.manager.ct_manager import update_one_to_many_relation_model, get_tag_for_choice
from app.app_models.other_model import Album
from app.app_models.config_model import Config, Version
from app.app_models.content_model import Article, Category, ArticleCategory, ArticleTag, Tag, FlatPage, Comment
from tool.deeru_html import Tag as htag
from tool.secure import encrypt
from tool.sign import unsign, sign


@admin.register(Article)
class ArticleAdmin(FormInitAdmin):
    form = ArticleAdminForm
    change_form_template = 'app/admin/article_change_form.html'
    search_fields = ['title', 'id']
    # date_hierarchy = 'created_time'

    list_display = ['m_title', 'read_num', 'comment_num']
    # list_editable = ['title']
    # list_display_links = ['title']

    fields = ('title', 'cover_img', 'cover_summary', 'content', 'category', 'tag')

    def m_title(self, obj):
        return render_to_string('app/admin/article_title.html', {'article': obj})

    m_title.short_description = '标题'

    def read_num(self, obj):
        return obj.meta_data().read_num

    read_num.short_description = '阅读数'

    def comment_num(self, obj):
        return obj.meta_data().comment_num

    comment_num.short_description = '评论数'

    def get_object(self, request, object_id, from_field=None):
        obj = super().get_object(request, object_id, from_field)

        self.old_category = list(filter_category_by_article(obj.id))
        self.old_tag = list(filter_tag_by_article(obj.id))
        self.field_init_value['category'] = [c.id for c in filter_category_by_article(obj.id)]
        self.field_init_value['tag'] = ' '.join([t.name for t in self.old_tag])

        self.field_init_value['cover_img'] = obj.image
        self.field_init_value['cover_summary'] = obj.summary[:-3]

        return obj

    def get_form(self, request, obj=None, **kwargs):
        return super().get_form(request, obj, **kwargs)

    def save_model(self, request, obj, form, change):
        cover_img = form.cleaned_data['cover_img']
        cover_summary = form.cleaned_data['cover_summary']
        obj.cover_img = cover_img
        obj.cover_summary = cover_summary
        result = super().save_model(request, obj, form, change)
        new_category = form.cleaned_data['category']
        update_one_to_many_relation_model(ArticleCategory, 'article_id', obj.id, 'category_id', new_category,
                                          lambda x: [int(c_id) for c_id in x],
                                          [c.id for c in self.old_category])
        new_tag_name = form.cleaned_data['tag']
        add_tag_name = list(set(new_tag_name).difference(set(get_tag_for_choice())))
        for add_name in add_tag_name:
            create_tag(add_name)
        update_one_to_many_relation_model(ArticleTag, 'article_id', obj.id, 'tag_id', new_tag_name,
                                          lambda x: list(filter_tag_by_name_list(x).values_list('id', flat=True)),
                                          [t.id for t in self.old_tag])

        return result

    def get_changelist(self, request, **kwargs):
        if request.path.endswith('/change/'):
            self.field_init_value = {}
            self.old_category = []
            self.old_tag = []

        return super().get_changelist(request, **kwargs)

    def add_view(self, request, form_url='', extra_context=None):
        self.field_init_value = {}
        self.old_category = []
        self.old_tag = []
        return super().add_view(request, form_url, extra_context)


@admin.register(Config)
class ConfigAdmin(admin.ModelAdmin):
    # form = ConfigAdminForm
    is_first = True
    list_display = ['name', 'id']
    fields = ['v2_config']

    def get_object(self, request, object_id, from_field=None):
        obj = super().get_object(request, object_id, from_field)
        obj.v2_config['_id'] = obj.id
        return obj

    def get_queryset(self, request):
        return super().get_queryset(request).exclude(name__endswith='.old')

    def save_model(self, request, obj, form, change):

        if obj.name == v2_app_config_context['v2_blog_config']:
            if obj.v2_config['host'].endswith('/'):
                obj.v2_config['host'] = obj.v2_config['host'][:-1]
            # 对email进行特殊处理
            # 这快代码和发送邮件是强关联的，所以不用handler处理
            password = obj.v2_config['email'].get('password', '').strip()
            if password:
                temp = unsign(password)
                if not temp:
                    # 说明密码没经过加密
                    obj.v2_config['email']['password'] = sign(encrypt(password))

        return super().save_model(request, obj, form, change)


@admin.register(Category)
class CategoryAdmin(SortableAdminMixin, admin.ModelAdmin):
    form = CategoryAdminForm
    change_list_template = 'app/admin/category_change_list.html'
    list_display = ['name', 'id', ]
    search_fields = ['name']
    list_filter = (
        CategoryFatherListFilter,
    )

    def has_delete_permission(self, request, obj=None):
        # todo 因存在关联关系，暂时禁止删除，之后版本处理
        return False


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

    # todo 标签删除逻辑


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'show_img']

    def show_img(self, obj):
        t = htag('img', attrs={'src': obj.img.url, 'style': 'overflow:hidden', 'height': '200'})

        return t.format_html()

    show_img.short_description = '图片'


@admin.register(FlatPage)
class FlatPageAdmin(admin.ModelAdmin):
    form = FlatpageAdminForm

    list_display = ('m_title', 'url')
    search_fields = ('url', 'title')
    fields = ('url', 'title', 'content')

    def m_title(self, obj):
        return render_to_string('app/admin/flatpage_title.html', {'flatpage': obj})

    m_title.short_description = '标题'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    search_fields = ['content', 'nickname']
    list_display = ('author', 'm_status', 'm_content', 'article', 'created_time')
    list_filter = ['status', 'created_time']
    actions = ['make_pass', 'make_fail']

    def m_status(self, obj):
        return render_to_string('app/admin/comment_status.html', {'status': obj.status})

    m_status.short_description = '状态'

    def author(self, obj):
        return render_to_string('app/admin/comment_author.html',
                                {'nickname': obj.nickname, 'email': obj.email or '', 'status': obj.status,
                                 'id': obj.id})

    author.short_description = '作者'

    def m_content(self, obj):
        return render_to_string('app/admin/comment_content.html', {'comment': obj})

    m_content.short_description = '内容'

    def article(self, obj):
        article = obj.article()
        title = article.title if article else '文章不存在'
        url = obj.url() if article else ''
        return mark_safe(
            '<div style="display:flex;flex-direction:column">'
            '<a style="font-size:16px;" target="_blank" href="%s"><strong>%s</strong></a>'
            '<a style="font-size:12px;margin-top:3px" target="_blank" href="%s">跳转到文章评论</a>'
            '</div>' % (url, title, url)
        )

    article.short_description = '文章'

    def make_pass(self, request, queryset):
        for q in queryset:
            q.status = CommentStatusChoices.Passed
            q.save()
            self.message_user(request, "%s 通过" % str(q), level=messages.INFO)

    make_pass.short_description = '通过'

    def make_fail(self, request, queryset):
        for q in queryset:
            q.status = CommentStatusChoices.Failed
            q.save()
            self.message_user(request, "%s 不通过" % str(q), level=messages.INFO)

    make_fail.short_description = '不通过'
