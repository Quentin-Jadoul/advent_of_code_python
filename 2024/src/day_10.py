"""Solution for Day 10 of 2024"""

import sys
import os
from collections import deque

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from utils import time_and_print, read_input_file

def parse_input():
    content = read_input_file("2024/data/day_10.txt")
    return [list(map(int, line.strip())) for line in content.splitlines()]

def bfs(map, start):
    rows, cols = len(map), len(map[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    queue = deque([start])
    visited = set([start])
    reachable_nines = set()

    while queue:
        x, y = queue.popleft()
        if map[x][y] == 9:
            reachable_nines.add((x, y))
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visited:
                if map[nx][ny] == map[x][y] + 1:
                    visited.add((nx, ny))
                    queue.append((nx, ny))
    
    return reachable_nines

def calculate_scores(map):
    rows, cols = len(map), len(map[0])
    trailheads = [(x, y) for x in range(rows) for y in range(cols) if map[x][y] == 0]
    total_score = 0

    for trailhead in trailheads:
        reachable_nines = bfs(map, trailhead)
        total_score += len(reachable_nines)
    
    return total_score

def dfs(map, x, y, visited):
    rows, cols = len(map), len(map[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    if map[x][y] == 9:
        return 1
    count = 0
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visited:
            if map[nx][ny] == map[x][y] + 1:
                visited.add((nx, ny))
                count += dfs(map, nx, ny, visited)
                visited.remove((nx, ny))
    return count

def calculate_ratings(map):
    rows, cols = len(map), len(map[0])
    trailheads = [(x, y) for x in range(rows) for y in range(cols) if map[x][y] == 0]
    total_rating = 0

    for trailhead in trailheads:
        x, y = trailhead
        visited = set([(x, y)])
        rating = dfs(map, x, y, visited)
        total_rating += rating
    
    return total_rating

def part1():
    map = parse_input()
    total_score = calculate_scores(map)
    print(total_score)

def part2():
    map = parse_input()
    total_rating = calculate_ratings(map)
    print(total_rating)

if __name__ == "__main__":
    time_and_print(part1, "Part 1")
    time_and_print(part2, "Part 2")