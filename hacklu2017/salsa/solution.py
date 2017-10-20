#!/bin/env python
# coding: utf-8

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

'''Salsa20 encryption but with a fixed nonce and not enough keystream displacement,
   leading to keystream reuse'''

from pwn import *
from base64 import b64encode, b64decode
import json

# host = 'localhost'
host = 'flatearth.fluxfingers.net'
# port = 9999
port = 1721

LEN = 100 

def xor_str(s1, s2):
    return ''.join(chr(ord(x) ^ ord(y)) for x, y in zip(s1, s2))

def get_data(s):
    conn.send(s)
    return conn.recvrepeat(0.5)

with remote(host, port) as conn:
    ciphertext = conn.recvrepeat(0.5)
    # print ciphertext.encode('hex')

    fakeflag = 'a'*LEN
    message = "Hello my dear friend, the flag is {}!".format(fakeflag)
    myplain = '{"cnt": 1, "data": "' + b64encode(message) + '"}'
    # print myplain
    mycipher = get_data(message)
    keystream = xor_str(myplain, mycipher)
    # print keystream.encode('hex')
    plaintext = xor_str(keystream, ciphertext[1:])
    print plaintext
    mydict = json.loads('{' + plaintext.strip())
    flag = b64decode(mydict['data'])
    print flag