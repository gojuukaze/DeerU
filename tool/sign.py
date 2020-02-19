from django.core.signing import Signer

"""
自带的签名算法，用于签名一需要校验的数据
"""


def sign(s):
    signer = Signer()
    return signer.sign(s)


def unsign(s):
    signer = Signer()
    try:
        return signer.unsign(s)
    except:
        return ''
