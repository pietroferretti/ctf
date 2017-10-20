#!/bin/env python
# -*- coding: utf-8 -*-

# MIT License
#
# Copyright (c) 2017 Pietro Ferretti
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

def xor(s1,s2):
    return ''.join(chr(ord(a) ^ ord(b)) for a,b in zip(s1,s2))

def repeat(s, l):
    return (s*(int(l/len(s))+1))[:l]

def key_decryption_round(enc_key, key_char_list):
    # enc_key è il ciphertext
    # key_char_list è una lista con i caratteri di key (-1 se sconosciuto)
    new_key = key_char_list[:]
    for i in range(len(key_char_list)):
        if key_char_list[i] != -1:
            new_key[(i+38) % 67] = xor(enc_key[i], key_char_list[i])  # la sfasatura è di +38
    return new_key


enc = open('encrypted').read().strip().decode('hex')

key = [-1] * 67
key = list(xor(enc, 'flag{')) + key[5:]

while -1 in key:
    key = key_decryption_round(enc[38:38+67], key)

print 'Key found!'
final_key = ''.join(key)
print final_key

print 'Message:'
print xor(enc, repeat(key, len(enc)))

# TODO: fare una funzione che usa key_decryption_round e trova da sola la sfasatura
# ad esempio controllando se un round sovrascrive con valori diversi caratteri della chiave già trovati
# così bruteforziamo rapidamente anche quella
