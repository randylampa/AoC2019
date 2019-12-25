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


def get_wires(is_hot = False):
    if is_hot:
        wires = get_input("input03")
    else:
        wires = get_input("input03-test0") # dist=6, steps=30
        #wires = get_input("input03-test1") # dist=159, steps=610
        #wires = get_input("input03-test2") # dist=135, steps=410

    return wires


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


def get_wires_points(wires, center_point = (1, 1)):
    wires_points = []

    for wire in wires:
        # start at centerpoint
        #print("WIRE")
        startpoint = center_point;
        wire_points = []

        for drr in wire:
            endpoint = drr_to_point(startpoint, drr)
            #print("endpoint", endpoint)
            draw_line(wire_points, startpoint, endpoint)
            # end as new start
            startpoint = endpoint

        wires_points.append(wire_points)

    return wires_points


def get_wires_crosses(wires_points):
    (wp1, wp2) = wires_points
    crosses = [*set(wp1).intersection(wp2)]
    return crosses


def points_to_distances(points, ref_point = (0, 0)):
    distances = [*map(lambda p: distance_manhattan(ref_point, p), points)]
    return distances


def solve1():

    wires = get_wires(True)

    #print("wires", wires)


    center_point = (1,1)
    wires_points = get_wires_points(wires, center_point)

    #print("wires_points", wires_points)


    crosses = get_wires_crosses(wires_points)

    #print("crosses", crosses)


    distances = points_to_distances(crosses, center_point)

    print("distances", distances)

    distance = min(distances)

    return distance


def solve2():

    wires = get_wires(True)

    #print("wires", wires)


    center_point = (1,1)
    wires_points = get_wires_points(wires, center_point)

    #print("wires_points", wires_points)


    crosses = get_wires_crosses(wires_points)

    #print("crosses", crosses)


    distances = []

    for cross in crosses:
        (wp1, wp2) = wires_points
        l1 = None
        l2 = None
        try:
            l1 = wp1.index(cross)
            l2 = wp2.index(cross)
        except ValueError:
            print("Cross not found!")

        if l1 is not None and l2 is not None:
            distances.append(l1 + 1 + l2 + 1)

    print("distances", distances)

    distance = min(distances)

    return distance


if __name__ == "__main__":

    print("="*40)
    #print("Solve 1 status:", solve1())
    print("="*40)

    print("="*40)
    print("Solve 2 status:", solve2())
    print("="*40)
