from django import forms
from ktag.fields import TagField

from app.manager.manager import get_category_for_choice, get_tag_for_choice
from app.app_models.content_model import Article, Comment


class ArticleAdminForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'

    category = forms.MultipleChoiceField(label='分类', choices=get_category_for_choice)
    tag = TagField(label='标签', delimiters=' ', help_text="输入标签，用空格分隔", data_list=get_tag_for_choice, required=False)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'

