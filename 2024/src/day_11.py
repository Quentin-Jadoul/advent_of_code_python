"""Solution for Day 11 of 2024"""

import sys
import os
from collections import Counter

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from utils import time_and_print, read_input_file

def parse_input():
    content = read_input_file("2024/data/day_11.txt")
    content = [int(x) for x in content.split()]
    return content

transformation_cache = {}

def transform_stone(value):
    if value in transformation_cache:
        return transformation_cache[value]
    
    if value == 0:
        result = [1]
    elif len(str(value)) % 2 == 0:
        digits = str(value)
        mid = len(digits) // 2
        left = int(digits[:mid])
        right = int(digits[mid:])
        result = [left, right]
    else:
        result = [value * 2024]
    
    transformation_cache[value] = result
    return result

def process_stones_with_memoization(stones, blinks):
    for i in range(blinks):
        next_stones = Counter()
        for value, count in stones.items():
            for new_value in transform_stone(value):
                next_stones[new_value] += count
        stones = next_stones
    return stones

def part1():
    initial_stones = Counter(parse_input())
    blinks = 25

    final_stones = process_stones_with_memoization(initial_stones, blinks)

    return sum(final_stones.values())

def part2():
    initial_stones = Counter(parse_input())
    blinks = 75

    final_stones = process_stones_with_memoization(initial_stones, blinks)

    print(len(final_stones))

    return sum(final_stones.values())

if __name__ == "__main__":
    time_and_print(part1, "Part 1")
    time_and_print(part2, "Part 2")
