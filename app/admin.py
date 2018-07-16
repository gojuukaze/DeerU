from ast import literal_eval

from adminsortable2.admin import SortableAdminMixin
from django.contrib import admin
from django.template.loader import render_to_string

# Register your models here.
from django.core.cache import cache

from app.consts import Global_value_cache_key, app_config_context, Theme_config_cache_key, Theme_cache_key
from app.ex_admins.admin import FormInitAdmin
from app.forms import ArticleAdminForm, CategoryAdminForm, FlatpageAdminForm, ConfigAdminForm
from app.db_manager.content_manager import filter_category_by_article, create_tag, filter_tag_by_name_list, \
    filter_tag_by_article
from app.ex_admins.list_filter import CategoryFatherListFilter
from app.manager.ct_manager import update_one_to_many_relation_model, get_tag_for_choice
from app.app_models.other_model import Album
from app.app_models.config_model import Config
from app.app_models.content_model import Article, Category, ArticleCategory, ArticleTag, Tag, FlatPage
from tool.deeru_html import Tag as htag


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

    # fieldsets = (
    #     (None, {
    #         'fields': ('title',)
    #     }),
    #     ('其他选项', {
    #         'classes': ('collapse',),
    #         'fields': ('cover_img', 'cover_summary'),
    #     }),
    #     (None, {
    #         'fields': ('content', 'category', 'tag')
    #     }),
    # )

    # fields = ( 'read_num', 'comment_num')

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
        cover_img = form.cleaned_data['cover_img'] if form.cleaned_data['is_use_cover_img'] else None
        cover_summary = form.cleaned_data['cover_summary'] if form.cleaned_data['is_use_cover_summary'] else None
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
    form = ConfigAdminForm
    is_first = True
    list_display = ['name', 'id']
    fields = ['name', 'config', 'last_config']

    def get_changelist(self, request, **kwargs):
        if request.path.endswith('/change/'):
            self.is_first = True

        return super().get_changelist(request, **kwargs)

    def get_object(self, request, object_id, from_field=None):
        obj = super().get_object(request, object_id, from_field)
        if self.is_first:
            self.config_bk = obj.config
            self.is_first = False
        return obj

    def save_model(self, request, obj, form, change):
        if not self.is_first:
            obj.last_config = self.config_bk
        self.is_first = True
        self.config_bk = None
        if obj.name == app_config_context['global_value']:
            cache.set(Global_value_cache_key, literal_eval(obj.config), 3600)
        elif obj.name == app_config_context['common_config']:
            cache.set(Theme_cache_key, literal_eval(obj.config)['theme'], 3600)

        return super().save_model(request, obj, form, change)

    def add_view(self, request, form_url='', extra_context=None):
        self.is_first = True
        self.config_bk = ''
        return super().add_view(request, form_url, extra_context)


@admin.register(Category)
class CategoryAdmin(SortableAdminMixin, admin.ModelAdmin):
    form = CategoryAdminForm
    change_list_template = 'app/admin/category_change_list.html'
    list_display = ['name', 'id', ]
    search_fields = ['name']
    list_filter = (
        CategoryFatherListFilter,
    )


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


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
