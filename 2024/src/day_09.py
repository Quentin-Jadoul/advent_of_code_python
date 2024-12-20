"""Solution for Day 9 of 2024"""

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from utils import time_and_print, read_input_file

def parse_input():
    content = read_input_file("2024/data/day_09.txt")
    return content

def parse_disk_map(disk_map):
    blocks = []
    file_id = 0
    i = 0
    while i < len(disk_map):
        file_length = int(disk_map[i])
        i += 1
        if i < len(disk_map):
            free_length = int(disk_map[i])
            i += 1
        else:
            free_length = 0
        blocks.extend([str(file_id)] * file_length)
        blocks.extend(['.'] * free_length)
        file_id += 1

    return blocks

def compact_disk(blocks):
    n = len(blocks)
    last_non_free_index = n - 1  # Pointer to track the last non-free block from the end

    for i in range(n):
        if blocks[i] == '.':
            # Find the last non-free block
            while last_non_free_index > i and blocks[last_non_free_index] == '.':
                last_non_free_index -= 1
            if last_non_free_index > i:
                # Swap the free space with the last non-free block
                blocks[i], blocks[last_non_free_index] = blocks[last_non_free_index], blocks[i]
                last_non_free_index -= 1

    return blocks

def compact_disk_whole_files(blocks):
    n = len(blocks)
    file_positions = {}
    free_spaces = []

    # Identify positions of files and free spaces
    i = 0
    while i < n:
        if blocks[i] != '.':
            file_id = blocks[i]
            start = i
            while i < n and blocks[i] == file_id:
                i += 1
            end = i
            file_positions[file_id] = (start, end)
        else:
            start = i
            while i < n and blocks[i] == '.':
                i += 1
            end = i
            free_spaces.append((start, end))

    # Sort files by decreasing file ID number
    sorted_files = sorted(file_positions.items(), key=lambda x: -int(x[0]))

    # Move files to the leftmost span of free space blocks that could fit the file
    for file_id, (start, end) in sorted_files:
        file_length = end - start
        for free_start, free_end in free_spaces:
            free_length = free_end - free_start
            if free_length >= file_length and free_start < start:
                # Move the file
                blocks[free_start:free_start + file_length] = [file_id] * file_length
                blocks[start:end] = ['.'] * file_length
                # Update free spaces
                free_spaces.append((start, end))
                free_spaces.remove((free_start, free_end))
                if free_length > file_length:
                    free_spaces.append((free_start + file_length, free_end))
                free_spaces.sort()
                break

    return blocks

def calculate_checksum(blocks):
    checksum = 0
    for i, block in enumerate(blocks):
        if block != '.':
            checksum += i * int(block)
    return checksum

def part1():
    disk_map = parse_input()
    blocks = parse_disk_map(disk_map)
    compacted_blocks = compact_disk(blocks)
    checksum = calculate_checksum(compacted_blocks)
    return checksum

def part2():
    disk_map = parse_input()
    blocks = parse_disk_map(disk_map)
    compacted_blocks = compact_disk_whole_files(blocks)
    checksum = calculate_checksum(compacted_blocks)
    return checksum

if __name__ == "__main__":
    time_and_print(part1, "Part 1")
    time_and_print(part2, "Part 2")
