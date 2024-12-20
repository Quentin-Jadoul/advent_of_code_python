"""Solution for Day 18 of 2024"""

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from utils import time_and_print, read_input_file

from collections import deque

def parse_input():
    content = read_input_file("2024/data/day_18.txt")
    return [tuple(map(int, line.split(','))) for line in content.strip().split('\n')]

def find_path(corrupted_cells, grid_size):
    start = (0, 0)
    end = (70, 70)
    queue = deque([(start, [])])
    visited = set([start])

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right

    while queue:
        (x, y), path = queue.popleft()
        if (x, y) == end:
            return path + [(x, y)]  # Return the path including the end

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < grid_size and 0 <= ny < grid_size and (nx, ny) not in corrupted_cells and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append(((nx, ny), path + [(x, y)]))

    return None  # No path found

def part1():
    byte_positions = parse_input()
    grid_size = 71  # 0 to 70 inclusive
    corrupted_cells = set()

    # Mark corrupted positions
    for x, y in byte_positions[:1024]:
        corrupted_cells.add((x, y))

    # Find the shortest path
    path = find_path(corrupted_cells, grid_size)
    if path:
        print(f"Minimum steps to reach the exit: {len(path) - 1}")
        return len(path) - 1
    else:
        print("No path found to the exit.")
        return -1

def part2():
    byte_positions = parse_input()
    grid_size = 71  # 0 to 70 inclusive
    corrupted_cells = set()

    # Mark initial corrupted positions
    for x, y in byte_positions[:1024]:
        corrupted_cells.add((x, y))

    # Find the initial path
    path = find_path(corrupted_cells, grid_size)
    if not path:
        print("Initial path is already blocked.")
        return ""

    # Simulate falling bytes starting from byte 1024
    for i, (x, y) in enumerate(byte_positions[1024:], start=1024):
        corrupted_cells.add((x, y))
        if (x, y) in path:
            path = find_path(corrupted_cells, grid_size)
            if not path:
                print(f"First byte that blocks the path: {x},{y}")
                return f"{x},{y}"

    print("No byte blocks the path.")
    return ""

if __name__ == "__main__":
    time_and_print(part1, "Part 1")
    time_and_print(part2, "Part 2")