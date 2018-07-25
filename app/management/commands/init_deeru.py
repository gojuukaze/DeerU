import os
import sys
import traceback
from getpass import getpass
from pprint import pprint
from django.core import management

from django.contrib.auth.models import User, UserManager
from django.core.management import BaseCommand
from django.core.management.base import OutputWrapper, CommandError

from app.app_models.config_model import Config
from app.app_models.content_model import Article, Category, Tag, ArticleMeta, ArticleCategory, ArticleTag, Comment
from app.manager.config_manager import cache_config
from app.manager.ct_manager import update_one_to_many_relation_model
from tool.datetime_helper import str_to_datetime, now


class Command(BaseCommand):
    """
    初始化

    python manage.py init_deeru

    """

    def handle(self, *args, **options):
        self.error = self.stderr.write

        info_out = OutputWrapper(sys.stdout)
        info_out.style_func = self.style.WARNING
        self.info = info_out.write

        success_out = OutputWrapper(sys.stdout)
        success_out.style_func = self.style.SUCCESS
        self.success = success_out.write

        self.info("初始化中：")
        try:
            os.mkdir('log')
        except:
            pass
        with open('./log/init.log', 'a', encoding='utf-8')as f:
            f.write('开始初始化(%s)\n' % str(now()))

        # ============

        self.info('初始化数据库 ... ')

        with open('./log/init.log', 'a', encoding='utf-8')as f:
            f.write('初始化数据库\n')
            try:

                management.call_command('migrate', stdout=f)
                # management.call_command('makemigrations', 'app', stdout=f)
            except:

                traceback.print_exc(file=f)
                self.error('初始化数据库 ... [失败]，更多信息查看 ./log/init.log ')
                raise

        self.success('初始化数据库 ... [完成]')

        # ============

        self.info('初始化静态文件 ... ')
        with open('./log/init.log', 'a', encoding='utf-8')as f:
            f.write('初始化静态文件\n')
            try:
                management.call_command('collectstatic', '--noinput', stdout=f)
            except:
                traceback.print_exc(file=f)
                self.error('初始化静态文件 ... [失败]，更多信息查看 ./log/init.log ')
                raise

        self.success('初始化静态文件 ... [完成]')

        # ============

        self.info('创建管理员账户 ... ')

        username = input('输入管理账户登录名（默认：admin）：')
        if not username:
            username = 'admin'
        password = getpass('输入密码（默认：123456）：')
        if not password:
            password = '123456'
        with open('./log/init.log', 'a', encoding='utf-8')as f:
            try:
                flag = True
                User._default_manager.db_manager('default').create_superuser(username, None, password)

            except:
                flag = False
                traceback.print_exc(3)

                traceback.print_exc(file=f)
                self.error('创建管理员账户 ... [失败]，更多信息查看 ./log/init.log ')


            finally:
                if not flag:
                    return

        # ============
        self.success('创建管理员账户 ... [完成]')

        self.success('\n初始化完成 ！！')
