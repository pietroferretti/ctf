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

def remove_pass(s):
    # il primo carattere è un byte random
    result = ''
    for i in range(1, len(s)):
        result += chr((ord(s[i]) - ord(s[i-1])) % 128)
    return result

def decrypt_char(c, k):
    return chr((ord(c) - ord(k)) % 128)

def find_key_char(plain_char, cipher_char):
    return decrypt_char(cipher_char, plain_char)

def decrypt_string(s, k):
    return ''.join(decrypt_char(c, k) for c, k in zip(s, k*10))

def key_decryption_round(enc_key, key_char_list):
    # enc_key è il ciphertext
    # key_char_list è una lista con i caratteri di key (-1 se sconosciuto)
    new_key = key_char_list[:]
    for i in range(len(key_char_list)):
        if key_char_list[i] != -1:
            new_key[(i-4) % 13] = decrypt_char(enc_key[i], key_char_list[i])  # la sfasatura è di 4
    return new_key


def solve(ciphertext):
    assert len(ciphertext) == 36
    
    ct = remove_pass(ciphertext)
    assert len(ct) == 35

    enc_key = ct[-13:]
    key = [-1] * 13

    # trova valore della chiave per '|'
    key[21%13] = find_key_char('|', ct[21])

    # decripta la chiave stessa
    while -1 in key:
        key = key_decryption_round(enc_key, key)

    print 'Key found!'
    final_key = ''.join(key)
    print final_key

    print 'Message:'
    print decrypt_string(ct, final_key)


if __name__ == '__main__':
    with open('encrypted.txt', 'r') as f:
        ciphertext_hex = f.read().strip()
    print 'Ciphertext:'
    print ciphertext_hex
    solve(ciphertext_hex.decode('hex'))
