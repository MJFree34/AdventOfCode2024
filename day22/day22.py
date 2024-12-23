from collections import defaultdict
from functools import cache

secret_numbers = []

def read_input(file_path: str) -> list[str]:
    with open(file_path, 'r') as file:
        return file.read().strip()

def process_input(input_data: str) -> list[int]:
    return list(map(int, input_data.split('\n')))

def mix(num1: int, num2: int) -> int:
    return num1 ^ num2

def prune(num: int) -> int:
    return num % 16777216

@cache
def generate_secret_number(secret_number: int) -> int:
    multiplied = secret_number * 64
    mixed1 = mix(secret_number, multiplied)
    pruned1 = prune(mixed1)
    divided = pruned1 // 32
    mixed2 = mix(pruned1, divided)
    pruned2 = prune(mixed2)
    multiplied2 = pruned2 * 2048
    mixed3 = mix(pruned2, multiplied2)
    pruned3 = prune(mixed3)
    return pruned3

def solve_part1() -> int:
    new_secret_number_sum = 0
    for secret_number in secret_numbers:
        for _ in range(2000):
            secret_number = generate_secret_number(secret_number)
        new_secret_number_sum += secret_number
    return new_secret_number_sum

def solve_part2() -> int:
    max_bananas_dict = defaultdict(int)

    for secret_number in secret_numbers:
        nums = []
        diffs = []

        for _ in range(2000):
            new_secret_number = generate_secret_number(secret_number)
            old_ones_digit = secret_number % 10
            new_ones_digit = new_secret_number % 10
            diff = new_ones_digit - old_ones_digit
            nums.append(new_ones_digit)
            diffs.append(diff)
            secret_number = new_secret_number

        seen = set()

        for i in range(3, 2000):
            diff_list = tuple(diffs[i-3:i+1])

            if diff_list not in seen:
                max_bananas_dict[diff_list] += nums[i]
                seen.add(diff_list)

    return max(max_bananas_dict.values())

if __name__ == "__main__":
    input_data = read_input('/Users/mattfree/Desktop/AdventOfCode/day22/input.txt')
    secret_numbers = process_input(input_data)

    result_part1 = solve_part1()
    print("Part 1:", result_part1)

    result_part2 = solve_part2()
    print("Part 2:", result_part2)