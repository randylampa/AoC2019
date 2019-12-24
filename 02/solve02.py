#!/usr/bin/env python3
# -*-coding-*-: utf-8
#
# AoC 2019
# RandyLampa

import os

DIR = os.path.dirname(os.path.realpath(__file__))


def get_program(name):
    fh = open(DIR + "/" + name, "r")
    program = [*map(lambda x: int(x), fh.read().strip().split(","))]
    return program


def execute_program(program, dbg = True):

    for pc in range(0, len(program), 4):
        #print("pc", pc)

        # fetch instruction
        instr = program[pc]

        # 1-byte instr
        if instr == 99:
            # HLT - halt
            print("Executing HLT on pc={}".format(pc)) if dbg else None
            break

        # 4-byte instr
        op1 = program[pc + 1]
        op2 = program[pc + 2]
        op3 = program[pc + 3]

        if instr == 1:
            # ADD - addition
            print("Executing ADD on pc={}".format(pc)) if dbg else None
            program[op3] = program[op1] + program[op2]
            pass
        elif instr == 2:
            # MUL - multiply
            print("Executing MUL on pc={}".format(pc)) if dbg else None
            program[op3] = program[op1] * program[op2]
            pass
        else:
            # unknown
            print("UNKNOWN instruction={} on pc={}".format(instr, pc))
            break

    return program


def solve1():

    if True:
        # input
        program = get_program("input02-1")
        """
        To do this, before running the program, replace position 1 with the value 12 and replace position 2 with the value 2. What value is left at position 0 after the program halts?
        """
        program[1] = 12
        program[2] = 2
    else:
        # input test
        program = get_program("input02-1-test2")


    print("program-pre", program)

    execute_program(program)

    print("program-post", program)

    return program[0]


def solve2():

    value_to_find = 19690720

    # input
    program = get_program("input02-1")

    is_found = False

    for noun in range(0, 100):
        for verb in range(0, 100):

            programX = program.copy()
            programX[1] = noun
            programX[2] = verb

            execute_program(programX, False)

            res = programX[0]
            print("noun={}, verb={}, res={}".format(noun, verb, res))

            if res == value_to_find:
                is_found = True
                break
        if is_found:
            break

    result = 100 * noun + verb

    return result


if __name__ == "__main__":

    print("="*40)
    print("Solve 1 status:", solve1())
    print("="*40)

    print("="*40)
    print("Solve 2 status:", solve2())
    print("="*40)
