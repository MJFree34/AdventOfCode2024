import re

def read_input(file_path):
    with open(file_path, 'r') as file:
        data = file.read().strip().split('\n\n')
    return data

def parsed_data(data):
    warehouse = [[char for char in line] for line in data[0].split('\n')]
    moves = [char for line in data[1].split('\n') for char in line]
    return warehouse, moves

def solve_part1(warehouse, moves):
    print("Starting:")
    print_warehouse(warehouse)

    robot_pos = None
    for r in range(len(warehouse)):
        for c in range(len(warehouse[0])):
            if warehouse[r][c] == '@':
                robot_pos = (r, c)
                break
    
    if robot_pos is None:
        raise ValueError("Robot starting position '@' not found in the warehouse.")

    for move in moves:
        robot_pos = move_robot(warehouse, robot_pos, move)
        
        print("Move:", move)
        print_warehouse(warehouse)
        
    total_gps = 0
    for r in range(len(warehouse)):
        for c in range(len(warehouse[0])):
            if warehouse[r][c] == 'O':
                total_gps += r * 100 + c

    return total_gps

def solve_part2(warehouse, moves):
    pass

def move_robot(warehouse, robot_pos, direction):
    directions = {
        '^': (-1, 0),
        'v': (1, 0),
        '<': (0, -1),
        '>': (0, 1)
    }
    
    delta = directions[direction]
    new_pos = (robot_pos[0] + delta[0], robot_pos[1] + delta[1])
    number_of_boxes = 0

    r, c = new_pos
    while 0 <= r < len(warehouse) and 0 <= c < len(warehouse[0]):
        if warehouse[r][c] == '#':
            number_of_boxes = -1
            break
        elif warehouse[r][c] == 'O':
            number_of_boxes += 1
        elif warehouse[r][c] == '.':
            break
        r += delta[0]
        c += delta[1]

    if number_of_boxes != -1:
        warehouse[new_pos[0]][new_pos[1]] = '@'
        warehouse[robot_pos[0]][robot_pos[1]] = '.'
        robot_pos = new_pos

        if number_of_boxes != 0:
            final_pos = (new_pos[0] + delta[0] * number_of_boxes, new_pos[1] + delta[1] * number_of_boxes)
            warehouse[final_pos[0]][final_pos[1]] = 'O'

    return robot_pos

def print_warehouse(warehouse):
    for row in warehouse:
        print(''.join(row))

if __name__ == "__main__":
    input_file = '/Users/mattfree/Desktop/AdventOfCode/day15/input.txt'
    data = read_input(input_file)
    warehouse, moves = parsed_data(data)
    
    result_part1 = solve_part1(warehouse, moves)
    print(f"Part 1: {result_part1}")
    
    result_part2 = solve_part2(warehouse, moves)
    print(f"Part 2: {result_part2}")