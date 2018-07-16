#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import sys

import pkg_resources
from django.core import management
from django.conf import settings

help_text = [
    'Deeru内置命令表:',
    '', '',
    'install',
    'new',
    'version',
    'upgrade'
]


def run():
    settings_path = os.path.join(os.getcwd(), 'deeru')
    settings_py = os.path.join(settings_path, 'settings.py')

    if os.path.exists(settings_py):
        sys.path.insert(0, os.getcwd())
        os.environ['DJANGO_SETTINGS_MODULE'] = 'deeru.settings'
    else:
        settings.configure(INSTALLED_APPS=['deeru_cmd.apps.DeerUCmdConfig'])

    management.execute_from_command_line()


if __name__ == "__main__":
    run()
