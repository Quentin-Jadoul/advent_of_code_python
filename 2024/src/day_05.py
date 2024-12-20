"""Solution for Day 5 of 2024"""

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from utils import time_and_print, read_input_file

from collections import defaultdict, deque

def topological_sort(pages, rules):
    graph = defaultdict(list)
    in_degree = {page: 0 for page in pages}
    
    for x, y in rules:
        if x in pages and y in pages:
            graph[x].append(y)
            in_degree[y] += 1
    
    queue = deque([page for page in pages if in_degree[page] == 0])
    sorted_pages = []
    
    while queue:
        node = queue.popleft()
        sorted_pages.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    return sorted_pages

def parse_input():
    content = read_input_file("2024/data/day_05.txt")
    rules_section, updates_section = content.strip().split("\n\n")
    
    rules = []
    for line in rules_section.split("\n"):
        x, y = map(int, line.split("|"))
        rules.append((x, y))
    
    updates = []
    for line in updates_section.split("\n"):
        updates.append(list(map(int, line.split(","))))
    
    return rules, updates

def is_correctly_ordered(update, rules):
    index_map = {page: i for i, page in enumerate(update)}
    for x, y in rules:
        if x in index_map and y in index_map:
            if index_map[x] > index_map[y]:
                return False
    return True

def part1():
    rules, updates = parse_input()
    middle_pages_sum = 0
    
    for update in updates:
        if is_correctly_ordered(update, rules):
            middle_page = update[len(update) // 2]
            middle_pages_sum += middle_page
    
    return middle_pages_sum

def part2():
    rules, updates = parse_input()
    middle_pages_sum = 0
    
    for update in updates:
        if not is_correctly_ordered(update, rules):
            sorted_update = topological_sort(update, rules)
            middle_page = sorted_update[len(sorted_update) // 2]
            middle_pages_sum += middle_page
    
    return middle_pages_sum

if __name__ == "__main__":
    time_and_print(part1, "Part 1")
    time_and_print(part2, "Part 2")
