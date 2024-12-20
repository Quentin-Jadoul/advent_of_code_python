"""Solution for Day 1 of 2023"""

import sys
import os
import re

# Add the base directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from utils import time_and_print, read_input_file


import re
from utils import time_and_print, read_input_file


def parse_input():
    content = read_input_file("2023/data/day_01.txt")
    lines = content.split("\n")
    return lines


def part1(data):
    return sum(
        (digits := [int(i) for i in line if i.isdigit()]) * 10 + digits[-1]
        for line in data
    )


def part2(data):
    mappings = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
new_data = []
for line in data:
    transformed_line = []
    for i in range(len(line)):
        x = "".join([str(idx) for idx, val in enumerate(mappings, 1) if line[i:].startswith(val)])
        if x:
            transformed_line.append(x)
        else:
            transformed_line.append(line[i])
    new_data.append("".join(transformed_line))

    return part1(new_data)


if __name__ == "__main__":
    input_data = parse_input()
    time_and_print(lambda: part1(input_data), "Part 1")
    time_and_print(lambda: part2(input_data), "Part 2")
