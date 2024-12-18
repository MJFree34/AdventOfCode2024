from collections import deque
from typing import List, Tuple

grid_size: int = 71
num_falling_bytes: int = 1024

def read_input(file_path: str) -> list[str]:
    with open(file_path, 'r') as file:
        return file.readlines()

def process_input(input_data: list[str]) -> List[Tuple[int, int]]:
    return [tuple(map(int, line.strip().split(','))) for line in input_data]

def print_grid(grid):
    for row in grid:
        print(''.join(row))

def bfs(grid: List[List[str]], start: Tuple[int, int], end: Tuple[int, int]) -> int:
    rows, cols = len(grid), len(grid[0])
    queue = deque([(start, 0)])
    visited = set()
    visited.add(start)

    while queue:
        (r, c), steps = queue.popleft()
        if (r, c) == end:
            return steps

        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_r, new_c = r + dr, c + dc
            if 0 <= new_r < rows and 0 <= new_c < cols and grid[new_r][new_c] == '.' and (new_r, new_c) not in visited:
                queue.append(((new_r, new_c), steps + 1))
                visited.add((new_r, new_c))

def solve_part1(coordinates: List[Tuple[int, int]]) -> int:
    grid = [['.'] * grid_size for _ in range(grid_size)]

    for i in range(num_falling_bytes):
        x, y = coordinates[i]
        grid[y][x] = '#'
    
    return bfs(grid, (0, 0), (grid_size - 1, grid_size - 1))

def solve_part2(coordinates: List[Tuple[int, int]]) -> int:
    pass

if __name__ == "__main__":
    input_data = read_input('/Users/mattfree/Desktop/AdventOfCode/day18/input.txt')
    coordinates = process_input(input_data)

    result_part1 = solve_part1(coordinates)
    print("Part 1:", result_part1)

    result_part2 = solve_part2(coordinates)
    print("Part 2:", result_part2)