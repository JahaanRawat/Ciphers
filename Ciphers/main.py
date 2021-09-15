"""
Ciphers
by Jahaan Rawat
TODO: Adversary attack
"""
from random import randint


def shift_left(cha, n):
    return ''.join(chr(ord(char) - n) for char in cha)


def shift_right(cha, n):
    return ''.join(chr(ord(char) + n) for char in cha)


def encrypt(text, k):
    return shift_right(text, k)


def decrypt(c_text, k):
    return shift_left(c_text, k)


def smart_encrypt(text):
    text_list = list(text)
    keys = []
    c_text = []
    for alpha in text_list:
        k = randint(1, 255)
        keys.append(k)
        c_text.append(chr(ord(alpha) + k))
    return ''.join(c_text), keys


def smart_decrypt(c_text, keys):
    c_text_list = list(c_text)
    text = []
    i = 0
    while i < len(c_text_list):
        text.append(chr(ord(c_text[i]) - keys[i]))
        i += 1
    return ''.join(text)


if __name__ == '__main__':
    t = "Hello World!"
    c_t = smart_encrypt(t)
    print(smart_decrypt(c_t[0], c_t[1]))
