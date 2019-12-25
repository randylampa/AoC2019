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


def draw_line(wire_points, start, end):
    dx = end[0] - start[0]
    dy = end[1] - start[1]
    #print("dx={}, dy={}".format(dx,dy))

    if dx != 0:
        d = -1 if dx < 0 else 1
        for x in range(start[0] + d, end[0] + d, d):
            wire_points.append((x, start[1]))
    elif dy != 0:
        d = -1 if dy < 0 else 1
        for y in range(start[1] + d, end[1] + d, d):
            wire_points.append((start[0], y))


def distance_manhattan(point1, point2):
    distance = abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])
    return distance


def get_grid_size_limit(wires_points):
    xs = []
    ys = []
    for wire_points in wires_points:
        for point in wire_points:
            xs.append(point[0])
            ys.append(point[1])
    size = ((min(xs), min(ys)), (max(xs), max(ys)))
    return size


def dump_grid(wires_points, crosses = [], centerpoint = (0, 0)):
    pass


def solve1():

    if True:
        wires = get_input("input03")
    else:
        #wires = get_input("input03-test0") # 6
        #wires = get_input("input03-test1") # 159
        wires = get_input("input03-test2") # 135

    #print("wires", wires)


    centerpoint = (1,1)
    wires_points = []
    crosses = []


    for wire in wires:
        # start at centerpoint
        print("WIRE")
        startpoint = centerpoint;
        wire_points = []

        for drr in wire:
            endpoint = drr_to_point(startpoint, drr)
            #print("endpoint", endpoint)
            draw_line(wire_points, startpoint, endpoint)
            # end as new start
            startpoint = endpoint

        wires_points.append(wire_points)


    #print("wires_points", wires_points)


    (wp1, wp2) = wires_points

    crosses = [*set(wp1).intersection(wp2)]

    #print("crosses", crosses)

    print("size", get_grid_size_limit(wires_points))

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
