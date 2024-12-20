from collections import defaultdict
import copy
from functools import cache
import heapq
from typing import Dict, List, Set, Iterator, Tuple, Optional
import sys

grid: List[List[str]] = []
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def read_input(file_path: str) -> List[str]:
    with open(file_path, 'r') as file:
        data = file.read().strip().split('\n')
    return data

def process_input(input_data: List[str]) -> List[List[str]]:
    return [list(line) for line in input_data]

def find_start_end(maze):
    for r in range(len(maze)):
        for c in range(len(maze[0])):
            if maze[r][c] == 'S':
                start = (r, c)
            if maze[r][c] == 'E':
                end = (r, c)
    return start, end

def bfs(node: Tuple[int, int]) -> Dict[Tuple[int, int], int]:
    dist_map = {node: 0}
    queue = [node]
    for r, c in queue:
        dist = dist_map[(r,c)]
        for dr, dc in dirs:
            new_r, new_c = r + dr, c + dc
            if (new_r, new_c) not in dist_map and grid[new_r][new_c] != '#':
                dist_map[(new_r, new_c)] = dist + 1
                queue.append((new_r, new_c))
    return dist_map

def test_cheats(dist_map: Dict[Tuple[int, int], int]) -> Dict[Tuple[Tuple[int, int], Tuple[int, int]], int]:
    cheats = {}
    for r, c in dist_map:
        for dr, dc in dirs:
            node_r, node_c = r + 2 * dr, c + 2 * dc
            if (node_r, node_c) in dist_map:
                if dist_map[(r, c)] > dist_map[(node_r, node_c)] + 2:
                    cheats[((r, c), (node_r, node_c))] = dist_map[(r, c)] - dist_map[(node_r, node_c)] - 2
    return cheats

def solve_part1() -> int:
    start, _ = find_start_end(grid)
    dist_map = bfs(start)
    cheats = test_cheats(dist_map)

    valid_cheats_count = 0

    for cheat in cheats:
        length = cheats[cheat]
        if length >= 100:
            valid_cheats_count += 1

    return valid_cheats_count

def test_longer_cheats(dist_map: Dict[Tuple[int, int], int]) -> Dict[Tuple[Tuple[int, int], Tuple[int, int]], int]:
    cheats = {}
    for r, c in dist_map:
        for i in range(-20, 21):
            for j in range(-20, 21):
                if abs(i) + abs(j) > 20:
                    continue
                node_r, node_c = r + i, c + j
                if (node_r, node_c) in dist_map:
                    if dist_map[(r, c)] > dist_map[(node_r, node_c)] + abs(i) + abs(j):
                        cheats[((r, c), (node_r, node_c))] = dist_map[(r, c)] - dist_map[(node_r, node_c)] - abs(i) - abs(j)
    return cheats

def solve_part2():
    start, _ = find_start_end(grid)
    dist_map = bfs(start)
    cheats = test_longer_cheats(dist_map)

    valid_cheats_count = 0

    for cheat in cheats:
        length = cheats[cheat]
        if length >= 100:
            valid_cheats_count += 1

    return valid_cheats_count

if __name__ == "__main__":
    input_data = read_input('/Users/mattfree/Desktop/AdventOfCode/day20/input.txt')
    grid = process_input(input_data)

    result_part1 = solve_part1()
    print("Part 1:", result_part1)

    result_part2 = solve_part2()
    print("Part 2:", result_part2)