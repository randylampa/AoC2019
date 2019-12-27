#!/usr/bin/env python3
# -*-coding-*-: utf-8
#
# AoC 2019
# RandyLampa

import os

DIR = os.path.dirname(os.path.realpath(__file__))


def get_file(name, filter_cbk = str):
    fh = open(DIR + "/" + name, "r")
    program = filter_cbk(fh.read())
    return program


def solve1():

    data = get_file(__file__, lambda x: "".join(filter(lambda y: y not in [" ", "\n"], x)))
    print(data)

    pass


def solve2():
    pass


if __name__ == "__main__":

    print("="*40)
    print("Solve 1 status:", solve1())
    print("="*40)

    print("="*40)
    print("Solve 2 status:", solve2())
    print("="*40)
