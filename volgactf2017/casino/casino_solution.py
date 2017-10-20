#! /usr/bin/env python
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

from pwn import *
from hashlib import sha1
import random


def solve_proof_of_work(prefix):
    print "Solving with prefix {}...".format(prefix)
    sha_suffix2 = '\xff\xff\xff'  # gli ultimi 3 byte
    sha_suffix1 = 0x03  # i primi 2 bit COME INTERO

    while True:
        candidate = prefix + ''.join([chr(random.randrange(0x20,0x7e)) for _ in range(5)])
        hash = sha1(candidate).digest()
        # 26 == 3*8 + 2
        if hash[-3:] == sha_suffix2 and ord(hash[-4]) & 0b11 == sha_suffix1:
            print "Found!", candidate
            return candidate


class Generator:
    def __init__(self, p, init_state=1):
        m = len(p) - 1
        self.rshift = m - 1
        self.state = init_state & (2 ** m - 1)
        self.polynomial = int(''.join(map(str, p[1:])), 2)

    def next_bit(self):
        n = self.state & 1   # least significant bit (prossimo bit nell coda)
        v = bin(self.state & self.polynomial).count('1') & 1   # xor dei bit agli indici del polinomio
        self.state = (self.state >> 1) | (v << self.rshift)   # shifta a destra di 1 lo stato, pusha v come nuovo bit
        return n

    def next_number(self, bc):
        num = 0
        for i in range(bc):
            num |= self.next_bit() << (bc - 1 - i)
        return num


def update_bitstreams(stream_list, number):
    new_list = []
    for stream in stream_list:
        new_list.append(stream + '{:06b}'.format(number))
    if number < 22:
        for stream in stream_list:
            new_list.append(stream + '{:06b}'.format(number + 42))
    return new_list


def bm_algorithm(bitstream):
    '''https://en.wikipedia.org/wiki/Berlekamp%E2%80%93Massey_algorithm'''
    n = len(bitstream)
    b = [0 for _ in range(n)]
    b[0] = 1
    c = [0 for _ in range(n)]
    c[0] = 1
    L = 0
    m = -1
    for N in range(n):
        d = 0    # discrepanza
        for i in range(L + 1):
            d ^= int(bitstream[N-i]) * c[i]
        if d != 0:
            t = c[:]
            for j in range(N - m, n):
                c[j] = c[j] ^ b[j - (N - m)]
            if L <= N/2:
                L = N + 1 - L
                m = N
                b = t
    poly = c[:L] + [1]
    return L, poly


def next_guess(current_bitstream, poly):
    initial_stream = current_bitstream[:len(poly)][::-1]
    initial_state = int(initial_stream,2)
    generator = Generator(poly, initial_state)
    for _ in range(len(current_bitstream)):
        generator.next_bit()
    return generator.next_number(6) % 42


p = remote('casino.quals.2017.volgactf.ru', 8788)

# proof of work
question = p.recvline()
print question
prefix = question.split("'")[1]
solution = solve_proof_of_work(prefix)
p.sendline(solution)

possible_bitstreams = ['']

print p.recvuntil('42):\r\n')
guess = 0
print "GUESS", guess
p.sendline(str(guess))
result = p.readline()  # Congratulations/Wrong
print result

while True:
    if 'Congratulations' in result:
        new_num = guess
    else:
        new_num = int(result.split(' ')[4].strip('.'))

    # i bitstream reali possono essere più di uno a causa del modulo 42
    possible_bitstreams = update_bitstreams(possible_bitstreams, new_num)

    # eliminiamo i bitstream generati da lfsr più lunghi di 64 bit
    feasible_bitstreams = []
    polys = []
    for stream in possible_bitstreams:
        L, poly = bm_algorithm(stream)
        if L < 65:
            feasible_bitstreams.append((stream, L, poly))

    # metto in ordine per lunghezza dei lfsr
    feasible_bitstreams = sorted(feasible_bitstreams, key=(lambda x: x[1]))
    possible_bitstreams = [x[0] for x in feasible_bitstreams]
    polys = [x[2] for x in feasible_bitstreams]

    nextline = p.readline()
    print nextline
    if 'flag' in nextline:
        break
    else:
        # genera prossimo numero usando il lfsr più corto
        guess = next_guess(possible_bitstreams[0], polys[0])
        print "GUESS", guess
        p.sendline(str(guess))
        result = p.readline()
        print result

p.interactive()
# VolgaCTF{G@mbling_is_fun_but_rarely_a_pr0f1t}
