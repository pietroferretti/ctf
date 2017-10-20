#!/usr/bin/python2.7

import random

import config
import utils


random.seed(utils.get_pid())
ngames = 0


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


def reset_jackpot():
    random.seed(utils.get_pid())
    utils.set_jackpot(0)
    ngames = 0


def draw(user_guess):
    ngames += 1
    if ngames > config.MAX_TRIES:
        reset_jackpot()
    winning_combination = generate_combination()
    if winning_combination == user_guess:
        utils.win()
        reset_jackpot()
