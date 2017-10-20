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

'''Possiamo flippare un bit alla volta e distinguere i casi 1->0 e 0->1 controllando se il nuovo risultato è stato moltiplicato o diviso per 2**n'''

from pwn import *
from Crypto.Util.number import long_to_bytes

HOST = 'ppc2.chal.ctf.westerns.tokyo'
PORT = 28459

p = 160634950613302858781995506902938412625377360249559915379491492274326359260806831823821711441204122060415286351711411013883400510041411782176467940678464161205204391247137689678794367049197824119717278923753940984084059450704378828123780678883777306239500480793044460796256306557893061457956479624163771194201
g = 2

def mod_mul_powof2(n, t, p):
    return (n * pow(2, t, p)) % p    # compute 2**t separately to improve performance (nb: t is itself a power of 2)

if __name__ == '__main__':
    conn = remote(HOST, PORT)
    n = 0
    conn.sendline(str(0))
    basenum = int(conn.recvline().strip(), 16)
    for i in range(1000):
        conn.sendline(hex(1 << i))
        newnum = int(conn.recvline().strip(), 16)
        if mod_mul_powof2(basenum, 1 << i, p) == newnum:
            print 0
        elif mod_mul_powof2(newnum, 1 << i, p) == basenum:
            print 1
            n += (1 << i)
        else:
            assert False    # something went wrong
        print long_to_bytes(n)
