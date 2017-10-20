# coding: utf-8
def dec_test(e):
    i = 0
    s = ''
    while i < len(e):
        a = ord(e[i])
        a -= 5
        if i%2 == 1:
            a += 3
        s += chr(a)
        i += 1
    return s
