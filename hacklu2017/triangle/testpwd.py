# coding: utf-8
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
