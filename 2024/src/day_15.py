"""Solution for Day 15 of 2024"""

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from utils import time_and_print, read_input_file

def parse_input():
    content = read_input_file("2024/data/day_15.txt")
    parts = content.strip().split('\n\n')
    warehouse_map = parts[0].split('\n')
    moves = ''.join(parts[1].split())
    return warehouse_map, moves

# def initialize_state(warehouse_map):
#     robot_pos = None
#     boxes = set()
#     for r, row in enumerate(warehouse_map):
#         for c, char in enumerate(row):
#             if char == '@':
#                 robot_pos = (r, c)
#             elif char == 'O':
#                 boxes.add((r, c))
#     return robot_pos, boxes

def simulate_movements(warehouse_map, robot_pos, boxes, moves):
    directions = {'^': (-1, 0), 'v': (1, 0), '<': (0, -1), '>': (0, 1)}
    
    for move in moves:
        dr, dc = directions[move]
        new_robot_pos = (robot_pos[0] + dr, robot_pos[1] + dc)
        
        if new_robot_pos in boxes:
            # Check if we can push all adjacent boxes
            can_push = True
            current_pos = new_robot_pos
            boxes_to_move = []
            
            while current_pos in boxes:
                next_pos = (current_pos[0] + dr, current_pos[1] + dc)
                if warehouse_map[next_pos[0]][next_pos[1]] == '#':
                    can_push = False
                    break
                boxes_to_move.append(current_pos)
                current_pos = next_pos
            
            if can_push:
                # Move all adjacent boxes
                for box_pos in reversed(boxes_to_move):
                    new_box_pos = (box_pos[0] + dr, box_pos[1] + dc)
                    boxes.remove(box_pos)
                    boxes.add(new_box_pos)
                robot_pos = new_robot_pos
        elif warehouse_map[new_robot_pos[0]][new_robot_pos[1]] != '#':
            robot_pos = new_robot_pos
    
    return robot_pos, boxes

def initialize_state(warehouse_map):
    robot_pos = None
    boxes = set()
    for r, row in enumerate(warehouse_map):
        c = 0
        while c < len(row):
            char = row[c]
            if char == '@':
                robot_pos = (r, c)
                c += 2  # Skip the next character as '@' is followed by '.'
            elif char == '[':
                boxes.add((r, c))
                c += 2  # Skip the next character as '[' is followed by ']'
            else:
                c += 1
    return robot_pos, boxes

def print_map(warehouse_map, robot_pos, boxes):
    updated_map = [list(row) for row in warehouse_map]
    
    for r, c in boxes:
        updated_map[r][c] = '['
        updated_map[r][c + 1] = ']'
    
    robot_r, robot_c = robot_pos
    updated_map[robot_r][robot_c] = '@'
    
    for row in updated_map:
        print(''.join(row))
    print()

def simulate_movements_part2(warehouse_map, robot_pos, boxes, moves):
    directions = {'^': (-1, 0), 'v': (1, 0), '<': (0, -1), '>': (0, 1)}
    
    for move in moves:
        print(f"Move: {move}")
        dr, dc = directions[move]
        new_robot_pos = (robot_pos[0] + dr, robot_pos[1] + dc)
        
        if new_robot_pos in boxes:
            # Check if we can push all adjacent boxes
            can_push = True
            current_pos = new_robot_pos
            boxes_to_move = []
            
            while current_pos in boxes:
                next_pos = (current_pos[0] + dr, current_pos[1] + dc)
                if warehouse_map[next_pos[0]][next_pos[1]] == '#' or next_pos in boxes:
                    can_push = False
                    break
                boxes_to_move.append(current_pos)
                current_pos = next_pos
            
            if can_push:
                # Move all adjacent boxes
                for box_pos in reversed(boxes_to_move):
                    new_box_pos = (box_pos[0] + dr, box_pos[1] + dc)
                    boxes.remove(box_pos)
                    boxes.add(new_box_pos)
                robot_pos = new_robot_pos
        elif warehouse_map[new_robot_pos[0]][new_robot_pos[1]] != '#':
            robot_pos = new_robot_pos
        
        # Print the map after each move
        print_map(warehouse_map, robot_pos, boxes)
    
    return robot_pos, boxes

def calculate_gps_coordinates(boxes):
    return sum(100 * r + c for r, c in boxes)

def scale_up_warehouse_map(warehouse_map):
    scaled_map = []
    for row in warehouse_map:
        scaled_row = []
        for char in row:
            if char == '#':
                scaled_row.append('##')
            elif char == 'O':
                scaled_row.append('[]')
            elif char == '.':
                scaled_row.append('..')
            elif char == '@':
                scaled_row.append('@.')
        scaled_map.append(''.join(scaled_row))
    return scaled_map

def part1():
    warehouse_map, moves = parse_input()

    robot_pos, boxes = initialize_state(warehouse_map)
    robot_pos, boxes = simulate_movements(warehouse_map, robot_pos, boxes, moves)

    result = calculate_gps_coordinates(boxes)
    print("Sum of GPS coordinates:", result)

def part2():
    warehouse_map, moves = parse_input()
    scaled_warehouse_map = scale_up_warehouse_map(warehouse_map)
    
    # Print the scaled-up warehouse map
    print("Scaled-up Warehouse Map:")
    for row in scaled_warehouse_map:
        print(row)
    print()
    
    robot_pos, boxes = initialize_state(scaled_warehouse_map)
    robot_pos, boxes = simulate_movements_part2(scaled_warehouse_map, robot_pos, boxes, moves)

    result = calculate_gps_coordinates(boxes)
    print("Sum of GPS coordinates:", result)

if __name__ == "__main__":
    time_and_print(part1, "Part 1")
    time_and_print(part2, "Part 2")