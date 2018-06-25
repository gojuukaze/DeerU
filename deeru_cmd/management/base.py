# -*- coding:utf-8 -*-
import os
import sys

from django.core.management import BaseCommand, CommandError
from django.core.management.base import OutputWrapper


class DeerUBaseCommand(BaseCommand):
    NEED_PROJECT = False

    def __init__(self, stdout=None, stderr=None, no_color=False):
        super().__init__(stdout, stderr, no_color)

        # 检测目录位置
        if self.NEED_PROJECT:
            settings_path = os.path.join(os.getcwd(), 'deeru')
            settings_py = os.path.join(settings_path, 'settings.py')

            if not os.path.exists(settings_py):
                raise CommandError('该命令需要在工程目录下运行')

        self.error = self.stderr.write

        info_out = OutputWrapper(sys.stdout)
        info_out.style_func = self.style.WARNING
        self.info = info_out.write

        success_out = OutputWrapper(sys.stdout)
        success_out.style_func = self.style.SUCCESS
        self.success = success_out.write
