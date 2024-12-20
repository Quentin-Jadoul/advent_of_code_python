"""Solution for Day 8 of 2024"""

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from utils import time_and_print, read_input_file

def parse_input():
    content = read_input_file("2024/data/day_08.txt")
    return content.strip().split('\n')

def find_antennas(map_data):
    antennas = {}
    for y, row in enumerate(map_data):
        for x, char in enumerate(row):
            if char != '.':
                if char not in antennas:
                    antennas[char] = []
                antennas[char].append((x, y))
    return antennas

def add_antinode(antinodes, x, y, delta_x, delta_y, max_x, max_y):
    while 0 <= x < max_x and 0 <= y < max_y:
        antinodes.add((x, y))
        x += delta_x
        y += delta_y

def calculate_antinode_positions(antennas, max_x, max_y, part):
    antinodes = set()
    for freq, positions in antennas.items():
        if len(positions) > 1:
            for i in range(len(positions)):
                for j in range(i + 1, len(positions)):
                    x1, y1 = positions[i]
                    x2, y2 = positions[j]
                    delta_x = x2 - x1
                    delta_y = y2 - y1
                    if part == 1:
                        # Calculate antinode positions by applying the same delta and inverse delta
                        antinodes.add((x2 + delta_x, y2 + delta_y))
                        antinodes.add((x1 - delta_x, y1 - delta_y))
                    elif part == 2:
                        # Calculate antinode positions by extending the delta in both directions
                        add_antinode(antinodes, x2, y2, delta_x, delta_y, max_x, max_y)
                        add_antinode(antinodes, x1, y1, -delta_x, -delta_y, max_x, max_y)
            if part == 2:
                # Add the positions of the antennas themselves as antinodes
                for position in positions:
                    antinodes.add(position)
    return antinodes

def part1():
    map_data = parse_input()
    antennas = find_antennas(map_data)
    max_y = len(map_data)
    max_x = len(map_data[0])
    antinodes = calculate_antinode_positions(antennas, max_x, max_y, part=1)
    
    # Filter antinodes within the bounds of the map
    valid_antinodes = {(x, y) for x, y in antinodes if 0 <= x < max_x and 0 <= y < max_y}
    
    return len(valid_antinodes)

def part2():
    map_data = parse_input()
    antennas = find_antennas(map_data)
    max_y = len(map_data)
    max_x = len(map_data[0])
    antinodes = calculate_antinode_positions(antennas, max_x, max_y, part=2)
    
    # Filter antinodes within the bounds of the map
    valid_antinodes = {(x, y) for x, y in antinodes if 0 <= x < max_x and 0 <= y < max_y}
    
    return len(valid_antinodes)

if __name__ == "__main__":
    time_and_print(part1, "Part 1")
    time_and_print(part2, "Part 2")