"""Solution for Day 14 of 2024"""

import sys
import os
import numpy as np


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from utils import time_and_print, read_input_file

import re

def parse_input():
    content = read_input_file("2024/data/day_14.txt")
    robots = []
    for line in content.strip().split('\n'):
        match = re.match(r'p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)', line)
        if match:
            px, py, vx, vy = map(int, match.groups())
            robots.append(((px, py), (vx, vy)))
    print(f"Number of robots: {len(robots)}")
    return robots

def calculate_variance(robots):
    x_positions = [x for x, y in robots]
    y_positions = [y for x, y in robots]
    variance_x = np.var(x_positions)
    variance_y = np.var(y_positions)
    return variance_x + variance_y

def generate_grid_string(robots, width, height):
    grid = [['.' for _ in range(width)] for _ in range(height)]
    for x, y in robots:
        grid[y][x] = '#'
    return "\n".join("".join(row) for row in grid)

def simulate_robots(robots, width, height, seconds, variance_threshold):
    for step in range(seconds + 1):
        new_positions = []
        for (px, py), (vx, vy) in robots:
            new_px = (px + vx) % width
            new_py = (py + vy) % height
            new_positions.append((new_px, new_py))
        robots = [(pos, vel) for pos, (_, vel) in zip(new_positions, robots)]
        
        # Calculate and check variance
        positions = [pos for pos, _ in robots]
        variance = calculate_variance(positions)
        if variance < variance_threshold:
            print(f"Iteration {step}: Variance is considerably lower ({variance})")
            grid_string = generate_grid_string(positions, width, height)
            print(grid_string)
        
        # save_grid_to_image(positions, width, height, step)
    return [pos for pos, _ in robots]

def count_robots_in_quadrants(robots, width, height):
    mid_x, mid_y = width // 2, height // 2
    quadrants = [0, 0, 0, 0]  # Top-left, Top-right, Bottom-left, Bottom-right

    for x, y in robots:
        if x == mid_x or y == mid_y:
            continue
        if x < mid_x and y < mid_y:
            quadrants[0] += 1
        elif x >= mid_x and y < mid_y:
            quadrants[1] += 1
        elif x < mid_x and y >= mid_y:
            quadrants[2] += 1
        elif x >= mid_x and y >= mid_y:
            quadrants[3] += 1

    return quadrants

def calculate_safety_factor(quadrants):
    factor = 1
    for count in quadrants:
        factor *= count
    return factor

def part1():
    robots = parse_input()
    width, height = 101, 103
    seconds = 100
    variance_threshold = 1000  # Adjust this threshold as needed
    final_positions = simulate_robots(robots, width, height, seconds, variance_threshold)
    quadrants = count_robots_in_quadrants(final_positions, width, height)
    safety_factor = calculate_safety_factor(quadrants)
    return safety_factor

def part2():
    robots = parse_input()
    width, height = 101, 103
    seconds = 10000
    variance_threshold = 1000  # Adjust this threshold as needed
    final_positions = simulate_robots(robots, width, height, seconds, variance_threshold)
    quadrants = count_robots_in_quadrants(final_positions, width, height)
    safety_factor = calculate_safety_factor(quadrants)
    return safety_factor

if __name__ == "__main__":
    time_and_print(part1, "Part 1")
    time_and_print(part2, "Part 2")
