import json

from django import forms
from django.utils.safestring import mark_safe


class ConfigWidget(forms.Textarea):
    class Media:
        js = ['https://cdn.staticfile.org/jquery/3.4.1/jquery.min.js',
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
        print('--', name)
        print('==', value)

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


class ConfigWidgetV2(forms.Textarea):

    def render(self, name, value, attrs=None, renderer=None):
        value = json.loads(value)
        id = value['_id']
        value.pop('_id')
        value = json.dumps(value)
        html = super().render(name, value, attrs)
        el_id = self.build_attrs(attrs).get('id')

        html += '''
        <script>
        django.jQuery(function(){
         django.jQuery('#%s').parent().append('<iframe src="/config/%s/html"  style="width: 100%%;border: none" scrolling="no"></iframe>');
         django.jQuery('#%s').hide();
         django.jQuery("[for$='id_v2_config']").hide();
         });
        function onConfigChange(s){
         django.jQuery('#%s').text(s);
        }
        function onHeightChange(h){
        django.jQuery('iframe').height(h);
        }
        </script>
        
        ''' % (el_id, id, el_id, el_id)

        return mark_safe(html)
