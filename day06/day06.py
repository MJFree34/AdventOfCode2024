from typing import List

def read_input(file_path: str) -> List[str]:
    with open(file_path, 'r') as file:
        return file.read().strip().split('\n')

def process_input(input_data: List[str]) -> List[List[str]]:
    return [list(line) for line in input_data]

def print_map(map: List[List[str]]):
    for row in map:
        print(''.join(row))

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
    for r in range(len(map)):
        for c in range(len(map[0])):
            if map[r][c] == '^':
                guard_pos = (r, c)
                guard_orientation = '^'

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

def solve_part2(data):
    # Implement the solution for part 2
    pass

if __name__ == "__main__":
    input_data = read_input('/Users/mattfree/Desktop/AdventOfCode/day06/input.txt')
    map = process_input(input_data)
    print("Part 1:", solve_part1(map))
    print("Part 2:", solve_part2(map))