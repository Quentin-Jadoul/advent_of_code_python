"""Solution for Day 6 of 2024"""

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from utils import time_and_print, read_input_file

def parse_input():
    content = read_input_file("2024/data/day_06.txt")
    return content

def turn_right(direction):
    directions = '^>v<'
    return directions[(directions.index(direction) + 1) % 4]

def move_forward(position, direction):
    r, c = position
    if direction == '^':
        return (r - 1, c)
    elif direction == '>':
        return (r, c + 1)
    elif direction == 'v':
        return (r + 1, c)
    elif direction == '<':
        return (r, c - 1)

def is_within_bounds(position, map_grid):
    r, c = position
    return 0 <= r < len(map_grid) and 0 <= c < len(map_grid[0])

def predict_guard_path(map_str):
    map_grid, start_pos, direction = parse_map(map_str)
    visited_positions = set()
    current_pos = start_pos
    visited_positions.add(current_pos)
    
    while True:
        next_pos = move_forward(current_pos, direction)
        if not is_within_bounds(next_pos, map_grid):
            break
        if map_grid[next_pos[0]][next_pos[1]] == '#':
            direction = turn_right(direction)
        else:
            current_pos = next_pos
            visited_positions.add(current_pos)
    
    # Mark visited positions on the map
    for r, c in visited_positions:
        map_grid[r][c] = 'X'
    
    # Print the final map
    for row in map_grid:
        print(''.join(row))
    
    return len(visited_positions)

def simulate_guard(map_grid, start_pos, direction):
    visited_positions = set()
    current_pos = start_pos
    visited_positions.add((current_pos, direction))
    
    while True:
        next_pos = move_forward(current_pos, direction)
        if not is_within_bounds(next_pos, map_grid):
            break
        if map_grid[next_pos[0]][next_pos[1]] == '#':
            direction = turn_right(direction)
        else:
            current_pos = next_pos
            if (current_pos, direction) in visited_positions:
                return True  # Guard is stuck in a loop
            visited_positions.add((current_pos, direction))
    
    return False  # Guard is not stuck in a loop

def find_obstruction_positions(map_str):
    map_grid, start_pos, direction = parse_map(map_str)
    visited_positions = set()
    current_pos = start_pos
    visited_positions.add(current_pos)
    
    # First, determine the original path of the guard
    while True:
        next_pos = move_forward(current_pos, direction)
        if not is_within_bounds(next_pos, map_grid):
            break
        if map_grid[next_pos[0]][next_pos[1]] == '#':
            direction = turn_right(direction)
        else:
            current_pos = next_pos
            visited_positions.add(current_pos)
    
    possible_positions = set()
    for pos in visited_positions:
        r, c = pos
        if (r, c) != start_pos:
            # Simulate adding an obstruction at (r, c)
            map_grid[r][c] = '#'
            if simulate_guard(map_grid, start_pos, direction):
                possible_positions.add((r, c))
            # Remove the obstruction
            map_grid[r][c] = '.'
    
    return len(possible_positions)

def parse_map(map_str):
    lines = map_str.strip().split('\n')
    map_grid = [list(line) for line in lines]
    start_pos = None
    direction = None
    for r, row in enumerate(map_grid):
        for c, cell in enumerate(row):
            if cell in '^>v<':
                start_pos = (r, c)
                direction = cell
                map_grid[r][c] = '.'
                break
        if start_pos:
            break
    return map_grid, start_pos, direction

def part1():
    map_str = parse_input()
    result = predict_guard_path(map_str)
    return result

def part2():
    map_str = parse_input()
    result = find_obstruction_positions(map_str)
    return result

if __name__ == "__main__":
    time_and_print(part1, "Part 1")
    time_and_print(part2, "Part 2")