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
def test_pwd(e, _):
    i = 0
    while i < len(e):
        a = ord(e[i])
        b = ord(_[i])
        b += 5
        if i % 2 == 1:
            b -= 3
        if a != b:
            print "Failed!"
            return 0
        i += 1
    return 1
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
dec_test("XYzaSAAX_PBssisodjsal_sSUVWZYYYb")
print dec_pwd(dec_test("XYzaSAAX_PBssisodjsal_sSUVWZYYYb"))
