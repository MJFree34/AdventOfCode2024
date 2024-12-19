def read_input(file_path: str) -> list[str]:
    with open(file_path, 'r') as file:
        return file.readlines()

def process_input(input_data):
    return input_data.split('\n')

def solve_part1(data):
    pass

def solve_part2(data):
    pass

if __name__ == "__main__":
    input_data = read_input('/Users/mattfree/Desktop/AdventOfCode/dayXX/input.txt')
    data = process_input(input_data)

    result_part1 = solve_part1(data)
    print("Part 1:", result_part1)

    result_part2 = solve_part2(data)
    print("Part 2:", result_part2)