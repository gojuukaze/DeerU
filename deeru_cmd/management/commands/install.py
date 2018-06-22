# -*- coding:utf-8 -*-
import os
import platform

from django.core.management import CommandError

from deeru_cmd.management.base import DeerUBaseCommand


class Command(DeerUBaseCommand):
    """
    用来临时跑一些东西
    python manage.py install
    """

    def add_arguments(self, parser):
        parser.description = '''安装下载DeerU项目、插件、项目'''

        parser.add_argument('type', type=str, choices=['project', 'plugin', 'theme'], help='安装的类型')
        parser.add_argument('name', type=str, help='名称')

        parser.add_argument(
            '--mode',
            default='git',
            dest='mode',
            choices=['git', 'pip'],
            help='用什么方式下载，git：从git仓库下载；pip：从pypi仓库下载。下载DeerU项目默认为git',
        )

        parser.add_argument(
            '--branch',
            default='master',
            dest='branch',
            help='从哪个分支下载，mode为pip时无效',
        )

    def install_project(self):
        self.info('开始安装DeerU')
        # 环境检测
        if not platform.python_version().startswith('3'):
            self.error('python版本必须3+，当前版本:' + platform.python_version())
            return
        # if 'windows' in platform.system().lower():
        #     print('windows 不支持自动安装')

        self.info('下载DeerU...')
        if os.path.exists(self.name):
            self.info('已存在相同目录 "%s" ,请选择: d(删除目录); s(跳过下载);  ')
            s = input()
            if s == 'd':
                os.rmdir(self.name)
            elif s == 's':
                pass
            else:
                raise CommandError('输入错误')

        code = os.system('git clone -b %s https://github.com/gojuukaze/DeerU.git' % self.branch)
        if code != 0:
            raise CommandError('\n下载DeerU失败，检测是否能正常连接github')
        self.info('安装依赖...')
        code = os.system('cd %s && pip install -r requirements.txt'%self.name)
        if code != 0:
            raise CommandError('\n安装依赖失败，检测pypi源是否有')
        else:
            self.success('\n安装完成 ！！')

    def handle(self, *args, **options):
        self.type = options['type']
        self.name = options['name']
        self.branch = options['branch']
        self.mode = options['mode']
