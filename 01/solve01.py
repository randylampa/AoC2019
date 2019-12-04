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


def get_input(name):
    fh = open(DIR + "/" + name, "r")
    masses = list(map(lambda x: int(x.strip()), fh.readlines()))
    return masses


def mass2fuel(mass):
    fuel = mass // 3 - 2
    return fuel


def solve1():
    # test input
    #masses = get_input_test()

    # input
    masses = get_input("input-1")

    print("Input masses:")
    print(masses)

    fuel = list(map(mass2fuel, masses))

    print("Fuel requirements:")
    print(fuel)

    total = sum(fuel)

    print("Total fuel requirement:")
    print(total)
    return total


def mass2fuel_realist(mass):
	
	l_fuel = []
	
	fuel = mass2fuel(mass)
	while fuel > 0:
		l_fuel.append(fuel)
		mass = fuel
		fuel = mass2fuel(mass)
	
	total_fuel = sum(l_fuel)
	
	return total_fuel


def solve2():
    # test input
    #masses = get_input_test()

    # input
    masses = get_input("input-1")

    print("Input masses:")
    print(masses)

    fuel = list(map(mass2fuel_realist, masses))

    print("Fuel requirements:")
    print(fuel)

    total = sum(fuel)

    print("Total fuel requirement:")
    print(total)
    return total


if __name__ == "__main__":

    print("=" * 40)
    print("Solve 1 status:", solve1())
    print("=" * 40)

    print("=" * 40)
    print("Solve 2 status:", solve2())
    print("=" * 40)
