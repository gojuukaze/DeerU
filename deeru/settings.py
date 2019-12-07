"""
优先在settings_local中修改添加配置
"""
from app.deeru_config_handler.base import BaseHandler
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

# v2的config handler
CONFIG_HANDLER_DICT = {}
for f in CONFIG_HANDLER + CUSTOM_CONFIG_HANDLER:
    handler_mod = import_module(f)
    for name in dir(handler_mod):
        try:
            _class = getattr(handler_mod, name)
            name = getattr(_class, 'deeru_config_handler_name', None)
            if name:
                CONFIG_HANDLER_DICT[name] = _class
        except:
            pass

# log
if LOG_DIR:
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,

        'formatters': {
            'verbose': {
                'format': '{asctime} {levelname} {module}.{funcName} Line:{lineno} {message}',
                'formatTime': '%Y-%m-%d %H:%M:%S',
                'style': '{',
            },
            'simple': {
                'format': '{asctime} {levelname} {message}',
                'formatTime': '%Y-%m-%d %H:%M:%S',
                'style': '{',

            },
            'simple2': {
                'format': '{asctime} {message}',
                'style': '{',
            }
        },

        'handlers': {
            'console': {
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
                'formatter': 'simple'
            },

            'default_err': {
                'level': 'ERROR',
                'class': 'logging.handlers.WatchedFileHandler',
                'filename': os.path.join(LOG_DIR, 'error.log'),
                'formatter': 'verbose',
            },

            'info': {
                'level': 'INFO',
                'class': 'logging.handlers.WatchedFileHandler',
                'filename': os.path.join(LOG_DIR, 'info.log'),
                'formatter': 'verbose',
            },

        },

        'loggers': {
            'django': {
                'handlers': ['console'],
                'propagate': False,
                'level': 'INFO',
            },
            'django.request': {
                'handlers': ['default_err', 'console'],
                'level': 'ERROR',
                'propagate': False,
            },
            'error_logger': {
                'handlers': ['default_err', 'console'],
                'level': 'ERROR',
                'propagate': False,
            },
            'info_logger': {
                'handlers': ['info', 'console'] if DEBUG else ['info'],
                'level': 'INFO',
                'propagate': False,
            },

        }
    }
