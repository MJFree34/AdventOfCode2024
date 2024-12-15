import re

def read_input(file_path):
    with open(file_path, 'r') as file:
        data = file.read().strip().split('\n\n')
    return data

def solve_part1(data):
    total_tokens = 0
    tolerance = 0.0001
    for machine in data:
        ax, ay, bx, by, x, y = map(int, re.findall(r'(\d+)', machine))
        A = (bx * y - by * x) / (bx * ay - by * ax)
        B = (x - ax * A) / bx
        if abs(A - round(A)) < tolerance and abs(B - round(B)) < tolerance:
            total_tokens += 3 * round(A) + round(B)
    return total_tokens

def solve_part2(data):
    # Implement the solution for part 2
    pass

if __name__ == "__main__":
    input_file = '/Users/mattfree/Desktop/AdventOfCode/day13/input.txt'
    data = read_input(input_file)
    
    result_part1 = solve_part1(data)
    print(f"Part 1: {result_part1}")
    
    result_part2 = solve_part2(data)
    print(f"Part 2: {result_part2}")