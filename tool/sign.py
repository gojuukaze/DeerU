from django.core.signing import Signer

"""
自带的签名算法，用于签名一需要校验的数据
"""


def sign(s):
    """
    Signs a string with the given signer.

    Args:
        s: (array): write your description
    """
    signer = Signer()
    return signer.sign(s)


def unsign(s):
    """
    Unsign a signer.

    Args:
        s: (array): write your description
    """
    signer = Signer()
    try:
        return signer.unsign(s)
    except:
        return ''
