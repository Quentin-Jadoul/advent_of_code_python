"""Solution for Day 17 of 2024"""

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from utils import time_and_print, read_input_file

def parse_input():
    content = read_input_file("2024/data/day_17.txt")
    lines = content.strip().split('\n')
    registers = [
        int(lines[0].split(': ')[1]),
        int(lines[1].split(': ')[1]),
        int(lines[2].split(': ')[1])
    ]
    program = list(map(int, lines[4].split(': ')[1].split(',')))
    return registers, program

def get_combo_value(operand, A, B, C):
    if operand <= 3:
        return operand
    elif operand == 4:
        return A
    elif operand == 5:
        return B
    elif operand == 6:
        return C
    else:
        raise ValueError("Invalid combo operand")

def run_program(registers, program):
    A, B, C = registers
    output = []
    ip = 0  # instruction pointer

    while ip < len(program):
        opcode = program[ip]
        operand = program[ip + 1]

        if opcode == 0:  # adv
            combo_value = get_combo_value(operand, A, B, C)
            A = A // (2 ** combo_value)
        elif opcode == 1:  # bxl
            B ^= operand
        elif opcode == 2:  # bst
            combo_value = get_combo_value(operand, A, B, C)
            B = combo_value % 8
        elif opcode == 3:  # jnz
            if A != 0:
                ip = operand
                continue
        elif opcode == 4:  # bxc
            B ^= C
        elif opcode == 5:  # out
            combo_value = get_combo_value(operand, A, B, C)
            output.append(combo_value % 8)
        elif opcode == 6:  # bdv
            combo_value = get_combo_value(operand, A, B, C)
            B = A // (2 ** combo_value)
        elif opcode == 7:  # cdv
            combo_value = get_combo_value(operand, A, B, C)
            C = A // (2 ** combo_value)

        ip += 2

    return ','.join(map(str, output))

def part1():
    registers, program = parse_input()
    output = run_program(registers, program)
    return output

def part2():
    registers, program = parse_input()
    B, C = registers[1], registers[2]  # Initial values for B and C

    for A in range(1, 100000000):  # Arbitrary large range to find the solution
        registers = [A, B, C]
        output = run_program(registers, program)
        if output == ','.join(map(str, program)):
            return A

if __name__ == "__main__":
    time_and_print(part1, "Part 1")
    time_and_print(part2, "Part 2")