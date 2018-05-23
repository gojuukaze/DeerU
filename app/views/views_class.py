from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.views.generic import ListView, DetailView

from app.db_manager.content_manager import filter_article_order_by_id, get_article_by_id, filter_article_by_category, \
    get_category_by_id, filter_article_by_tag, get_article_meta_by_article, get_tag_by_id, filter_comment_by_article
from app.forms import CommentForm
from app.manager.config_manager import get_global_value
from app.manager.uiconfig_manager import get_top_menu, get_aside_category, get_aside_tags, get_top_ico
from tool.kblog_paginator import kblogPaginator


def get_base_data(context):
    context['top_menu'] = get_top_menu()
    context['global_value'] = get_global_value()
    context['aside_category'] = get_aside_category()
    context['aside_tags'] = get_aside_tags()
    context['top_ico'] = get_top_ico()

    return context


class ArticleList(ListView):
    paginator = None
    allow_empty = True

    def _get_paginator(self):
        pass

    def get_queryset(self):
        page = int(self.request.GET.get('page', 1))
        if self.paginator:
            paginator = self.paginator
        else:
            paginator = self._get_paginator()
        if page < 1:
            page = 1
        if page > paginator.end_index:
            page = paginator.end_index
        self.page = page
        return paginator.page(page).object_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        get_base_data(context)
        # context['top_menu'] = get_top_menu()
        # context['global_value'] = get_global_value()
        # context['aside_category'] = get_aside_category()
        context['page_list'] = self.paginator.get_page_html_list(self.page)
        return context


class Home(ArticleList):
    template_name = 'base_theme/home.html'
    context_object_name = 'article_list'

    def _get_paginator(self):
        self.paginator = kblogPaginator(filter_article_order_by_id(), 7)
        return self.paginator


class DetailArticle(DetailView):
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
        get_base_data(context)
        context['comments'] = filter_comment_by_article(self.kwargs['article_id'])
        context['comment_form'] = CommentForm()
        context['form_error'] = self.request.GET.get('form_error', '')
        return context


class CategoryArticle(ArticleList):
    template_name = 'base_theme/category.html'
    context_object_name = 'article_list'

    def _get_paginator(self):
        category_id = self.kwargs['category_id']
        self.paginator = kblogPaginator(filter_article_by_category(category_id).order_by('-id'), 7)
        return self.paginator

    def get_context_data(self, **kwargs):
        category_id = self.kwargs['category_id']
        context = super().get_context_data(**kwargs)
        category = get_category_by_id(category_id)
        if not category:
            raise Http404()
        context['category'] = category
        return context


class TagArticle(ArticleList):
    template_name = 'base_theme/tag.html'
    context_object_name = 'article_list'

    def _get_paginator(self):
        tag_id = self.kwargs['tag_id']
        self.paginator = kblogPaginator(filter_article_by_tag(tag_id).order_by('-id'), 7)
        return self.paginator

    def get_context_data(self, **kwargs):
        tag_id = self.kwargs['tag_id']
        context = super().get_context_data(**kwargs)
        tag = get_tag_by_id(tag_id)
        if not tag:
            raise Http404()
        context['tag'] = tag
        return context
