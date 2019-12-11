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
            raise CommandError('\n自动升级失败，请参照手动升级教程升级')
        self.success('\n安装完成 ！！')

