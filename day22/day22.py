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

def solve_part1() -> int:
    new_secret_number_sum = 0
    for secret_number in secret_numbers:
        for _ in range(2000):
            multiplied = secret_number * 64
            mixed1 = mix(secret_number, multiplied)
            pruned1 = prune(mixed1)
            divided = pruned1 // 32
            mixed2 = mix(pruned1, divided)
            pruned2 = prune(mixed2)
            multiplied2 = pruned2 * 2048
            mixed3 = mix(pruned2, multiplied2)
            pruned3 = prune(mixed3)
            secret_number = pruned3
            # print(secret_number)
        new_secret_number_sum += secret_number
    return new_secret_number_sum

def solve_part2():
    pass

if __name__ == "__main__":
    input_data = read_input('/Users/mattfree/Desktop/AdventOfCode/day22/input.txt')
    secret_numbers = process_input(input_data)

    result_part1 = solve_part1()
    print("Part 1:", result_part1)

    result_part2 = solve_part2()
    print("Part 2:", result_part2)