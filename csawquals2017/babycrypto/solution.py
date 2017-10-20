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

'''AES ECB with a fixed key, my input is prefixed to a fixed string.
   Solved with a chosen plaintext attack, a byte at a time'''

from pwn import *

HOST = 'crypto.chal.csaw.io'
PORT = 1578


print "--- Phase 1 ---"

secret = ''
for n in range(16):
    print "N:", n

    with remote(HOST, PORT) as conn:
        conn.sendline('a' * (15-n))
        conn.recvuntil('Your Cookie is: ')
        base = conn.recvline().strip()[:32]

    for i in range(256):
        print "i:", i
        if i == 10:
            continue
        with remote(HOST, PORT) as conn:
            conn.sendline('a' * (15 -n) + secret + chr(i))
            conn.recvuntil('Your Cookie is: ')
            res = conn.recvline().strip()[:32]
            if res == base:
                secret += chr(i)
                print secret
                break


print "--- Phase 2 ---"

for n in range(16):
    print "N:", n

    with remote(HOST, PORT) as conn:
        conn.sendline('a' * (15-n))
        conn.recvuntil('Your Cookie is: ')
        base = conn.recvline().strip()[32:64]

    for i in range(256):
        print "i:", i
        if i == 10:
            continue
        with remote(HOST, PORT) as conn:
            conn.sendline(secret[(n+1):(n+16)] + chr(i))
            conn.recvuntil('Your Cookie is: ')
            res = conn.recvline().strip()[:32]
            if res == base:
                secret += chr(i)
                print secret
                break

print "Done:", secret
