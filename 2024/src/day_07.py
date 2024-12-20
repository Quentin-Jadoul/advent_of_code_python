"""Solution for Day 7 of 2024"""

import sys
import os
import itertools

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from utils import time_and_print, read_input_file

def parse_input():
    content = read_input_file("2024/data/day_07.txt")
    return content.strip().split('\n')

def dfs(numbers, operators, index, current_value, test_value):
    if index == len(numbers):
        return current_value == test_value
    
    for op in operators:
        if op == '+':
            next_value = current_value + numbers[index]
        elif op == '*':
            next_value = current_value * numbers[index]
        elif op == '||':
            next_value = int(str(current_value) + str(numbers[index]))
        
        if next_value > test_value:
            continue
        
        if dfs(numbers, operators, index + 1, next_value, test_value):
            return True
    
    return False

def calculate_total_calibration_result(operators):
    equations = parse_input()
    total_calibration_result = 0
    
    for equation in equations:
        test_value, numbers = equation.split(': ')
        test_value = int(test_value)
        numbers = list(map(int, numbers.split()))
        
        if dfs(tuple(numbers), tuple(operators), 1, numbers[0], test_value):
            total_calibration_result += test_value
    
    return total_calibration_result

def part1():
    operators = ['+', '*']
    total_calibration_result = calculate_total_calibration_result(operators)
    print(f"Total Calibration Result: {total_calibration_result}")

def part2():
    operators = ['+', '*', '||']
    total_calibration_result = calculate_total_calibration_result(operators)
    print(f"Total Calibration Result: {total_calibration_result}")

if __name__ == "__main__":
    time_and_print(part1, "Part 1")
    time_and_print(part2, "Part 2")