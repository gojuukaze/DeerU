import json

from django import forms
from django.conf import settings
from django.forms import Media, SelectMultiple
from django.urls import reverse, NoReverseMatch
from django.utils.safestring import mark_safe
from froala_editor import PLUGINS_WITH_CSS
from froala_editor.widgets import FroalaEditor


class MFroalaEditor(FroalaEditor):
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


class ConfigWidget(forms.Textarea):
    class Media:
        js = ['https://cdn.bootcss.com/jquery/3.3.1/jquery.min.js',
              'https://cdn.bootcss.com/codemirror/5.36.0/codemirror.min.js',
              'https://cdn.bootcss.com/codemirror/5.36.0/mode/python/python.min.js',
              'https://cdn.bootcss.com/codemirror/5.36.0/addon/fold/foldgutter.min.js',
              'https://cdn.bootcss.com/codemirror/5.36.0/addon/fold/foldcode.min.js',
              'https://cdn.bootcss.com/codemirror/5.36.0/addon/fold/brace-fold.min.js',
              'https://cdn.bootcss.com/codemirror/5.36.0/addon/fold/comment-fold.min.js',
              'https://cdn.bootcss.com/codemirror/5.36.0/addon/edit/matchbrackets.min.js',
              'https://cdn.bootcss.com/codemirror/5.36.0/addon/fold/indent-fold.js',
              ]
        css = {'all': ['https://cdn.bootcss.com/codemirror/5.36.0/codemirror.min.css',
                       'https://cdn.bootcss.com/codemirror/5.36.0/addon/fold/foldgutter.min.css',
                       'https://cdn.bootcss.com/codemirror/5.36.0/base_theme/mdn-like.min.css',
                       ]}

    def render(self, name, value, attrs=None, renderer=None):
        html = super().render(name, value, attrs)
        el_id = self.build_attrs(attrs).get('id')

        html += """
        <script>
        $(function(){
        var myTextarea = document.getElementById('%s');
        var w=myTextarea.offsetWidth;
        var h=myTextarea.offsetHeight;
        var cm = CodeMirror.fromTextArea(myTextarea, {
                    mode: "python",
                    lineNumbers: true,
                    smartIndent: true,
                    indentUnit:4,
                    base_theme: "mdn-like",
                    matchBrackets: true,	//括号匹配
                    lineWrapping:true,
         foldGutter: true,
    gutters: ["CodeMirror-linenumbers", "CodeMirror-foldgutter"]
                    
            });
        //cm.setSize(w+'px',h+'px');
        }
        );
        </script>
        """ % el_id
        return mark_safe(html)