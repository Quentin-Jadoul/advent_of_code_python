"""Solution for Day 3 of 2024"""

import re
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from utils import time_and_print, read_input_file

def parse_input():
    content = read_input_file("2024/data/day_03.txt")
    return content

def part1():
    content = parse_input()
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    matches = re.findall(pattern, content)
    
    total = 0
    for match in matches:
        x, y = map(int, match)
        total += x * y
    
    return total

def part2():
    content = parse_input()
    pattern = r"(mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\))"
    matches = re.findall(pattern, content)
    
    total = 0
    mul_enabled = True
    
    for match in matches:
        instruction = match[0]
        
        if instruction == "do()":
            mul_enabled = True
        elif instruction == "don't()":
            mul_enabled = False
        else:
            if mul_enabled:
                x, y = map(int, match[1:3])
                total += x * y
    
    return total

if __name__ == "__main__":
    time_and_print(part1, "Part 1")
    time_and_print(part2, "Part 2")
