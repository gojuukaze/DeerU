# -*- coding:utf-8 -*-

__author__ = 'gojuukaze'

from setuptools import setup, find_packages

setup(
    name="DeerU",
    version="2.0.2",
    description="DeerU is a content management system(DeerU 是一个开源博客系统)",
    long_description=open("README.rst").read(),
    license="GUN V3.0",

    url="https://github.com/gojuukaze/DeerU",
    author="gojuukaze",
    author_email="i@ikaze.uu.me",
    python_requires='>=3.6',
    install_requires=[
        'Django>=2.2,<3.0',
    ],
    zip_safe=False,
    include_package_data=True,

    packages=find_packages(include=['deeru_cmd*', ]),

    entry_points={
        'console_scripts': [
            'deeru-admin = deeru_cmd.bin.deeru_admin:run'
        ]
    },

    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Development Status :: 4 - Beta',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Internet :: WWW/HTTP :: WSGI',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],

    project_urls={
        'Documentation': 'https://deeru.readthedocs.io',
        'Source': 'https://github.com/gojuukaze/DeerU',
    },

)
