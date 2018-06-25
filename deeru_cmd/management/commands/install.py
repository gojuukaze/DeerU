# -*- coding:utf-8 -*-
import os
import platform
import shutil
import subprocess
from django.core.management import CommandError

from deeru_cmd.management.base import DeerUBaseCommand


class Command(DeerUBaseCommand):
    """
    用来临时跑一些东西
    python manage.py install
    """

    def add_arguments(self, parser):
        parser.description = '''安装下载DeerU项目、插件、主题'''

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

    def get_git_url(self):
        if self.type == 'project':
            return 'https://github.com/gojuukaze/DeerU.git'

    def download(self):
        if self.mode == 'git':
            url = self.get_git_url()
            result = subprocess.run('git clone -b %s %s %s' % (url, self.branch, self.name), shell=True)
            return result

    def install_project(self):
        self.info('开始安装DeerU')
        # 环境检测
        if not platform.python_version().startswith('3'):
            raise CommandError('python版本必须3+，当前版本:' + platform.python_version())
        # if 'windows' in platform.system().lower():
        #     print('windows 不支持自动安装')

        self.info('下载DeerU（使用git模式）...')
        s = ''
        if os.path.exists(self.name):
            # self.info('已存在相同目录 "%s" ,请选择: d(删除已存在目录); s(跳过下载) ' % self.name)
            s = input('已存在相同目录 "%s" ,请选择: d(删除已存在目录); s(跳过下载) ' % self.name)
            if s == 'd':
                shutil.rmtree(self.name)
            elif s == 's':
                pass
            else:
                raise CommandError('输入错误')
        if s != 's':
            result = self.download()
            if result.returncode != 0:
                raise CommandError('\n下载DeerU失败')

        self.info('安装依赖...')
        result = subprocess.run('pip install -r requirements.txt', cwd=self.name, shell=True)
        if result.returncode != 0:
            raise CommandError('\n安装依赖失败')

        self.success('\n安装完成 ！！')

    def handle(self, *args, **options):
        self.type = options['type']
        self.name = options['name']
        self.branch = options['branch']
        self.mode = options['mode']

        if self.type == 'project':
            self.install_project()
