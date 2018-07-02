import re
import traceback
from ast import literal_eval

from django import forms
from django.utils.safestring import mark_safe
from django.utils.translation import gettext, gettext_lazy as _

from ktag.fields import TagField

from app.app_models.config_model import Config
from app.consts import app_config_context
from app.manager.ct_manager import get_category_for_choice, get_tag_for_choice, get_category_for_category_form_choice
from app.app_models.content_model import Article, Comment, Category, FlatPage


class ArticleAdminForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'

    is_use_cover_img = forms.BooleanField(label='是否使用自定义封面图片', initial=True)
    cover_img = forms.CharField(label='封面图片', max_length=150, required=False)
    is_use_cover_summary = forms.BooleanField(label='是否使用自定义简介', required=False)

    cover_summary = forms.CharField(label='封面简介', max_length=200, required=False, help_text='为空将自动自取',
                                    widget=forms.Textarea(attrs={'rows': '4', 'cols': '55'}), )

    category = forms.MultipleChoiceField(label='分类', choices=get_category_for_choice)
    tag = TagField(label='标签', delimiters=' ', help_text="输入标签，用空格分隔", data_list=get_tag_for_choice, required=False)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'


class CategoryAdminForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

    father_id = forms.ChoiceField(label='父级目录', choices=get_category_for_category_form_choice, initial=-1)

    def is_valid(self):
        result = super().is_valid()
        if not result:
            return result
        if int(self.cleaned_data['father_id']) == self.instance.id:
            self.add_error('father_id', '父目录不能是自己')
            return False
        return True


class ConfigAdminForm(forms.ModelForm):
    class Meta:
        model = Config
        fields = '__all__'

    required_keys = {
        app_config_context['top_ico']: {'left', 'right'},
        app_config_context['global_value']: {'title', 'blog_name', 'nickname'},
        app_config_context['common_config']: {'theme'},
    }

    def check_bool(self, config):
        """
        检测bool值
        :return:
        """
        msg = '检测到bool值，请使用0,1代替'
        if re.search(r':\s*true\s*[,}]', config):
            raise forms.ValidationError(msg)
        if re.search(r':\s*True\s*[,}]', config):
            raise forms.ValidationError(msg)
        if re.search(r':\s*false\s*[,}]', config):
            raise forms.ValidationError(msg)
        if re.search(r':\s*False\s*[,}]', config):
            raise forms.ValidationError(msg)

    def check_keys(self, config):
        """
        检测必须的配置项
        :param config:
        :return:
        """
        name = self.cleaned_data['name']
        keys = self.required_keys.get(name)
        if not keys:
            return

        diff = keys.difference(set(config.keys()))
        if diff:
            raise forms.ValidationError('缺少必须项 : ' + str(diff))

    def clean_config(self):
        config = self.cleaned_data['config']
        self.check_bool(config)
        try:
            temp = literal_eval(config)
        except:
            s = traceback.format_exc(1)
            # s = s.replace('\n', '<br>')
            s = s.replace('<', '&lt;')
            s = s.replace('>', '&gt;')

            s = s.strip().split('\n')
            s = '<br>'.join(s[3:-1])
            s = s.replace(' ', '&nbsp;')

            # s = '[语法错误] %s -- %s' % (s[3].split(',')[1].strip(), s[4].strip())
            s = '【语法错误】<br>' + s
            s = mark_safe(s)
            raise forms.ValidationError(s)
        self.check_keys(temp)

        return config


class FlatpageAdminForm(forms.ModelForm):
    url = forms.RegexField(
        label='url',
        max_length=100,
        regex=r'^[-\w/\.~]+$',
        help_text="如: '/about/contact/' ，最终url为你设置的前缀+url ",
        error_messages={
            "invalid": _(
                "This value must contain only letters, numbers, dots, "
                "underscores, dashes, slashes or tildes."
            ),
        },
    )

    class Meta:
        model = FlatPage
        fields = '__all__'

    def clean_url(self):
        url = self.cleaned_data['url']
        if not url.startswith('/'):
            raise forms.ValidationError(
                gettext("URL is missing a leading slash."),
                code='missing_leading_slash',
            )

        return url

    def clean(self):
        url = self.cleaned_data.get('url')

        same_url = FlatPage.objects.filter(url=url)
        if self.instance.pk:
            same_url = same_url.exclude(pk=self.instance.pk)

        if same_url.exists():
            raise forms.ValidationError(
               _('存在相同的url  %(url)s'),
                code='duplicate_url',
                params={'url': url},
            )

        return super().clean()
