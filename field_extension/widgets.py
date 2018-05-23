import json

from django.conf import settings
from django.forms import Media, SelectMultiple
from django.urls import reverse, NoReverseMatch
from froala_editor import PLUGINS_WITH_CSS
from froala_editor.widgets import FroalaEditor


class KFroalaEditor(FroalaEditor):
    # template_name = 'froala_k_textarea.html'

    def trigger_froala(self, el_id, options):

        str = """
        <script>
            $(function(){
                $('#%s').froalaEditor(%s)
            });
        </script>""" % (el_id, options)
        return str

    def _media(self):
        css = {
            'all': ('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.4.0/css/font-awesome.min.css',
                    'froala_editor/css/froala_editor.min.css', 'froala_editor/css/froala_style.min.css',
                    'froala_editor/css/froala-django.css')
        }
        js = ('froala_editor/js/froala_editor.min.js', 'froala_editor/js/froala-django.js',)

        if self.include_jquery:
            js = ('https://cdn.bootcss.com/jquery/3.3.1/jquery.min.js',) + js

        if self.theme:
            css['all'] += ('froala_editor/css/themes/' + self.theme + '.css',)

        if self.language:
            js += ('froala_editor/js/languages/' + self.language + '.js',)

        for plugin in self.plugins:
            js += ('froala_editor/js/plugins/' + plugin + '.min.js',)
            if plugin in PLUGINS_WITH_CSS:
                css['all'] += ('froala_editor/css/plugins/' + plugin + '.min.css',)

        return Media(css=css, js=js)

    media = property(_media)

