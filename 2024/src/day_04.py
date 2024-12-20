"""Solution for Day 4 of 2024"""
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from utils import time_and_print, read_input_file

def parse_input():
    content = read_input_file("2024/data/day_04.txt")
    return [line.strip() for line in content.splitlines()]

def is_valid(x, y, rows, cols):
    return 0 <= x < rows and 0 <= y < cols

def search_from(x, y, dx, dy, word, grid, rows, cols):
    word_len = len(word)
    for i in range(word_len):
        nx, ny = x + i * dx, y + i * dy
        if not is_valid(nx, ny, rows, cols) or grid[nx][ny] != word[i]:
            return False
    return True

def count_xmas(grid):
    rows = len(grid)
    cols = len(grid[0])
    word = "XMAS"
    directions = [
        (0, 1),  # right
        (1, 0),  # down
        (1, 1),  # down-right
        (1, -1), # down-left
        (0, -1), # left
        (-1, 0), # up
        (-1, -1),# up-left
        (-1, 1)  # up-right
    ]

    count = 0
    for row in range(rows):
        for col in range(cols):
            for dx, dy in directions:
                if search_from(row, col, dx, dy, word, grid, rows, cols):
                    count += 1
    return count

def search_x_mas_from(x, y, grid, rows, cols):
    patterns = [
        [(-1, -1, 'M'), (-1, 1, 'M'), (1, -1, 'S'), (1, 1, 'S')],
        [(-1, -1, 'S'), (-1, 1, 'S'), (1, -1, 'M'), (1, 1, 'M')],
        [(-1, -1, 'S'), (-1, 1, 'M'), (1, -1, 'S'), (1, 1, 'M')],
        [(-1, -1, 'M'), (-1, 1, 'S'), (1, -1, 'M'), (1, 1, 'S')],
    ]
    for pattern in patterns:
        if all(is_valid(x + dx, y + dy, rows, cols) and grid[x + dx][y + dy] == char for dx, dy, char in pattern):
            return True
    return False

def count_x_mas(grid):
    rows = len(grid)
    cols = len(grid[0])
    count = 0
    for r in range(1, rows - 1):
        for c in range(1, cols - 1):
            if grid[r][c] == 'A':
                if search_x_mas_from(r, c, grid, rows, cols):
                    count += 1
    return count

def part1():
    grid = parse_input()
    result = count_xmas(grid)
    print(f"Part 1: {result}")

def part2():
    grid = parse_input()
    result = count_x_mas(grid)
    print(f"Part 2: {result}")

if __name__ == "__main__":
    time_and_print(part1, "Part 1")
    time_and_print(part2, "Part 2")