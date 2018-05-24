import math
import random


def var(l):
    mean = sum(l) / len(l)
    temp_sum = 0
    for i in l:
        temp_sum += (i - mean) ** 2
    return temp_sum / len(l)


def sta(l):
    v = var(l)
    return math.sqrt(v)


def shuffle(l):
    n = len(l)
    if n==1:
        return l
    for i in range(n):
        j = random.randint(0, n - 2)
        l[i], l[j] = l[j], l[i]
    return l
