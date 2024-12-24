disk = ''

def read_input(file_path: str) -> list[str]:
    with open(file_path, 'r') as file:
        return file.read().strip().split('\n')

def process_input(input_data: list[str]) -> str:
    return input_data[0]

def solve_part1() -> int:
    expanded_disk = []
    id_num = 0
    i = 0

    while i < len(disk):
        if i % 2 == 0:
            # Represents a block
            expanded_disk.extend([str(id_num)] * int(disk[i]))
            id_num += 1
        else:
            # Represents free space
            expanded_disk.extend(['.'] * int(disk[i]))
        i += 1

    free_space = expanded_disk.index('.')
    for i in reversed(range(len(expanded_disk))):
        if expanded_disk[i] != '.':
            expanded_disk[free_space] = expanded_disk[i]
            expanded_disk[i] = '.'
            while expanded_disk[free_space] != '.':
                free_space += 1
            if i - free_space <= 1:
                break

    checksum = sum(i * int(char) for i, char in enumerate(expanded_disk) if char != '.')

    return checksum

def solve_part2():
    pass

if __name__ == "__main__":
    input_data = read_input('/Users/mattfree/Desktop/AdventOfCode/day09/input.txt')
    disk = process_input(input_data)

    result_part1 = solve_part1()
    print("Part 1:", result_part1)

    result_part2 = solve_part2()
    print("Part 2:", result_part2)