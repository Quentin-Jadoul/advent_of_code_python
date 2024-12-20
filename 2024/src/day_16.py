"""Solution for Day 16 of 2024"""

import sys
import os
import heapq
import math
from collections import defaultdict

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from utils import time_and_print, read_input_file

def parse_input():
    content = read_input_file("2024/data/day_16.txt")
    maze = content.strip().split('\n')
    return maze

def find_start_and_end(maze):
    start = end = None
    for y, row in enumerate(maze):
        for x, char in enumerate(row):
            if char == 'S':
                start = (x, y)
            elif char == 'E':
                end = (x, y)
    return start, end

def dijkstra(maze, start, end):
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]  # East, South, West, North
    start_state = (start[0], start[1], 1, 0)  # (x, y, dx, dy)
    pq = [(0, start_state)]
    came_from = set()  # To store unique (x, y) coordinates
    time_dict = defaultdict(lambda: math.inf, {start_state: 0})
    parent_dict = {}  # To store the parent of each state

    while pq:
        time, (x, y, dx, dy) = heapq.heappop(pq)

        if (x, y) == end:
            # Backtrack to find all cells in the best paths
            current_state = (x, y, dx, dy)
            while current_state in parent_dict:
                came_from.add((current_state[0], current_state[1]))
                current_state = parent_dict[current_state]
            came_from.add((start[0], start[1]))  # Add the start state
            print(came_from)
            print(len(came_from))
            return time

        # Move forward in the current direction
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < len(maze[0]) and 0 <= new_y < len(maze) and maze[new_y][new_x] != '#':
            new_time = time + 1
            new_state = (new_x, new_y, dx, dy)
            if new_time <= time_dict[new_state]:
                if new_time < time_dict[new_state]:
                    time_dict[new_state] = new_time
                parent_dict[new_state] = (x, y, dx, dy)
                heapq.heappush(pq, (new_time, new_state))

        # Turn left or right
        for turn in [-1, 1]:
            new_direction_index = (directions.index((dx, dy)) + turn) % 4
            new_dx, new_dy = directions[new_direction_index]
            new_time = time + 1000
            new_state = (x, y, new_dx, new_dy)
            if new_time <= time_dict[new_state]:
                if new_time < time_dict[new_state]:
                    time_dict[new_state] = new_time
                parent_dict[new_state] = (x, y, dx, dy)
                heapq.heappush(pq, (new_time, new_state))

    return float('inf')

def part1():
    maze = parse_input()
    start, end = find_start_and_end(maze)
    return dijkstra(maze, start, end)

def part2():
    pass

if __name__ == "__main__":
    time_and_print(part1, "Part 1")
    time_and_print(part2, "Part 2")