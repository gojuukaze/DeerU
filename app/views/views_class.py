from django.contrib.sitemaps import Sitemap
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.views.generic import ListView, DetailView
from django.views.generic.base import ContextMixin

from app.db_manager.content_manager import filter_article_order_by_id, get_article_by_id, filter_article_by_category, \
    get_category_by_id, filter_article_by_tag, get_article_meta_by_article, get_tag_by_id, filter_comment_by_article
from app.forms import CommentForm
from app.manager import get_base_context
from app.manager.config_manager import get_global_value, get_theme_config
from app.manager.uiconfig_manager import get_top_menu, get_aside_category, get_aside_tags, get_top_ico, \
    get_aside_category2
from app.ex_paginator import DeerUPaginator





class DeerUContextMixin(ContextMixin):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        get_base_context(context)

        return context


class ArticleList(ListView):
    paginator = None
    allow_empty = True

    def _get_paginator(self, page):
        pass

    def get_queryset(self):
        page = int(self.request.GET.get('page', 1))
        if self.paginator:
            paginator = self.paginator
        else:
            paginator = self._get_paginator(page)
        if page < 1:
            page = 1
        if page > paginator.end_index:
            page = paginator.end_index
        self.page = page
        return paginator.page(page).object_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['top_menu'] = get_top_menu()
        # context['global_value'] = get_global_value()
        # context['aside_category'] = get_aside_category()
        context['paginator'] = self.paginator
        return context


class Home(ArticleList,DeerUContextMixin):
    template_name = 'base_theme/home.html'
    context_object_name = 'article_list'

    def _get_paginator(self, page):
        self.paginator = DeerUPaginator(filter_article_order_by_id(), 7, page)
        return self.paginator


class DetailArticle(DetailView,DeerUContextMixin):
    template_name = 'base_theme/detail_article.html'
    context_object_name = 'article'

    def get_object(self, queryset=None):
        try:
            article_meta = get_article_meta_by_article(self.kwargs['article_id'])
            article_meta.read_num += 1
            article_meta.save()

        except ObjectDoesNotExist:
            raise Http404()

        return get_article_by_id(self.kwargs['article_id'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = filter_comment_by_article(self.kwargs['article_id'])
        context['comment_form'] = CommentForm()
        context['form_error'] = self.request.GET.get('form_error', '')
        return context


class CategoryArticle(ArticleList,DeerUContextMixin):
    template_name = 'base_theme/category.html'
    context_object_name = 'article_list'

    def _get_paginator(self, page):
        category_id = self.kwargs['category_id']
        self.paginator = DeerUPaginator(filter_article_by_category(category_id).order_by('-id'), 7, page)
        return self.paginator

    def get_context_data(self, **kwargs):
        category_id = self.kwargs['category_id']
        context = super().get_context_data(**kwargs)
        category = get_category_by_id(category_id)
        if not category:
            raise Http404()
        context['category'] = category
        return context


class TagArticle(ArticleList,DeerUContextMixin):
    template_name = 'base_theme/tag.html'
    context_object_name = 'article_list'

    def _get_paginator(self, page):
        tag_id = self.kwargs['tag_id']
        self.paginator = DeerUPaginator(filter_article_by_tag(tag_id).order_by('-id'), 7, page)
        return self.paginator

    def get_context_data(self, **kwargs):
        tag_id = self.kwargs['tag_id']
        context = super().get_context_data(**kwargs)
        tag = get_tag_by_id(tag_id)
        if not tag:
            raise Http404()
        context['tag'] = tag
        return context


class DetailFlatPage(DetailView,DeerUContextMixin):
    template_name = 'base_theme/detail_article.html'
    context_object_name = 'article'

    def get_object(self, queryset=None):
        self.kwargs['article_id'] = self.kwargs['url']
        try:
            article_meta = get_article_meta_by_article(self.kwargs['url'])
            article_meta.read_num += 1
            article_meta.save()

        except ObjectDoesNotExist:
            raise Http404()

        return get_article_by_id(self.kwargs['url'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = filter_comment_by_article(self.kwargs['url'])
        context['comment_form'] = CommentForm()
        context['form_error'] = self.request.GET.get('form_error', '')
        return context
