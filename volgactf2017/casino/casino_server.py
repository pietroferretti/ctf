#!/usr/bin/env python
# -*- coding: ascii -*-
from __future__ import print_function
import sys
import random
from fractions import gcd
# from secret import flag
flag = 'asdfff'

"""
    Utils
"""


def read_message():
    return sys.stdin.readline()


def send_message(message):
    sys.stdout.write('{0}\r\n'.format(message))
    sys.stdout.flush()


def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def gen_poly(deg):
    poly = [0 for _ in range(deg + 1)]
    while True:
        n = random.randrange(deg // 8, deg // 2)
        n |= 1
        powers = random.sample(range(1, deg), n)
        powers.append(deg)
        if reduce(gcd, tuple(powers)) == 1:
            break
    for i in range(n):
        poly[powers[i]] = 1
    poly[0] = poly[deg] = 1
    return poly


"""
    Generator
"""


class Generator:
    def __init__(self, p, init_state=1):
        m = len(p) - 1
        self.rshift = m - 1
        self.state = init_state & (2 ** m - 1)
        self.polynomial = int(''.join(map(str, p[1:])), 2)
        self.seq = []

    def next_bit(self):
        n = self.state & 1   # least significant bit (prossimo bit nell coda)
        v = bin(self.state & self.polynomial).count('1') & 1   # xor dei bit agli indici del polinomio
        self.state = (self.state >> 1) | (v << self.rshift)   # shifta a destra di 1 lo stato, pusha v come nuovo bit
        self.seq.append(n)
        return n

    def next_number(self, bc):
        num = 0
        for i in range(bc):
            num |= self.next_bit() << (bc - 1 - i)
        return num


"""
    Main
"""

if __name__ == '__main__':
    # parameters
    points = 21
    points_total = 101
    bc = 6
    range_max = 42
    N = random.randrange(24, 65)
    # N = 24
    # assert (2*N > points*bc)

    # initialize a generator
    poly = gen_poly(N)
    state = random.randrange(1, 2 ** (N - 1))
    generator = Generator(poly, state)

    # my debug
    print('N =', N)
    print('Poly:', poly)
    print(''.join([str(x) for x in poly]))
    print('State:', bin(state)[2:])

    # the honest casino
    try:
        send_message('Welcome to Guess-a-number game at VolgaCTF Grand Casino!\nYour stack: {0}\n'.format(points))
        # gamble
        while 0 < points < points_total:
            new_number = generator.next_number(bc)

            # my debug
            print('New number: {:06b}'.format(new_number), new_number, '->', new_number % range_max)
            # print('State:', bin(generator.state)[2:])
            # print(generator.seq)

            true_number = new_number % range_max
            send_message('Guess a number in range [0, {0}):'.format(range_max))
            guessed_number = int(read_message().strip())
            if not 0 <= guessed_number < range_max:
                send_message('Your guess "{0}" is not in the range'.format(guessed_number))
                continue
            if guessed_number == true_number:
                points += 1
                send_message('Congratulations! Your stack: {0}'.format(points))
            else:
                points -= 1
                send_message('Wrong. The number was {0}. Your stack: {1}'.format(true_number, points))

        # check points
        if points == points_total:
            send_message('Your flag: {0}'.format(flag))
        else:
            send_message('Wasted!')

    except Exception as ex:
        eprint('Exception: {0}'.format(ex))
        send_message('Something went wrong. Try again later!')
