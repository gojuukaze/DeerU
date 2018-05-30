#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import platform
import os


def run():
    print('开始安装DeerU')
    # 环境检测
    if not platform.python_version().startswith('3'):
        print('python版本必须3+，当前版本:' + platform.python_version())
        return
    if 'windows' in platform.system().lower():
        print('windows 不支持自动安装')

    os.system('git clone -b dev git@github.com:gojuukaze/DeerU.git')
    os.system('cd DeerU && pip install -r requirements.txt')
    print('\n安装完成 ！！')


if __name__ == '__main__':
    run()
