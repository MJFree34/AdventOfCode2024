class Operation:
    def __init__(self, test_value: int, numbers: list[int], concatenate: bool = False):
        self.test_value = test_value
        self.numbers = numbers
        self.concatenate = concatenate
        self.possible = self.test_possible(numbers[0], 1)

    def test_possible(self, curr_total: int, start_i: int) -> bool:
        if start_i == len(self.numbers):
            return curr_total == self.test_value
        mult_total = self.numbers[start_i] * curr_total
        add_total = self.numbers[start_i] + curr_total
        if self.concatenate:
            concatenate_total = int(str(curr_total) + str(self.numbers[start_i]))
            return self.test_possible(mult_total, start_i + 1) or self.test_possible(add_total, start_i + 1) or self.test_possible(concatenate_total, start_i + 1)
        return self.test_possible(mult_total, start_i + 1) or self.test_possible(add_total, start_i + 1)

def read_input(file_path: str) -> list[str]:
    with open(file_path, 'r') as file:
        return file.readlines()

def process_input(input_data: list[str]) -> list[list[str]]:
    return [line.split(':') for line in input_data]

def solve_part1(data: list[list[str]]) -> int:
    possible_operations_sum = 0
    for line in data:
        test_value = int(line[0])
        numbers = [int(num) for num in line[1].split()]
        operation = Operation(test_value, numbers)
        if operation.possible:
            possible_operations_sum += operation.test_value
    return possible_operations_sum

def solve_part2(data):
    possible_operations_sum = 0
    for line in data:
        test_value = int(line[0])
        numbers = [int(num) for num in line[1].split()]
        operation = Operation(test_value, numbers, concatenate=True)
        if operation.possible:
            possible_operations_sum += operation.test_value
    return possible_operations_sum

if __name__ == "__main__":
    input_data = read_input('/Users/mattfree/Desktop/AdventOfCode/day07/input.txt')
    data = process_input(input_data)

    result_part1 = solve_part1(data)
    print("Part 1:", result_part1)

    result_part2 = solve_part2(data)
    print("Part 2:", result_part2)