from pprint import pprint

from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.views.generic import ListView, DetailView
from django.views.generic.base import ContextMixin

from app.db_manager.content_manager import filter_article_order_by_id, get_article_by_id, filter_article_by_category, \
    get_category_by_id, filter_article_by_tag, get_article_meta_by_article, get_tag_by_id, \
    filter_valid_comment_by_article, \
    get_flatpage_by_id
from app.forms import CommentForm
from app.manager import get_base_context
from app.manager.config_manager import get_theme
from app.manager.content_manager import get_flatpage_url_dict

from app.ex_paginator import DeerUPaginator


class DeerUContextMixin(ContextMixin):
    theme = 'base_theme'

    def get_context_data(self, **kwargs):
        """
        Add context data to the template.

        Args:
            self: (todo): write your description
        """
        context = super().get_context_data(**kwargs)
        get_base_context(context)
        self.theme = context['config']['v2_blog_config']['theme']

        return context


class ArticleList(ListView):
    paginator = None
    allow_empty = True

    def _get_paginator(self, page):
        """
        Return the paginator.

        Args:
            self: (todo): write your description
            page: (str): write your description
        """
        pass

    def get_queryset(self):
        """
        Return the list of pagyset.

        Args:
            self: (todo): write your description
        """
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
        """
        Returns the context data to the template.

        Args:
            self: (todo): write your description
        """
        context = super().get_context_data(**kwargs)
        # context['top_menu'] = get_top_menu()
        # context['global_value'] = get_global_value()
        # context['aside_category'] = get_aside_category()
        context['paginator'] = self.paginator
        return context


class Home(ArticleList, DeerUContextMixin):
    # template_name = theme + '/home.html'
    context_object_name = 'article_list'

    def get_template_names(self):
        """
        Returns a list of template names.

        Args:
            self: (todo): write your description
        """
        return self.theme + '/home.html'

    def _get_paginator(self, page):
        """
        Get paginator for paginator.

        Args:
            self: (todo): write your description
            page: (str): write your description
        """
        per_page = int(self.request.GET.get('per_page', 7))
        self.paginator = DeerUPaginator(filter_article_order_by_id(), per_page, page)
        return self.paginator


class DetailArticle(DetailView, DeerUContextMixin):
    # template_name = theme + '/detail_article.html'
    context_object_name = 'article'

    def get_template_names(self):
        """
        Returns a list of template names.

        Args:
            self: (todo): write your description
        """
        return self.theme + '/detail_article.html'

    def get_object(self, queryset=None):
        """
        Returns an object by queryset.

        Args:
            self: (todo): write your description
            queryset: (str): write your description
        """
        try:
            article_meta = get_article_meta_by_article(self.kwargs['article_id'])
            article_meta.read_num += 1
            article_meta.save()
        except:
            raise Http404()

        return get_article_by_id(self.kwargs['article_id'])

    def get_context_data(self, **kwargs):
        """
        Returns the context data to provide to the template.

        Args:
            self: (todo): write your description
        """
        context = super().get_context_data(**kwargs)
        context['comments'] = filter_valid_comment_by_article(self.kwargs['article_id'])
        context['comment_form'] = CommentForm()
        context['form_error'] = self.request.GET.get('form_error', '')
        return context


class CategoryArticle(ArticleList, DeerUContextMixin):
    # template_name = theme + '/category.html'
    context_object_name = 'article_list'

    def get_template_names(self):
        """
        Returns a list of template names.

        Args:
            self: (todo): write your description
        """
        return self.theme + '/category.html'

    def _get_paginator(self, page):
        """
        Return paginated paginator

        Args:
            self: (todo): write your description
            page: (str): write your description
        """
        category_id = self.kwargs['category_id']
        per_page = int(self.request.GET.get('per_page', 7))
        self.paginator = DeerUPaginator(filter_article_by_category(category_id).order_by('-id'), per_page, page)
        return self.paginator

    def get_context_data(self, **kwargs):
        """
        Returns the context data to provide to the template.

        Args:
            self: (todo): write your description
        """
        category_id = self.kwargs['category_id']
        context = super().get_context_data(**kwargs)
        category = get_category_by_id(category_id)
        if not category:
            raise Http404()
        context['category'] = category
        return context


class TagArticle(ArticleList, DeerUContextMixin):
    # template_name = theme + '/tag.html'
    context_object_name = 'article_list'

    def get_template_names(self):
        """
        Returns a list of template names.

        Args:
            self: (todo): write your description
        """
        return self.theme + '/tag.html'

    def _get_paginator(self, page):
        """
        Return paginator for paginator.

        Args:
            self: (todo): write your description
            page: (str): write your description
        """
        tag_id = self.kwargs['tag_id']
        per_page = int(self.request.GET.get('per_page', 7))
        self.paginator = DeerUPaginator(filter_article_by_tag(tag_id).order_by('-id'), per_page, page)
        return self.paginator

    def get_context_data(self, **kwargs):
        """
        Add the context data to the template.

        Args:
            self: (todo): write your description
        """
        tag_id = self.kwargs['tag_id']
        context = super().get_context_data(**kwargs)
        tag = get_tag_by_id(tag_id)
        if not tag:
            raise Http404()
        context['tag'] = tag
        return context


class DetailFlatPage(DetailView, DeerUContextMixin):
    # template_name = theme + '/detail_flatpage.html'
    context_object_name = 'flatpage'

    def get_template_names(self):
        """
        Returns a list of template names.

        Args:
            self: (todo): write your description
        """
        return self.theme + '/detail_flatpage.html'

    def get_object(self, queryset=None):
        """
        Return the object by queryset.

        Args:
            self: (todo): write your description
            queryset: (str): write your description
        """
        urld = get_flatpage_url_dict()
        try:
            page_id = urld[self.kwargs['url']]
        except:
            raise Http404()

        return get_flatpage_by_id(page_id)

    def get_context_data(self, **kwargs):
        """
        Add the context data to the template.

        Args:
            self: (todo): write your description
        """
        context = super().get_context_data(**kwargs)
        return context
