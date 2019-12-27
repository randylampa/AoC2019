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


def pass_have_double2(char_list):
    """
    Contains at least one group of two same digits.
    Subgroup of bigger group does not counts.
    """
    group_list = []
    for c in char_list:
        # get last group and if char is different, add new

        #print("group_list", group_list)
        last_group = group_list.pop() if group_list else []
        #print("last_group", last_group)

        if last_group and last_group[-1] != c:
            group_list.append(last_group)
            last_group = []
        last_group.append(c)

        #print("last_group", last_group)
        group_list.append(last_group)

    #print("group_list", group_list)

    group_lens = [*map(lambda l: len(l), group_list)]

    #print("group_lens", group_lens)


    match = group_lens.count(2) > 0

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


def pass_match2(password):
    pass_list = list(str(password))
    match = pass_have_double2(pass_list) and pass_is_increasing(pass_list)
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

    ttt = []#[112233, 123444, 111122]
    for password in ttt:
        pass_list = list(str(password))
        print(password, pass_have_double2(pass_list))


    pass_range = get_range()

    print("pass_range", pass_range)

    n = 0
    rng = range(pass_range[0], pass_range[1])
    #rng = range(pass_range[0], pass_range[0] + 100)
    for password in rng:
        #print(password)
        if pass_match2(password):
            #print(password)
            n += 1

    return n


if __name__ == "__main__":

    print("="*40)
    #print("Solve 1 status:", solve1())
    print("="*40)

    print("="*40)
    print("Solve 2 status:", solve2())
    print("="*40)
