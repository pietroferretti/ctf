# coding: utf-8

'''Every bit in the image is trivially bit flipped.
   Easy to find out from the header magic bytes'''

f = open('secret_encrypted.png')
s = f.read()
m = ''.join(chr((ord(x) ^ 0xff) & 0xff) for x in s)
f = open('secret.png', 'w')
f.write(m)
f.close()
