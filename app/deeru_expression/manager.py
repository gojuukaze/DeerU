import re

from app.manager.config_manager import get_global_value_by_key
from django.conf import settings


def format_expression(value):
    if not value or not isinstance(value, str):
        return value

    # 全局变量{{xxx}}
    expression = re.findall(r'^{{(.*)}}$', value.strip())
    if expression:
        if not expression[0]:
            return None
        else:
            return get_global_value_by_key(expression[0])
    # 表达式{%xx|xx%}
    expression = re.findall(r'^{%(.*)%}$', value.strip())
    if expression:
        if not expression[0]:
            return None
        else:
            pos = expression[0].find('|')
            if pos == -1:
                return None
            else:
                exp_name = expression[0][:pos].strip()
                exp_args = expression[0][pos + 1:]
                exp_class = settings.EXPRESSION_DICT.get(exp_name.lower(), None)
                if not exp_class:
                    return None
                return exp_class(exp_args)
    # 普通的字符串
    else:
        return value
