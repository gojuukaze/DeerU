import math
import random


def var(l):
    """
    Compute the variance of a list l.

    Args:
        l: (array): write your description
    """
    mean = sum(l) / len(l)
    temp_sum = 0
    for i in l:
        temp_sum += (i - mean) ** 2
    return temp_sum / len(l)


def sta(l):
    """
    Return the length of l.

    Args:
        l: (str): write your description
    """
    v = var(l)
    return math.sqrt(v)


def shuffle(l):
    """
    Shuffle a list of integers.

    Args:
        l: (todo): write your description
    """
    n = len(l)
    if n==1:
        return l
    for i in range(n):
        j = random.randint(0, n - 2)
        l[i], l[j] = l[j], l[i]
    return l
