from django.conf import settings
from pyDes import triple_des, CBC, PAD_PKCS5
import binascii

# 秘钥
KEY = settings.SECRET_KEY


def encrypt(s):
    """
    DES 加密
    :param s: 原始字符串
    :return: 加密后字符串，16进制
    """
    secret_key = KEY[:24]
    iv = secret_key[-8:]
    k = triple_des(secret_key, mode=CBC, IV=iv, padmode=PAD_PKCS5)
    en = k.encrypt(s, padmode=PAD_PKCS5)
    return binascii.b2a_hex(en).decode(encoding='utf-8')


def descrypt(s):
    """
    解密
    :param s: 加密后的字符串，16进制
    :return:  解密后的字符串
    """
    secret_key = KEY[:24]
    iv = secret_key[-8:]
    k = triple_des(secret_key, mode=CBC, IV=iv, padmode=PAD_PKCS5)
    de = k.decrypt(binascii.a2b_hex(s), padmode=PAD_PKCS5)
    return de.decode(encoding='utf-8')
