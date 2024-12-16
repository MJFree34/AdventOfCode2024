import re

dim_x, dim_y = (101, 103)

def read_input(file_path):
    with open(file_path, 'r') as file:
        data = file.read().strip().split('\n')
    return data

def process_data(data):
    grid = [[[] for _ in range(dim_x)] for _ in range(dim_y)]
    for robot in data:
        x, y, vx, vy = map(int, re.findall(r'-?\d+', robot))
        grid[y][x].append((vx, vy))
    return grid

def print_grid(grid):
    for r in range(dim_y):
        for c in range(dim_x):
            print(len(grid[r][c]), end=' ')
        print()

def solve_part1(grid):
    print("Initial grid:")
    print_grid(grid)

    for sec in range(100):
        new_grid = [[[] for _ in range(dim_x)] for _ in range(dim_y)]
        for r in range(dim_y):
            for c in range(dim_x):
                for vx, vy in grid[r][c]:
                    new_r = (r + vy) % dim_y
                    new_c = (c + vx) % dim_x
                    new_grid[new_r][new_c].append((vx, vy))
        grid = new_grid
        print(f"After {sec+1} seconds:")
        print_grid(grid)
    
    top_left_count = 0
    top_right_count = 0
    bottom_left_count = 0
    bottom_right_count = 0
    for r in range(dim_y):
        for c in range(dim_x):
            if r == dim_y // 2 or c == dim_x // 2:
                continue
            elif r < dim_y // 2 and c < dim_x // 2:
                top_left_count += len(grid[r][c])
            elif r < dim_y // 2 and c > dim_x // 2:
                top_right_count += len(grid[r][c])
            elif r > dim_y // 2 and c < dim_x // 2:
                bottom_left_count += len(grid[r][c])
            elif r > dim_y // 2 and c > dim_x // 2:
                bottom_right_count += len(grid[r][c])
    print(top_left_count, top_right_count, bottom_left_count, bottom_right_count)
    return top_left_count * top_right_count * bottom_left_count * bottom_right_count

def solve_part2(grid):
    pass

if __name__ == "__main__":
    input_file = '/Users/mattfree/Desktop/AdventOfCode/day14/input.txt'
    data = read_input(input_file)
    grid = process_data(data)
    
    result_part1 = solve_part1(grid)
    print(f"Part 1: {result_part1}")
    
    result_part2 = solve_part2(grid)
    print(f"Part 2: {result_part2}")