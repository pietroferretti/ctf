# coding: utf-8
def dec_pwd(s):
    res = ''
    i = 0
    prev_odd = 0
    while i < len(s):
        c = ord(s[i])
        this_odd = prev_odd
        prev_odd = c % 2
        c -= 6
        if this_odd:
            c -= (i & 0x3)
        res += chr(c)
        i += 1
    return res
