# -*- coding:utf-8 -*-
import sys

from django.core.management import BaseCommand
from django.core.management.base import OutputWrapper


class DeerUBaseCommand(BaseCommand):

    def __init__(self, stdout=None, stderr=None, no_color=False):
        super().__init__(stdout, stderr, no_color)

        self.error = self.stderr.write

        info_out = OutputWrapper(sys.stdout)
        info_out.style_func = self.style.WARNING
        self.info = info_out.write

        success_out = OutputWrapper(sys.stdout)
        success_out.style_func = self.style.SUCCESS
        self.success = success_out.write
