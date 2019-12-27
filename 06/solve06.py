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


def data_to_orbits(data):
    """
    'AAA)BBB\nBBB)CCC' -> [('AAA', 'BBB'), ('BBB', 'CCC')]
    """
    orbits = [*map(lambda x : tuple(x.split(")")), data.strip().split("\n"))]
    return orbits


def get_orbit_index(orbit_list, orbit):
    try:
        index = orbit_list[0].index(orbit)
    except ValueError:
        index = None
    return index


def put_orbit(orbit_list, orbit):
    center, orbiter = orbit
    index = get_orbit_index(orbit_list, center)
    if index is None:
        orbit_list[0].append(center)
        orbit_list[1].append([])
        index = len(orbit_list[0]) - 1
    orbit_list[1][index].append(orbiter)


def generate_all_orbits(orbit_list, center, orbit_chain = []):
    index = get_orbit_index(orbit_list, center)
    orbit_chain.append(center)
    if index is None:
        return
    orbiters = orbit_list[1][index]
    #print(orbiters)
    for orbiter in orbiters:
        orbit_chain2 = orbit_chain.copy()
        orbit_list[2].append(orbit_chain2)
        generate_all_orbits(orbit_list, orbiter, orbit_chain2)


def solve1():

    orbits = get_file("input06", data_to_orbits)
    #orbits = get_file("input06.1-test", data_to_orbits)
    #print(orbits)

    orbit_list = [
        [], # indexes
        [], # orbiters
        [], # chains
    ]

    for orbit in orbits:
        put_orbit(orbit_list, orbit)

    #print("orbit_list", orbit_list)


    generate_all_orbits(orbit_list, "COM")

    #print("orbit_list[2]", orbit_list[2])


    orbit_counts = [*map(lambda x: len(x) - 1, orbit_list[2])]

    #print("orbit_counts", orbit_counts)

    orbit_count2 = sum(orbit_counts)

    #print("orbit_count2", orbit_count2)


    return orbit_count2


def solve2():
    pass


if __name__ == "__main__":

    print("="*40)
    print("Solve 1 status:", solve1())
    print("="*40)

    print("="*40)
    #print("Solve 2 status:", solve2())
    print("="*40)
