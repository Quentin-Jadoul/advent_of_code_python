"""Solution for Day 12 of 2024"""

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from utils import time_and_print, read_input_file

def parse_input():
    content = read_input_file("2024/data/day_12.txt")
    return [list(line.strip()) for line in content.split('\n') if line.strip()]

def get_neighbors(x, y, max_x, max_y):
    neighbors = []
    if x > 0:
        neighbors.append((x-1, y))
    if x < max_x - 1:
        neighbors.append((x+1, y))
    if y > 0:
        neighbors.append((x, y-1))
    if y < max_y - 1:
        neighbors.append((x, y+1))
    return neighbors

def flood_fill(map, x, y, visited):
    plant_type = map[x][y]
    stack = [(x, y)]
    area = 0
    perimeter = 0
    while stack:
        cx, cy = stack.pop()
        if (cx, cy) in visited:
            continue
        visited.add((cx, cy))
        area += 1
        
        # Check the four sides of the current cell
        if cx == 0 or map[cx-1][cy] != plant_type:
            perimeter += 1
        if cx == len(map) - 1 or map[cx+1][cy] != plant_type:
            perimeter += 1
        if cy == 0 or map[cx][cy-1] != plant_type:
            perimeter += 1
        if cy == len(map[0]) - 1 or map[cx][cy+1] != plant_type:
            perimeter += 1
        
        # Add valid neighbors to the stack
        for nx, ny in get_neighbors(cx, cy, len(map), len(map[0])):
            if map[nx][ny] == plant_type and (nx, ny) not in visited:
                stack.append((nx, ny))
    
    return area, perimeter

def calculate_total_price(map):
    visited = set()
    total_price = 0
    for x in range(len(map)):
        for y in range(len(map[0])):
            if (x, y) not in visited:
                area, perimeter = flood_fill(map, x, y, visited)
                total_price += area * perimeter
    return total_price

def count_corners(map, x, y):
    plant_type = map[x][y]
    max_x, max_y = len(map), len(map[0])
    corners = 0

    # Define neighbor states
    top = x == 0 or map[x-1][y] != plant_type
    bottom = x == max_x - 1 or map[x+1][y] != plant_type
    left = y == 0 or map[x][y-1] != plant_type
    right = y == max_y - 1 or map[x][y+1] != plant_type

    # Convex corners (boundary intersections)
    if top and left:
        corners += 1
    if top and right:
        corners += 1
    if bottom and left:
        corners += 1
    if bottom and right:
        corners += 1

    if not top and not left:
        # Check diagonal neighbor
        if map[x-1][y-1] != plant_type:
            corners += 1
    if not top and not right:
        # Check diagonal neighbor
        if map[x-1][y+1] != plant_type:
            corners += 1
    if not bottom and not left:
        # Check diagonal neighbor
        if map[x+1][y-1] != plant_type:
            corners += 1
    if not bottom and not right:
        # Check diagonal neighbor
        if map[x+1][y+1] != plant_type:
            corners += 1

    return corners

def flood_fill_sides(map, x, y, visited):
    plant_type = map[x][y]
    stack = [(x, y)]
    area = 0
    total_corners = 0

    while stack:
        cx, cy = stack.pop()
        if (cx, cy) in visited:
            continue
        visited.add((cx, cy))
        area += 1

        # Count corners for the current cell
        total_corners += count_corners(map, cx, cy)

        # Add valid neighbors to the stack
        for nx, ny in get_neighbors(cx, cy, len(map), len(map[0])):
            if map[nx][ny] == plant_type and (nx, ny) not in visited:
                stack.append((nx, ny))

    return area, total_corners

def calculate_total_price_sides(map):
    visited = set()
    total_price = 0
    for x in range(len(map)):
        for y in range(len(map[0])):
            if (x, y) not in visited:
                area, sides = flood_fill_sides(map, x, y, visited)
                total_price += area * sides
    return total_price

def part1():
    map = parse_input()
    total_price = calculate_total_price(map)
    return total_price

def part2():
    map = parse_input()
    total_price = calculate_total_price_sides(map)
    return total_price

if __name__ == "__main__":
    time_and_print(part1, "Part 1")
    time_and_print(part2, "Part 2")