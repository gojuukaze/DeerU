from ast import literal_eval

from django.contrib import admin

# Register your models here.
from django.core.cache import cache
from ktag.admin import MultipleChoiceAdmin

from app.consts import Global_value_cache_key, Config_Name
from app.forms import ArticleAdminForm
from app.db_manager.content_manager import filter_category_by_article, create_tag, filter_tag_by_name_list, \
    filter_tag_by_article
from app.manager.manager import update_one_to_many_relation_model, get_tag_for_choice
from app.app_models.other_model import Album
from app.app_models.config_model import Config
from app.app_models.content_model import Article, Category, ArticleCategory, ArticleTag, Tag
from tool.kblog_html import Tag as htag


@admin.register(Article)
class ArticleAdmin(MultipleChoiceAdmin):
    list_display = ['id', 'title', ]
    list_editable = ['title']
    form = ArticleAdminForm

    def get_object(self, request, object_id, from_field=None):
        obj = super().get_object(request, object_id, from_field)

        self.old_category = list(filter_category_by_article(obj.id))
        self.old_tag = list(filter_tag_by_article(obj.id))
        self.choice_field_value['category'] = [c.id for c in filter_category_by_article(obj.id)]
        self.choice_field_value['tag'] = ' '.join([t.name for t in self.old_tag])

        return obj

    def get_form(self, request, obj=None, **kwargs):
        return super().get_form(request, obj, **kwargs)

    def save_model(self, request, obj, form, change):
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

    def add_view(self, request, form_url='', extra_context=None):
        self.choice_field_value = {}
        self.old_category = []
        self.old_tag = []
        return super().add_view(request, form_url, extra_context)


@admin.register(Config)
class ConfigAdmin(admin.ModelAdmin):
    is_first = True
    list_display = ['name', 'id']
    fields = ['name', 'config', 'last_config']

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
        if obj.name == Config_Name['global_value']:
            cache.set(Global_value_cache_key, literal_eval(obj.config), 3600)
        return super().save_model(request, obj, form, change)

    def add_view(self, request, form_url='', extra_context=None):
        self.is_first = True
        self.config_bk = ''
        return super().add_view(request, form_url, extra_context)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


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
