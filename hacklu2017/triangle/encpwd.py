# coding: utf-8
def enc_pwd(s):
    res = ''
    i = 0
    prev_odd = 0
    while i < len(s):
        c = ord(s[i])
        if prev_odd:
            c += (i & 0x3)
        c += 6
        prev_odd = c % 2
        res += chr(c)
        i += 1
    return res
