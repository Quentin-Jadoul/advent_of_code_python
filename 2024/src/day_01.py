"""Solution for Day 1 of 2024"""

from collections import Counter
from utils import time_and_print, read_input_file

def parse_input():
    content = read_input_file("2024/data/day_01.txt")
    numbers1, numbers2 = zip(*(map(int, line.split("   ")) for line in content.split("\n")))
    return list(numbers1), list(numbers2)


def part1():
    numbers1, numbers2 = parse_input()
    numbers1.sort()
    numbers2.sort()
    difference = sum(abs(num1 - num2) for num1, num2 in zip(numbers1, numbers2))

    return difference


def part2():
    numbers1, numbers2 = parse_input()
    count_map = Counter(numbers2)
    result = sum(num * count_map[num] for num in numbers1)

    return result


if __name__ == "__main__":
    time_and_print(part1, "Part 1")
    time_and_print(part2, "Part 2")
