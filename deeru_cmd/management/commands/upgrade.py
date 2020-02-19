# -*- coding:utf-8 -*-
import os
import platform
import shutil
import subprocess
from django.core.management import CommandError

from deeru_cmd.management.base import DeerUBaseCommand


class Command(DeerUBaseCommand):
    """
    升级
    python manage.py upgrade
    """
    NEED_PROJECT = True

    def add_arguments(self, parser):
        parser.description = '''升级DeerU'''

        parser.add_argument(
            '--branch',
            default='master',
            dest='branch',
            help='从哪个分支升级',
        )

    def handle(self, *args, **options):
        branch = options['branch']
        subprocess.run('git reset --hard', shell=True)
        result = subprocess.run('git pull origin '+branch, shell=True)
        if result.returncode != 0:
            raise CommandError('\n拉取最新版本失败，请参照手动升级教程升级')
        result =subprocess.run('pip install -r requirements.txt', shell=True)
        if result.returncode != 0:
            raise CommandError('\n安装依赖失败，请参照手动升级教程升级')
        self.success('\n升级完成，运行 python manage.py init_deeru 更新必要配置')

