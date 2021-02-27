# -*- coding:utf-8 -*-
import os
import platform
import shutil
import subprocess
from pathlib import Path
from django.core.management import CommandError
from django.core import management
from django.template import Engine, Context

from deeru_cmd.management.base import DeerUBaseCommand


class Command(DeerUBaseCommand):
    """
    python manage.py starttheme xx
    """
    NEED_PROJECT = True
    templates_dir = 'app_templates'

    def add_arguments(self, parser):
        parser.description = '''创建DeerU主题目录'''

        parser.add_argument('name', type=str, help='名称')

    def mk_dir(self, dir_name):
        for name in dir_name:
            os.mkdir(Path(self.name) / name)

    def rm_file(self, files):
        for f in files:
            f = Path(self.name) / f
            if f.is_file():
                os.remove(f)
            else:
                shutil.rmtree(f)

    def handle(self, *args, **options):
        self.name = options['name']
        management.call_command('startapp', self.name)

        self.mk_dir(['static', Path('static/', self.name), 'templates', Path('templates/', self.name)])

        self.rm_file(['migrations', 'models.py', 'tests.py', 'views.py'])
