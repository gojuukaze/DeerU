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
    用来临时跑一些东西
    python manage.py install
    """

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
                    Path(self.name+'/templates/'+self.name) / Path('home.html')
                ],
                [
                    'empty.py-tpl',
                    Path(self.name+'/templates/'+self.name) / Path('detail_article.html')
                ],
                [
                    'empty.py-tpl',
                    Path(self.name+'/templates/'+self.name) / Path('detail_article.html')
                ],
                [
                    'empty.py-tpl',
                    Path(self.name+'/templates/'+self.name) / Path('category.html')
                ],
                [
                    'empty.py-tpl',
                    Path(self.name+'/templates/'+self.name) / Path('tag.html')
                ],
                [
                    'empty.py-tpl',
                    Path(self.name+'/templates/'+self.name) / Path('404.html')
                ],
                [
                    'empty.py-tpl',
                    Path(self.name+'/templates/'+self.name) / Path('detail_flatpage.html')
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

    def get_template_str(self, template_name):
        import deeru_cmd
        template_dir = deeru_cmd.__path__[0]
        templdate_file = Path(template_dir) / Path('app_templates') / Path(template_name)
        return templdate_file.read_text()

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
            'deeru_type': self.type
        }, autoescape=False)

        for template_name, new_file in self.get_app_templates():
            template = Engine().from_string(self.get_template_str(template_name))
            content = template.render(context)
            new_file.write_text(content)
