from django import forms
from django.db.models import TextField
import json
from ast import literal_eval
from django.utils.safestring import mark_safe
from codemirror import CodeMirrorTextarea


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
                       'https://cdn.bootcss.com/codemirror/5.36.0/theme/mdn-like.min.css',
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
                    theme: "mdn-like",
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


class ConfigField(TextField):
    def to_python(self, value):
        value = super().to_python(value)
        if not value:
            return value
        value = literal_eval(value)
        return json.dumps(value, ensure_ascii=False, indent=4)

    def formfield(self, **kwargs):
        defaults = {'widget': ConfigWidget,
                    'max_length': self.max_length}
        defaults.update(kwargs)
        defaults['widget'] = ConfigWidget
        return super(TextField, self).formfield(**defaults)
