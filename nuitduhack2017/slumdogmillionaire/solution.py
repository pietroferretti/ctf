#!/usr/bin/python2.7

import random

current_draw = '33-26-56-99-38-87-91-21-27-68'    # changeme

def generate_combination():
    numbers = ""
    for _ in range(10):
        rand_num = random.randint(0, 99)
        if rand_num < 10:
            numbers += "0"
        numbers += str(rand_num)
        if _ != 9:
            numbers += "-"
    return numbers


def reset_jackpot(i):
    random.seed(i)


if __name__ == '__main__':
    for i in range(2**16):
        reset_jackpot(i)
        comb = generate_combination()
        if comb == current_draw:
            print i
            for _ in range(20):
                print generate_combination()
            break