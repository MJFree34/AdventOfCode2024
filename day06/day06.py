from typing import List, Tuple
from copy import deepcopy

def read_input(file_path: str) -> List[str]:
    with open(file_path, 'r') as file:
        return file.read().strip().split('\n')

def process_input(input_data: List[str]) -> List[List[str]]:
    return [list(line) for line in input_data]

def print_map(map: List[List[str]]):
    for row in map:
        print(''.join(row))

def find_guard(map: List[List[str]]) -> Tuple[Tuple[int, int], str]:
    for r in range(len(map)):
        for c in range(len(map[0])):
            if map[r][c] == '^':
                return (r, c), '^'
            elif map[r][c] == 'v':
                return (r, c), 'v'
            elif map[r][c] == '<':
                return (r, c), '<'
            elif map[r][c] == '>':
                return (r, c), '>'

def guard_on_map(map: List[List[str]], pos: tuple, orientation: str) -> bool:
    r, c = pos
    if r < 0 and orientation == '^':
        return False
    if r > len(map) - 1 and orientation == 'v':
        return False
    if c < 0 and orientation == '<':
        return False
    if c > len(map[0]) - 1 and orientation == '>':
        return False
    return True

def solve_part1(map: List[List[str]]) -> int:
    guard_pos, guard_orientation = find_guard(map)

    while guard_on_map(map, guard_pos, guard_orientation):
        r, c = guard_pos
        if guard_orientation == '^':
            if r - 1 >= 0 and map[r-1][c] == '#':
                guard_orientation = '>'
                map[r][c] = '>'
            else:
                map[r][c] = 'X'
                guard_pos = (r-1, c)
                if r - 1 >= 0:
                    map[r-1][c] = '^'
        elif guard_orientation == 'v':
            if r + 1 < len(map) and map[r+1][c] == '#':
                guard_orientation = '<'
                map[r][c] = '<'
            else:
                map[r][c] = 'X'
                guard_pos = (r+1, c)
                if r + 1 < len(map):
                    map[r+1][c] = 'v'
        elif guard_orientation == '<':
            if c - 1 >= 0 and map[r][c-1] == '#':
                guard_orientation = '^'
                map[r][c] = '^'
            else:
                map[r][c] = 'X'
                guard_pos = (r, c-1)
                if c - 1 >= 0:
                    map[r][c-1] = '<'
        elif guard_orientation == '>':
            if c + 1 < len(map[0]) and map[r][c+1] == '#':
                guard_orientation = 'v'
                map[r][c] = 'v'
            else:
                map[r][c] = 'X'
                guard_pos = (r, c+1)
                if c + 1 < len(map[0]):
                    map[r][c+1] = '>'

    pos_count = 0

    for r in range(len(map)):
        for c in range(len(map[0])):
            if map[r][c] == 'X':
                pos_count += 1

    return pos_count

def solve_part2(map: List[List[str]]) -> int:
    guard_pos, guard_orientation = find_guard(map)

    start_guard_pos = guard_pos
    start_guard_orientation = guard_orientation

    obstacle_pos_count = 0

    for out_r in range(len(map)):
        for out_c in range(len(map[0])):
            guard_pos = start_guard_pos
            guard_orientation = start_guard_orientation
            map_copy = deepcopy(map)

            if map_copy[out_r][out_c] == '#' or map_copy[out_r][out_c] == '^':
                print("Skipping", out_r, out_c)
                continue
            print("Checking obstacle at", out_r, out_c)
            map_copy[out_r][out_c] = 'O'
            hit_obstacle_count = 0

            iteration = 0

            while guard_on_map(map_copy, guard_pos, guard_orientation):
                if iteration > 100000:
                    print("Infinite loop, breaking")
                    break

                iteration += 1
                r, c = guard_pos
                if guard_orientation == '^':
                    if r - 1 >= 0 and (map_copy[r-1][c] == '#' or map_copy[r-1][c] == 'O'):
                        if map_copy[r-1][c] == 'O':
                            hit_obstacle_count += 1
                            if hit_obstacle_count > 1:
                                break

                        guard_orientation = '>'
                        map_copy[r][c] = '>'
                    else:
                        map_copy[r][c] = 'X'
                        guard_pos = (r-1, c)
                        if r - 1 >= 0:
                            map_copy[r-1][c] = '^'
                elif guard_orientation == 'v':
                    if r + 1 < len(map_copy) and (map_copy[r+1][c] == '#' or map_copy[r+1][c] == 'O'):
                        if map_copy[r+1][c] == 'O':
                            hit_obstacle_count += 1
                            if hit_obstacle_count > 1:
                                break

                        guard_orientation = '<'
                        map_copy[r][c] = '<'
                    else:
                        map_copy[r][c] = 'X'
                        guard_pos = (r+1, c)
                        if r + 1 < len(map_copy):
                            map_copy[r+1][c] = 'v'
                elif guard_orientation == '<':
                    if c - 1 >= 0 and (map_copy[r][c-1] == '#' or map_copy[r][c-1] == 'O'):
                        if map_copy[r][c-1] == 'O':
                            hit_obstacle_count += 1
                            if hit_obstacle_count > 1:
                                break

                        guard_orientation = '^'
                        map_copy[r][c] = '^'
                    else:
                        map_copy[r][c] = 'X'
                        guard_pos = (r, c-1)
                        if c - 1 >= 0:
                            map_copy[r][c-1] = '<'
                elif guard_orientation == '>':
                    if c + 1 < len(map_copy[0]) and (map_copy[r][c+1] == '#' or map_copy[r][c+1] == 'O'):
                        if map_copy[r][c+1] == 'O':
                            hit_obstacle_count += 1
                            if hit_obstacle_count > 1:
                                break

                        guard_orientation = 'v'
                        map_copy[r][c] = 'v'
                    else:
                        map_copy[r][c] = 'X'
                        guard_pos = (r, c+1)
                        if c + 1 < len(map_copy[0]):
                            map_copy[r][c+1] = '>'

            if hit_obstacle_count > 1:
                print("Hit obstacle at", r, c)
                obstacle_pos_count += 1

    return obstacle_pos_count

if __name__ == "__main__":
    input_data = read_input('/Users/mattfree/Desktop/AdventOfCode/day06/input.txt')
    map = process_input(input_data)
    print("Part 1:", solve_part1(map))
    map = process_input(input_data)
    print("Part 2:", solve_part2(map)) # slightly overestimates