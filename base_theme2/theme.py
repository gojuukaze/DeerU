from pathlib import Path

from django.conf import settings
from django.template import Context, Template
from django.template.loader import get_template, render_to_string
from django.templatetags.static import static as static_url
from django.utils.safestring import mark_safe


class Static(object):
    """
    Static( ['base_theme2.css', ['base_theme2.css',{'media':'all'} ] ],
            ['jquery.css', ['jquery.css',{'defer': True} ] ],
            'template'
          )
    """
    def __init__(self, css, js):
        self.css = css
        self.js = js

    def append_css(self, c):
        self.css.append(c)

    def add_css(self, c):
        self.css += c

    def append_js(self, c):
        self.js.append(c)

    def add_js(self, c):
        self.js += c

    def get_css(self):
        base_css = {
            'rel': 'stylesheet',
            "type": 'text/css'
        }

        r = []
        for c in self.css:
            if isinstance(c, list) or isinstance(c, tuple):
                href = c[0]
                attrs = c[1]
            else:
                href = c
                attrs = {}
            attrs['href'] = href
            attrs.update(base_css)
            r.append(attrs)
        return r

    def get_js(self):
        base_js = {
            "type": 'text/javascript'
        }

        r = []
        for c in self.js:
            if isinstance(c, list) or isinstance(c, tuple):
                src = c[0]
                attrs = c[1]
            else:
                src = c
                attrs = {}
            attrs['src'] = src
            attrs.update(base_js)
            r.append(attrs)
        return r


class TemplatesMixin(object):
    template_context = {
        'head_begin_template': 'base_theme2/empty.html',
        'head_static_template': 'base_theme2/head_static.html',
        'head_end_template': 'base_theme2/empty.html',

        'body_begin_template': 'base_theme2/empty.html',

        'body_navbar_template': 'base_theme2/body_navbar.html',
        'body_navbar_left_template': 'base_theme2/body_navbar_left.html',
        'body_navbar_right_template': 'base_theme2/body_navbar_right.html',
        'body_navbar_menu_template': 'base_theme2/body_navbar_menu.html',

        'body_section_template': 'base_theme2/body_section.html',
        'body_section_content_begin_template': 'base_theme2/empty.html',
        'body_section_content_template': 'base_theme2/empty.html',
        'body_section_sidebar_template': 'base_theme2/empty.html',
        'body_section_content_end_template': 'base_theme2/empty.html',

        'body_footer_begin_template': 'base_theme2/empty.html',
        'body_footer_template': 'base_theme2/body_footer.html',
        'body_footer_end_template': 'base_theme2/empty.html',

        'body_end_template': 'base_theme2/empty.html',

    }
    ex_template_context = {}

    _updated = False

    def update_template_context(self):
        if self._updated:
            return
        self.template_context.update(self.ex_template_context)

        for k, v in settings.BASE_THEME2_TEMPLATES.items():
            if k in self.template_context:
                self.template_context[k] = v

        self._updated = True

    def get_template_context(self):
        self.update_template_context()

        return self.template_context


class Theme(TemplatesMixin):
    head_title = ''
    template = 'base_theme2/base2.html'

    ex_context = {}

    def __init__(self, config, extend_data=None):
        super(Theme, self).__init__()
        if extend_data is None:
            extend_data = {}
        self.config = config
        self.extend_data = extend_data

    def _static(self):
        css = [
            'https://cdn.staticfile.org/bulma/0.9.1/css/bulma.min.css',
            (static_url('/base_theme2/css/base_theme2.css'), {'media': 'all'})
        ]
        js = [
            ('https://cdn.staticfile.org/font-awesome/5.11.2/js/all.min.js', {'defer': True}),
            'https://cdn.staticfile.org/jquery/3.5.1/jquery.min.js'
        ]
        return Static(css, js)

    def static(self):
        return self._static()

    def get_context(self):
        static = self.static()

        context = {
            'config': self.config,
            'head_title': self.head_title or self.config['v2_blog_config']['title'],
            'css': static.get_css(),
            'js': static.get_js(),
            'extend_data': self.extend_data
        }

        context.update(self.get_template_context())
        context.update(self.ex_context)

        return context

    def get_html(self, request):
        return render_to_string(self.template, context=self.get_context(), request=request)


class HomeTemplate(Theme):
    ex_template_context = {
        'article_list_template': 'base_theme2/article_list.html',
        'article_list_breadcrumb_template': 'base_theme2/article_list_breadcrumb.html',
        'article_list_item_template': 'base_theme2/article_list_item.html',
        'article_list_empty_item_template': 'base_theme2/article_list_empty_item.html',

        'article_list_sidebar_template': 'base_theme2/body_section_sidebar.html',
    }

    def __init__(self, config, article_list, paginator, breadcrumbs, extend_data):
        super(HomeTemplate, self).__init__(config, extend_data=extend_data)
        self.article_list = article_list
        self.ex_context = {
            'article_list': article_list,
            'paginator': paginator,
            'breadcrumbs': breadcrumbs,
        }

        self.ex_template_context['body_section_content_template'] = self.ex_template_context[
            'article_list_template']
        self.ex_template_context['body_section_sidebar_template'] = self.ex_template_context[
            'article_list_sidebar_template']


class DetailArticleTemplate(Theme):
    ex_template_context = {
        'detail_article_template': 'base_theme2/detail_article.html',
        'detail_article_content_template': 'base_theme2/detail_article_content.html',
        'detail_article_comment_template': 'base_theme2/detail_article_comment.html',

        'detail_article_sidebar_template': 'base_theme2/body_section_sidebar.html',
    }

    def __init__(self, config, article, comment_form, form_error, extend_data):
        super(DetailArticleTemplate, self).__init__(config, extend_data=extend_data)
        self.article = article
        self.head_title = '%s |%s' % (article.title, self.config['v2_blog_config']['title'])

        self.ex_context = {
            'article': article,
            'comment_form': comment_form,
            'form_error': form_error
        }

        self.ex_template_context['body_section_content_template'] = self.ex_template_context[
            'detail_article_template']
        self.ex_template_context['body_section_sidebar_template'] = self.ex_template_context[
            'detail_article_sidebar_template']

    def static(self):
        static = super(DetailArticleTemplate, self).static()
        static.add_css([
            static_url('/base_theme2/css/jodit.es2018.min.css'),
            'https://cdn.staticfile.org/froala-editor/2.9.5/css/froala_style.min.css',

        ])
        static.add_js([
            static_url('/base_theme2/js/jodit.es2018.min.js'),
            static_url('/base_theme2/js/comment-editor.js'),
            'https://cdn.staticfile.org/layer/3.1.1/layer.js',
            'https://cdn.staticfile.org/clipboard.js/2.0.1/clipboard.min.js',
            'https://cdn.staticfile.org/jquery.qrcode/1.0/jquery.qrcode.min.js'
        ])
        return static


class DetailFlatpageTemplate(Theme):
    ex_template_context = {
        'detail_flatpage_template': 'base_theme2/detail_flatpage.html',

        'detail_flatpage_sidebar_template': 'base_theme2/body_section_sidebar.html',
    }

    def __init__(self, config, flatpage, extend_data):
        super(DetailFlatpageTemplate, self).__init__(config, extend_data=extend_data)
        self.head_title = '%s |%s' % (flatpage.title, self.config['v2_blog_config']['title'])

        self.ex_context = {
            'flatpage': flatpage,
        }

        self.ex_template_context['body_section_content_template'] = self.ex_template_context[
            'detail_flatpage_template']
        self.ex_template_context['body_section_sidebar_template'] = self.ex_template_context[
            'detail_flatpage_sidebar_template']

    def static(self):
        static = super(DetailFlatpageTemplate, self).static()
        static.append_css('https://cdn.staticfile.org/froala-editor/2.9.5/css/froala_style.min.css')

        return static


class Page404Template(Theme):
    ex_template_context = {
        '404_template': 'base_theme2/404.html',
        '404_sidebar_template': 'base_theme2/empty.html',

    }

    def __init__(self, config, extend_data):
        super(Page404Template, self).__init__(config, extend_data=extend_data)
        self.head_title = '404 not found |%s' % self.config['v2_blog_config']['title']

        self.ex_template_context['body_section_content_template'] = self.ex_template_context[
            '404_template']
        self.ex_template_context['body_section_sidebar_template'] = self.ex_template_context[
            '404_sidebar_template']
