#!/usr/bin/env python3
# -*-coding-*-: utf-8
#
# AoC 2019
# RandyLampa

import os

DIR = os.path.dirname(os.path.realpath(__file__))


def line_to_wire(line):
    wire = [*map(lambda x: (x[0], int(x[1:])), line)]
    return wire


def get_input(name):
    fh = open(DIR + "/" + name, "r")
    lines = [*map(lambda x: x.strip().split(","), fh.readlines())]
    data = [*map(line_to_wire, lines)]
    return data


def drr_to_point(point, drr):
    drc = drr[0]
    step = drr[1]
    newpoint = None

    if drc == "L":
        newpoint = (point[0] - step, point[1])
    elif drc == "R":
        newpoint = (point[0] + step, point[1])
    elif drc == "D":
        newpoint = (point[0], point[1] - step)
    elif drc == "U":
        newpoint = (point[0], point[1] + step)
    else:
        print("Unknown direction: {}".format(drc))

    return newpoint


def put_point(grid, point, crosses):
    if point in grid:
        crosses.append(point)
    else:
        grid.append(point)


def draw_line(grid, start, end, crosses = []):
    dx = end[0] - start[0]
    dy = end[1] - start[1]
    #print("dx={}, dy={}".format(dx,dy))

    if dx != 0:
        d = -1 if dx < 0 else 1
        for x in range(start[0] + d, end[0] + d, d):
            #print(x)
            point = (x, start[1])
            put_point(grid, point, crosses)
    elif dy != 0:
        d = -1 if dy < 0 else 1
        for y in range(start[1] + d, end[1] + d, d):
            #print(y)
            point = (start[0], y)
            put_point(grid, point, crosses)


def distance_manhattan(point1, point2):
    distance = abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])
    return distance


def dump_grid(grid, dim_x, dim_y, crosses = [], centerpoint = (0, 0)):
    for y in range(dim_y):
        line = ""
        for x in range(dim_x):
            p = (x, y)
            if p == centerpoint:
                ch = "O"
            elif p in crosses:
                ch = "X"
            elif p in grid:
                ch = "+"
            else:
                ch = "."
            line += ch
        print(line)


def solve1():

    if False:
        wires = get_input("input03")
    else:
        wires = get_input("input03-test0") # 6
        #wires = get_input("input03-test1") # 159
        #wires = get_input("input03-test2") # 135

    print("wires", wires)


    centerpoint = (1,1);
    # grid[x][y] # e-e
    grid = []
    crosses = []

    grid.append(centerpoint)


    for wire in wires:
        # start at centerpoint
        print("WIRE")
        startpoint = centerpoint;


        for drr in wire:
            endpoint = drr_to_point(startpoint, drr)
            #print("endpoint", endpoint)
            draw_line(grid, startpoint, endpoint, crosses)
            # end as new start
            startpoint = endpoint

    #print("grid", grid)
    #dump_grid(grid, 100, 100, crosses, centerpoint)

    print("crosses", crosses)

    distances = [*map(lambda p: distance_manhattan(centerpoint, p), crosses)]
    print("distances", distances)

    distance = min(distances)

    return distance


def solve2():
    pass


if __name__ == "__main__":

    print("="*40)
    print("Solve 1 status:", solve1())
    print("="*40)

    print("="*40)
    #print("Solve 2 status:", solve2())
    print("="*40)
