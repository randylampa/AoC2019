#!/usr/bin/env python3
# -*-coding-*-: utf-8
#
# AoC 2019
# RandyLampa

import os

DIR = os.path.dirname(os.path.realpath(__file__))


def get_input():
    data = "108457-562041"
    #data = "123457-562041" # test
    return data


def get_range():
    data = get_input()
    pass_range = tuple(map(lambda x: int(x), data.split("-")))
    return pass_range


def pass_have_double(pass_list):
    match = False
    prev = pass_list[0]
    for c in pass_list[1:]:
        if c == prev:
            match = True
            break
        prev = c
    if match:
        #print("have double:", pass_list)
        pass
    return match


def pass_is_increasing(pass_list):
    match = True
    prev = pass_list[0]
    for c in pass_list[1:]:
        match &= c >= prev
        prev = c
    if match:
        #print("is increasing:", pass_list)
        pass
    return match


def pass_match(password):
    pass_list = list(str(password))
    match = pass_have_double(pass_list) and pass_is_increasing(pass_list)
    return match


def solve1():

    pass_range = get_range()

    print("pass_range", pass_range)

    n = 0
    rng = range(pass_range[0], pass_range[1])
    #rng = range(pass_range[0], pass_range[0] + 100)
    for password in rng:
        #print(password)
        if pass_match(password):
            #print(password)
            n += 1

    return n


def solve2():
    pass


if __name__ == "__main__":

    print("="*40)
    print("Solve 1 status:", solve1())
    print("="*40)

    print("="*40)
    #print("Solve 2 status:", solve2())
    print("="*40)
