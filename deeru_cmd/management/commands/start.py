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
    python manage.py start
    """
    NEED_PROJECT = True
    templates_dir = 'app_templates'

    def get_app_templates(self):
        app_templates = [
            [
                'apps.py-tpl',
                Path(self.name) / Path('apps.py')
            ],

            [
                'setup.py-tpl',
                Path(self.name + '_setup.py')
            ],
            [
                'consts.py-tpl',
                Path(self.name) / Path('consts.py')
            ],
            [
                'README.rst-tpl',
                Path('README.rst')
            ],
            [
                'MANIFEST.in-tpl',
                Path('MANIFEST.in')
            ],
            [
                'git_add.py-tpl',
                Path('git_add.sh')
            ],
            [
                'empty.py-tpl',
                Path(self.name) / Path('management/__init__.py')
            ],
            [
                'empty.py-tpl',
                Path(self.name) / Path('management/commands/__init__.py')
            ],
        ]

        if self.type == 'theme':
            app_templates += [
                [
                    'empty.py-tpl',
                    Path(self.name + '/templates/' + self.name) / Path('home.html')
                ],
                [
                    'empty.py-tpl',
                    Path(self.name + '/templates/' + self.name) / Path('detail_article.html')
                ],
                [
                    'empty.py-tpl',
                    Path(self.name + '/templates/' + self.name) / Path('detail_article.html')
                ],
                [
                    'empty.py-tpl',
                    Path(self.name + '/templates/' + self.name) / Path('category.html')
                ],
                [
                    'empty.py-tpl',
                    Path(self.name + '/templates/' + self.name) / Path('tag.html')
                ],
                [
                    'empty.py-tpl',
                    Path(self.name + '/templates/' + self.name) / Path('404.html')
                ],
                [
                    'empty.py-tpl',
                    Path(self.name + '/templates/' + self.name) / Path('detail_flatpage.html')
                ],
            ]
        return app_templates

    def add_arguments(self, parser):
        parser.description = '''创建DeerU插件、主题项目'''

        parser.add_argument('type', type=str, choices=['plugin', 'theme'], help='项目的类型')
        parser.add_argument('name', type=str, help='名称')

    def mk_dir(self, dir_name):
        for name in dir_name:
            new_dir = os.path.join(self.name, name)
            os.mkdir(new_dir)

    def handle(self, *args, **options):
        self.type = options['type']
        self.name = options['name']
        management.call_command('startapp', self.name)
        dir_name = ['management', Path('management/commands')]
        self.mk_dir(dir_name)

        if self.type == 'theme':
            dir_name = ['static', Path('static/' + self.name), 'templates', Path('templates/' + self.name)]
            self.mk_dir(dir_name)

        context = Context({
            'app_name': self.name,
            'app_camel_name': self.name[0].upper() + self.name[1:],
            'app_upper_name': self.name.upper(),
            'deeru_type': self.type
        }, autoescape=False)

        for template_name, new_file in self.get_app_templates():
            template = Engine().from_string(self.get_template_str(template_name))
            content = template.render(context)
            new_file.write_text(content)
