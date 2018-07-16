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

    def handle(self, *args, **options):
        subprocess.run('git reset hard', shell=True)
        result = subprocess.run('git pull origin', shell=True)
        if result.returncode != 0:
            subprocess.run('git reset hard', shell=True)
            raise CommandError('\n升级失败')
        self.success('\n安装完成 ！！')
