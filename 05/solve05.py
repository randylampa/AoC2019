#!/usr/bin/env python3
# -*-coding-*-: utf-8
#
# AoC 2019
# RandyLampa

import os

DIR = os.path.dirname(os.path.realpath(__file__))


def data_to_program(data):
    program = [*map(int, data.strip().split(","))]
    return program


def get_program(name):
    fh = open(DIR + "/" + name, "r")
    program = data_to_program(fh.read())
    return program


class IntcodeError(Exception):
    pass


def execute_intcode_program(memory, dbg = True):

    I_ADD = 1
    I_MUL = 2
    I_INP = 3
    I_OUT = 4
    I_JNZ = 5 # jump if non-zero
    I_JEZ = 6 # jump if equal zero
    I_CLT = 7 # compare less than
    I_CEQ = 8 # compare equal
    I_HLT = 99

    valid = True

    pc = 0
    pc_step = 1
    while pc < len(memory):

        op1_val = None
        op2_val = None
        res_addr = None
        res_val = None
        jmp_val = None

        # FETCH
        instr = memory[pc]
        #modes = str(instr // 100).rjust(3, "0") # upper digits
        modes = list(map(int, str(instr // 100).rjust(3, "0"))) # upper digits
        modes.reverse()
        opcode = instr % 100 # lower digits

        print("PC={}, OP={}, MODE={}".format(pc, opcode, modes))

        # DECODE
        if opcode in [I_HLT]:
            pc_step = 1
        elif opcode in [I_INP, I_OUT]:
            pc_step = 2
        elif opcode in [I_JNZ, I_JEZ]:
            pc_step = 3
        elif opcode in [I_ADD, I_MUL, I_CLT, I_CEQ]:
            pc_step = 4
        else:
            raise IntcodeError("UNKNOWN instruction={} on pc={}".format(instr, pc))

        if opcode in [I_INP]:
            res_addr = memory[pc + 1]
        elif opcode in [I_OUT]:
            op1_val = memory[pc + 1] if modes[0] == 1 else memory[memory[pc + 1]]
        elif opcode in [I_JNZ, I_JEZ]:
            op1_val = memory[pc + 1] if modes[0] == 1 else memory[memory[pc + 1]]
            op2_val = memory[pc + 2] if modes[1] == 1 else memory[memory[pc + 2]]
        elif opcode in [I_ADD, I_MUL, I_CLT, I_CEQ]:
            op1_val = memory[pc + 1] if modes[0] == 1 else memory[memory[pc + 1]]
            op2_val = memory[pc + 2] if modes[1] == 1 else memory[memory[pc + 2]]
            res_addr = memory[pc + 3]

        # EXECUTE
        if opcode == I_HLT:
            break
        elif opcode == I_ADD:
            res_val = op1_val + op2_val
        elif opcode == I_MUL:
            res_val = op1_val * op2_val
        elif opcode == I_INP:
            try:
                res_val = int(input("Intcode INPUT :$ "))
            except ValueError:
                print("Non integer input treated as ZERO")
                res_val = 0
        elif opcode == I_OUT:
            print("Intcode OUTPUT :$", op1_val)
        elif opcode == I_JNZ:
            if op1_val != 0:
                jmp_val = op2_val
        elif opcode == I_JEZ:
            if op1_val == 0:
                jmp_val = op2_val
        elif opcode == I_CLT:
            res_val = 1 if op1_val < op2_val else 0
        elif opcode == I_CEQ:
            res_val = 1 if op1_val == op2_val else 0
        else:
            raise IntcodeError("NOT IMPLEMENTED instruction={} on pc={}".format(instr, pc))

        # WRITEBACK
        if res_addr is not None:
            memory[res_addr] = res_val

        #print(memory)

        if jmp_val:
            pc = jmp_val
        else:
            pc += pc_step

    return valid


def solve1():

    if True:
        # input
        memimg = get_program("input05")
    else:
        # input test
        memimg = get_program("input05.1-test1")
        #memimg = get_program("input05.1-test2")
        #memimg = get_program("input05.1-test3")
        #memimg = [102, 3, 1, 0, 99] # [9, 3, 1, 0, 99]

    print("program-pre", memimg)


    execute_intcode_program(memimg)

    print("program-post", memimg)

    pass


def solve2():

    if True:
        # input
        memimg = get_program("input05")
    else:
        # input test
        memimg = get_program("input05.2-test1")
        #memimg = data_to_program("")

    print("program-pre", memimg)


    execute_intcode_program(memimg)

    print("program-post", memimg)

    pass


if __name__ == "__main__":

    print("="*40)
    #print("Solve 1 status:", solve1())
    print("="*40)

    print("="*40)
    print("Solve 2 status:", solve2())
    print("="*40)
