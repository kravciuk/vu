# -*- coding: utf-8 -*-
__author__ = 'Vadim Kravciuk, vadim@kravciuk.com'

from hashids import Hashids
from .aes import AESCipher

SECRET_KEY = ''

def id_to_hash(short_id, salt=SECRET_KEY, length=4):
    return Hashids(salt=salt, min_length=length).encrypt(short_id)


def hash_to_id(short_id, salt=SECRET_KEY, length=4, default=0):
    hashids = Hashids(salt=salt, min_length=length)
    decrypt = hashids.decrypt(short_id)
    if len(decrypt) == 0:
        real_id = default
    else:
        real_id = decrypt[0]

    return real_id


def encrypt(key, plaintext):
    aes = AESCipher(SECRET_KEY)
    x = aes.encrypt(plaintext).decode('utf-8')
    pad_count = x.count('=')
    return "%s%s" % (x.replace('=', ''), pad_count)


def decrypt(key, ciphertext):
    try:
        aes = AESCipher(SECRET_KEY)
        i = int(ciphertext[-1])
        ciphertext = "%s%s" % (ciphertext[:-1], '='*i)
        return aes.decrypt(ciphertext)
    except Exception as e:
        return e