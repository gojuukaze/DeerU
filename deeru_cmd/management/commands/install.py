# -*- coding:utf-8 -*-
import os
import platform
import shutil
import subprocess
from pathlib import Path

from django.core.management import CommandError
from django.core.management.utils import get_random_secret_key
from django.template import Context, Engine

from deeru_cmd.management.base import DeerUBaseCommand


class Command(DeerUBaseCommand):
    """
    下载deeru项目
    python manage.py install_project
    """

    DEERU_GIT_URL = 'https://github.com/gojuukaze/DeerU.git'
    templates_dir = 'project_templates'

    def add_arguments(self, parser):
        parser.description = '''安装下载DeerU项目、插件、主题'''

        parser.add_argument('name', type=str, help='名称')

        parser.add_argument(
            '--branch',
            default='master',
            dest='branch',
            help='从哪个分支下载',
        )

    def get_project_templates(self):
        return [
            ['settings_local.py-tpl', Path(self.name) / Path('deeru/settings_local.py')],
            ['urls_local.py-tpl', Path(self.name) / Path('deeru/urls_local.py')]
        ]

    def install_project(self):
        self.info('开始安装DeerU')

        self.info('下载DeerU ...')

        s = ''
        if os.path.exists(self.name):
            # self.info('已存在相同目录 "%s" ,请选择: d(删除已存在目录); s(跳过下载) ' % self.name)
            s = input('已存在相同目录 "%s" ,请选择: d(删除已存在目录); s(跳过下载): ' % self.name)
            if s == 'd':
                shutil.rmtree(self.name)
            elif s == 's':
                pass
            else:
                raise CommandError('输入错误')

        if s != 's':
            result = subprocess.run('git clone -b %s %s %s' % (self.branch, self.DEERU_GIT_URL, self.name), shell=True)
            if result.returncode != 0:
                raise CommandError('\n下载DeerU失败')

        self.info('安装依赖...')
        result = subprocess.run('pip install -r requirements.txt', cwd=self.name, shell=True)
        if result.returncode != 0:
            raise CommandError('\n安装依赖失败')

        self.info('复制必要文件...')

        context = Context({'SECRET_KEY': get_random_secret_key()}, autoescape=False)

        for template_name, new_file in self.get_project_templates():
            template = Engine().from_string(self.get_template_str(template_name))
            content = template.render(context)
            new_file.write_text(content)

        self.success('\n安装完成 ！！')

    def handle(self, *args, **options):
        self.name = options['name']
        self.branch = options['branch']

        self.install_project()
