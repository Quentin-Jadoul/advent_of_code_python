"""Solution for Day 2 of 2024"""

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from utils import time_and_print, read_input_file

def parse_input():
    content = read_input_file("2024/data/day_02.txt")
    lines = content.strip().split("\n")
    reports = [list(map(int, line.split())) for line in lines]
    return reports

def is_safe(report):
    increasing = all(report[i] < report[i + 1] and 1 <= report[i + 1] - report[i] <= 3 for i in range(len(report) - 1))
    decreasing = all(report[i] > report[i + 1] and 1 <= report[i] - report[i + 1] <= 3 for i in range(len(report) - 1))
    return increasing or decreasing

def can_be_safe_with_one_removal(report):
    for i in range(len(report)):
        modified_report = report[:i] + report[i+1:]
        if is_safe(modified_report):
            return True
    return False

def part1():
    reports = parse_input()
    safe_reports = sum(1 for report in reports if is_safe(report))
    return safe_reports

def part2():
    reports = parse_input()
    safe_reports = sum(1 for report in reports if is_safe(report) or can_be_safe_with_one_removal(report))
    return safe_reports

if __name__ == "__main__":
    time_and_print(part1, "Part 1")
    time_and_print(part2, "Part 2")
