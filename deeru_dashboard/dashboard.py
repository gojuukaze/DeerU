from django.urls import reverse
from jet.dashboard import modules
from jet.dashboard.dashboard import Dashboard

from deeru_dashboard.dashboard_modules import CountModule, CommentModule


class CustomIndexDashboard(Dashboard):

    columns = 2

    def init_with_context(self, context):
        self.children.append(CountModule('统计', column=0, order=0))

        self.children.append(modules.LinkList(
            '快捷操作',
            children=[
                {
                    'title': '博客首页',
                    'url': '/',
                    'external': True,
                },
                {
                    'title': '创建文章',
                    'url': reverse('admin:app_article_add'),
                    'external': True,
                },
                {
                    'title': 'DeerU - 开源博客框架',
                    'url': 'https://github.com/gojuukaze/DeerU',
                    'external': True,
                },
            ],
            column=0,
            order=1
        ))

        self.children.append(CommentModule('待审核评论', column=0, order=2))

        self.children.append(modules.RecentActions('操作记录', 10, column=1, order=1))
