#!/usr/bin/env python3
import pickle
import sys

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

def most_common(lst):
    return max(set(lst), key=lst.count)

def xor_bytes(var, key):
    int_var = int.from_bytes(var, sys.byteorder)
    int_key = int.from_bytes(key, sys.byteorder)
    int_enc = int_var ^ int_key
    return int_enc.to_bytes(len(var), sys.byteorder)


with open('flag.enc', 'rb') as f:
    ciphertext = f.read()

# spezziamo il ciphertext in pezzi di 20 byte (lunghezza della chiave)
subs = []
for i in range(0, len(ciphertext), 20):
    subs.append(ciphertext[i:i+20])

# byte per indice in ogni substring
characters = []
for i in range(20):
    characters.append([])
    for s in subs[:-1]:
        characters[i].append(s[i])

# ipotizzo che il carattere piu' frequente sia lo spazio (\x20)
key = b''
for index_chars in characters:
    key += (most_common(index_chars) ^ 0x20).to_bytes(1, sys.byteorder)
print('key', key)
# key = b'\xd1\xffc\xf7\xc8u\xd8\xc4\x1a\x84\xca$[f\x0c\x1f\xc6\xe2\xcc\xea'

# chiave modificata a mano:
key = b'\x94\xffc\xa3\x8du\xd8\xc4\x1a\xc1\xca$\x1ef\x0c\x1f\xc6\xe2\xcc\xea'

try:
    solution = b''
    for x in subs:
        tmp = xor_bytes(x, key)
        print(tmp)
        solution += tmp

finally:
    print(solution)
    # VolgaCTF{N@me_is_Pad_Many_Times_P@d_Mi$$_me?}