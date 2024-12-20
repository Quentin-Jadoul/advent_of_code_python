"""Solution for Day 19 of 2024"""

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from utils import time_and_print, read_input_file

def parse_input():
    content = read_input_file("2024/data/day_19.txt")
    lines = content.strip().split('\n')
    patterns = lines[0].split(', ')
    designs = lines[2:]
    return patterns, designs

def can_construct_design(patterns, design):
    dp = [0] * (len(design) + 1)
    dp[0] = 1

    for i in range(1, len(design) + 1):
        for pattern in patterns:
            if i >= len(pattern) and design[i - len(pattern):i] == pattern:
                dp[i] += dp[i - len(pattern)]
    
    return dp[len(design)]

def part1():
    patterns, designs = parse_input()
    possible_count = sum(can_construct_design(patterns, design) > 0 for design in designs)
    return possible_count

def part2():
    patterns, designs = parse_input()
    total_ways = sum(can_construct_design(patterns, design) for design in designs)
    return total_ways

if __name__ == "__main__":
    time_and_print(part1, "Part 1")
    time_and_print(part2, "Part 2")
