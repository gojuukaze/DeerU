from django.db.models import Sum, Count
from jet.dashboard.modules import DashboardModule

from app.consts import CommentStatusChoices
from app.db_manager.content_manager import all_article, all_comment, all_flatpage, filter_created_comment


class CountModule(DashboardModule):
    template = 'deeru_dashboard/count.html'

    def __init__(self, title=None, **kwargs):
        """
        Initialize the title.

        Args:
            self: (todo): write your description
            title: (str): write your description
        """
        super().__init__(title, **kwargs)

    def init_with_context(self, context):
        """
        Initialize the article.

        Args:
            self: (todo): write your description
            context: (dict): write your description
        """
        article_count = all_article().count()
        comment_count = all_comment().count()
        flatpage_count = all_flatpage().count()

        self.children = [[article_count, '文章数'],
                         [comment_count, '评论数'],
                         [flatpage_count, '单页面数']]


class CommentModule(DashboardModule):
    template = 'deeru_dashboard/comment.html'

    def __init__(self, title=None, **kwargs):
        """
        Initialize the title.

        Args:
            self: (todo): write your description
            title: (str): write your description
        """
        super().__init__(title, **kwargs)

    def init_with_context(self, context):
        """
        Initialize the context with the given context.

        Args:
            self: (todo): write your description
            context: (dict): write your description
        """
        comments = filter_created_comment().order_by('-id')[:10]

        self.children = list(comments)
