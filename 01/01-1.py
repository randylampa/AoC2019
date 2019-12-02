#!/usr/bin/env python3
# -*-coding-*-: utf-8
#
# AoC 2019
# RandyLampa

from sys import *

# test input
#masses = [12, 14, 1969, 100756]

# input
#masses = []
fh = open("input-1", "r")
masses = list(map(lambda x: int(x.strip()), fh.readlines()))
#print(masses)
#exit()

print("Input masses:", masses)
reqs = []

for mass in masses:
	req = mass // 3 - 2
	reqs.append(req)
	
print("Output requirements:", reqs)

total = sum(reqs)

print("Fina requirement: ", total)
