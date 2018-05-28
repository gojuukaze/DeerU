from django import forms
from ktag.fields import TagField

from app.manager.manager import get_category_for_choice, get_tag_for_choice, get_category_for_category_form_choice
from app.app_models.content_model import Article, Comment, Category


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
