import heapq
from collections import defaultdict
import math

with open('2024/data/day_16.txt') as f:
    grid = f.read().splitlines()

directions = {(-1,0),(0,-1),(0,1),(1,0)}

walls = {(i,j) for i,line in enumerate(grid) for j,char in enumerate(line) if char=='#'}

start = [(i,j) for i,line in enumerate(grid) for j,char in enumerate(line) if char=='S']
assert len(start) == 1
start = start[0]+(0,1)

end = [(i,j) for i,line in enumerate(grid) for j,char in enumerate(line) if char=='E']
assert len(end) == 1
end = end[0]
ends = [end+direction for direction in directions]

def dijkstra_function(start, ends, distance_function):
    visited = {}
    queue = [(0, start)]
    time_dict = defaultdict(lambda: math.inf, {start: 0})
    came_from = {}  # To reconstruct the path

    while queue:
        time, loc = heapq.heappop(queue)
        if loc in visited:
            continue
        visited[loc] = 1
        if loc in ends:
            path = []
            while loc in came_from:
                path.append(loc)
                loc = came_from[loc]
            path.append(start)
            path.reverse()
            return time, path
        neighbours = distance_function(loc)
        for coord, distance in neighbours:
            newtime = time + distance
            if coord not in visited:
                if newtime < time_dict[coord]:
                    time_dict[coord] = newtime
                    came_from[coord] = loc
                    heapq.heappush(queue, (newtime, coord))

def dijkstra_function_2(starts, distance_function):
    visited = {}
    queue = [(0, start) for start in starts]
    time_dict = defaultdict(lambda: math.inf, {start: 0 for start in starts})
    output = dict()
    while queue:
        time, loc = heapq.heappop(queue)
        if loc in visited:
            continue
        else:
            output[loc] = time
        visited[loc] = 1
        neighbours = distance_function(loc)
        for coord, distance in neighbours:
            newtime = time + distance
            if coord not in visited:
                if newtime < time_dict[coord]:
                    time_dict[coord] = newtime
                    heapq.heappush(queue, (newtime, coord))
    return output

def distance_function(loc):
    x, y, dx, dy = loc
    output = []
    if (x + dx, y + dy) not in walls:
        output.append([(x + dx, y + dy, dx, dy), 1])
    for newdx, newdy in directions:
        if (newdx, newdy) != (dx, dy):
            output.append([(x, y, newdx, newdy), 1000])
    return output

answer, path = dijkstra_function(start, ends, distance_function)
print(f"Answer: {answer}")
print("Path taken:")
for step in path:
    print(step)

distance_from_start = dijkstra_function_2([start], distance_function)
distance_from_end = dijkstra_function_2(ends, distance_function)

coords = set()
for (x, y, dx, dy) in distance_from_start:
    if distance_from_start[(x, y, dx, dy)] + distance_from_end[(x, y, -dx, -dy)] == answer:
        coords.add((x, y))
print(len(coords))