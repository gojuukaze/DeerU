import random
from math import sqrt

_MAPPING = ('零', '一', '二', '三', '四', '五', '六', '七', '八', '九', '十', '十一', '十二', '十三', '十四', '十五', '十六', '十七', '十八', '十九')
_P0 = ('', '十', '百', '千',)
_S4 = 10 ** 4


def num_to_ch(num):
    """
    copy from: https://www.jianshu.com/p/c87581f9aaa4
    """
    assert 0 <= num < _S4
    if num < 20:
        return _MAPPING[num]
    else:
        lst = []
        while num >= 10:
            lst.append(num % 10)
            num = num / 10
        lst.append(num)
        c = len(lst)  # 位数
        result = ''

        for idx, val in enumerate(lst):
            val = int(val)
            if val != 0:
                result += _P0[idx] + _MAPPING[val]
                if idx < c - 1 and lst[idx + 1] == 0:
                    result += '零'
        return result[::-1]


def rand_num(operator):
    if operator in ('+', '*', '-',):
        nums = (random.randint(0, 20), random.randint(0, 20))
        if nums[0] < nums[1] and '-' == operator:
            return nums[1], nums[0]
        return nums
    if operator == '√':
        num = random.randint(0, 10)
        return num * num, num
    if operator == '/':
        nums = (random.randint(1, 10), random.randint(1, 10))
        return nums[0] * nums[1], nums[0]


def get_result(num1, num2, operator):
    if operator == '√':
        return str(num2)
    else:
        return str(int(eval('%d%s%d' % (num1, operator, num2))))


def get_ch(num1, num2, operator):
    operators_to_ch = {'+': '加', '*': '乘', '-': '减', '/': '除以', }
    if operator == '√':
        return '根号 %s 等于' % num_to_ch(num1)
    return '%s %s %s 等于' % (num_to_ch(num1), operators_to_ch[operator], num_to_ch(num2))


def math_challenge():
    operators = ('+', '*', '-', '√', '/')
    operator = random.choice(operators)

    num1, num2 = rand_num(operator)

    return get_ch(num1, num2, operator), get_result(num1, num2, operator)


def noise_arcs(draw, image):
    size = image.size
    draw.arc([-20, -20, size[0], 20], 0, 295, fill='#FFB5C5')
    draw.line([-20, 20, size[0] + 20, size[1] - 20], fill='#FFB5C5')
    draw.line([-20, 0, size[0] + 20, size[1]], fill='#FFB5C5')
    return draw
