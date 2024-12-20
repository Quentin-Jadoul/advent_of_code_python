"""Solution for Day 13 of 2024"""

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from utils import time_and_print, read_input_file


def parse_input(file_path):
    content = read_input_file(file_path)
    machines = []
    lines = content.strip().split('\n')
    for i in range(0, len(lines), 4):
        a_x, a_y = map(lambda x: int(x[2:]), lines[i].split(': ')[1].split(', '))
        b_x, b_y = map(lambda x: int(x[2:]), lines[i+1].split(': ')[1].split(', '))
        prize_x, prize_y = map(lambda x: int(x[2:]), lines[i+2].split(': ')[1].split(', '))
        machines.append(((a_x, a_y), (b_x, b_y), (prize_x, prize_y)))
    return machines

def solve_equation_pair(a, b, c):
    det = a[0] * b[1] - a[1] * b[0]
    det_m = c[0] * b[1] - c[1] * b[0]
    det_n = a[0] * c[1] - a[1] * c[0]
    m = det_m / det
    n = det_n / det

    if m.is_integer() and n.is_integer():
        return int(m), int(n)
    return None, None

def part1():
    machines = parse_input("2024/data/day_13.txt")
    total = 0
    for a, b, prize in machines:
        m, n = solve_equation_pair(a, b, prize)
        if m and n:
            total += m * 3 + n
    return total

def part2():
    machines = parse_input("2024/data/day_13.txt")
    total = 0
    for a, b, prize in machines:
        prize = (prize[0] + 10000000000000, prize[1] + 10000000000000)
        m, n = solve_equation_pair(a, b, prize)
        if m and n:
            total += m * 3 + n
    return total

if __name__ == "__main__":
    time_and_print(part1, "Part 1")
    time_and_print(part2, "Part 2")