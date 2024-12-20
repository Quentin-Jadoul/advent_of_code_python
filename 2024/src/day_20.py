"""Solution for Day 20 of 2024"""

import sys
import os
from itertools import combinations
from collections import deque

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from utils import time_and_print, read_input_file

def parse_input():
    content = read_input_file("2024/data/day_20.txt")
    return [list(line.strip()) for line in content.split('\n')]

def calculate_distances(grid_dict, start_pos):
    dist = {start_pos: 0}
    queue = deque([start_pos])
    visited = {start_pos}
    
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    while queue:
        p = queue.popleft()
        for d in directions:
            q = (p[0] + d[0], p[1] + d[1])
            if q in grid_dict and q not in visited:
                dist[q] = dist[p] + 1
                queue.append(q)
                visited.add(q)
    
    return dist


def count_cheats(dist, max_distance):
    total_cheats = 0
    for (p, i), (q, j) in combinations(dist.items(), 2):
        # Manhattan distance between p and q
        md = abs(p[0] - q[0]) + abs(p[1] - q[1])
        if md <= max_distance:
            if (abs(i - j) - md) >= 100:
                total_cheats += 1
    return total_cheats

def calculate_solution(max_distance):
    grid = parse_input()
    grid_dict = {(i, j): c for i, row in enumerate(grid) for j, c in enumerate(row) if c != '#'}
    start_pos = next(p for p in grid_dict if grid_dict[p] == 'S')
    dist = calculate_distances(grid_dict, start_pos)
    cheat_counts = count_cheats(dist, max_distance)

    return cheat_counts

def part1():
    return calculate_solution(2)

def part2():
    return calculate_solution(20)

if __name__ == "__main__":
    time_and_print(part1, "Part 1")
    time_and_print(part2, "Part 2")