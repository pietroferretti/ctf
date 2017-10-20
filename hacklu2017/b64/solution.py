#!/bin/env python
# coding:utf-8

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

from pwn import *
from base64 import b64encode
import random

# host = 'flatearth.fluxfingers.net'
host = 'localhost'
port = 1718

cover_set = [0, 128, 75, 203, 36, 164, 8, 136]
b64chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz+/"

def enc(c1, c2):
    return chr(((ord(c1)^ord(c2))+64)%256)

def dec(ciphertext, char):
    return chr(((ord(ciphertext)- 64) %256)^ord(char))

def compare_chars(c1, c2):
    '''A compare function
        returns -1 if c1 is before c2
        returns +1 if c1 is after c2 '''
    # prendi 2 caratteri conosciuti, spara i valori di xor da cui sai che uscirà qualcosa in base64chars
    # il server fa enc(my, char) -> b64chars
    # quindi prendiamo dec(b64chars, char) = my
    # print c1.encode('hex'), c2.encode('hex')
    result = 0
    while result == 0:
        # choose two uniquely distinguishable b64chars
        a = random.choice(b64chars)
        b = random.choice(b64chars)
        if a == b:
            continue
        checka = dec(a, c1)
        checkb = dec(b, c2)
        for otherchar in chars:
            if otherchar != c1 and otherchar != c2:
                if dec(a, otherchar) == checka or dec(b, otherchar) == checka or dec(a, otherchar) == checkb or dec(b, otherchar) == checkb:
                    continue
        # print a, b
        # choose a position to split at
        i = random.randrange(1, 8)
        # choose who to test as first
        if random.randrange(2):
            mask = checka * i + checkb * (8 - i)
        else:
            mask = checkb * i + checka * (8 - i)
        # print mask.encode('hex')
        answer = b64encode(send_encode(mask))
        answer = answer.strip('=')
        if len(answer) % 4 != 0:
            answer = answer[:-1]
        # check if both chars are present once, otherwise retry
        if answer.count(a) == 1 and answer.count(b) == 1:
            if answer.index(a) < answer.index(b):
                return -1
            else:
                return 1


def send_encode(code):
    conn.recvuntil('> ')
    conn.sendline('1')
    conn.recvuntil('> ')
    conn.send(code)
    conn.recvuntil('answer: ')
    base64dec = conn.recvuntil('\nRound', drop=True)
    return base64dec

def send_secret(secret):
    conn.recvuntil('> ')
    conn.sendline('2')
    conn.recvuntil('> ')
    conn.sendline(secret)
    return conn.recvall()


print "Script started."

while 1:
    with remote(host, port) as conn:

        # find 8 characters
        chars = []
        for c in range(256):
            # print c
            answer = b64encode(send_encode(chr(c) * 8))
            answer = answer.strip('=')
            if len(answer) % 4 != 0:
                answer = answer[:-1]
            for x in answer:
                chars += dec(x, chr(c))
        chars = list(set(chars))

        if len(chars) != 8:    # we keep only the case when the characters are distinct
            print "Couldn't find all 8 characters."
            print "Trying again..."
            continue
        print "Characters found:"
        print chars

        # find order of chars
        chars = sorted(chars, cmp=compare_chars)
        print "Secret found:"
        print chars

        # get flag
        print send_secret(''.join(chars).encode('hex'))
        break
