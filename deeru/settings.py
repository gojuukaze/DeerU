"""
优先在settings_local中修改添加配置
"""

from deeru.settings_common import *
from deeru.settings_local import *
from app.deeru_expression.expressions import BaseExpression

# app
INSTALLED_APPS += CUSTOM_APPS

# 导入表达式
from importlib import import_module

EXPRESSION_DICT = {}
for f in EXPRESSION + CUSTOM_EXPRESSION:
    exp_mod = import_module(f)
    for name in dir(exp_mod):
        if name.startswith('_') or name == 'BaseExpression':
            continue
        try:
            _class = getattr(exp_mod, name)
            if isinstance(_class(None), BaseExpression):
                EXPRESSION_DICT[name.lower()] = _class
        except:
            pass
