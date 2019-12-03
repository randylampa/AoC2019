#!/usr/bin/env python3
# -*-coding-*-: utf-8
#
# AoC 2019
# RandyLampa

import os

DIR = os.path.dirname(os.path.realpath(__file__))


def get_input_test():
    masses = [12, 14, 1969, 100756]
    return masses


def get_input():
    fh = open(DIR + "/input-1", "r")
    masses = list(map(lambda x: int(x.strip()), fh.readlines()))
    return masses


def mass2fuel(mass):
    fuel = mass // 3 - 2
    return fuel


def solve1():
    # test input
    #masses = get_input_test()

    # input
    masses = get_input()

    print("Input masses:")
    print(masses)

    fuel = list(map(mass2fuel, masses))

    print("Fuel requirements:")
    print(fuel)

    total = sum(fuel)

    print("Total fuel requirement:")
    print(total)
    return total


def solve2():
    pass


if __name__ == "__main__":

    print("=" * 40)
    print("Solve 1 status:", solve1())
    print("=" * 40)

    print("=" * 40)
    print("Solve 2 status:", solve2())
    print("=" * 40)
