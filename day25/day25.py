locks = []
keys = []

def read_input(file_path: str) -> list[str]:
    with open(file_path, 'r') as file:
        return file.read().strip()

def process_input(input_data: str) -> tuple[list[str], list[str]]:
    locks_and_keys = input_data.split('\n\n')
    locks = [x for x in locks_and_keys if x.startswith('#####')]
    keys = [x for x in locks_and_keys if x.startswith('.....')]

    # Convert locks and keys into arrays of column heights (excluding first/last row)
    locks = [[sum(1 for c in col[1:] if c == '#') for col in zip(*lock.split('\n'))] for lock in locks]
    keys = [[sum(1 for c in col[1:-1] if c == '#') for col in zip(*key.split('\n'))] for key in keys]
    
    return locks, keys

def solve_part1():
    fit_count = 0
    
    for i, lock in enumerate(locks):
        for j, key in enumerate(keys):                
            # Check if key fits lock (sum of heights <= 5 for each column)
            fits = True
            for lock_height, key_height in zip(lock, key):
                if lock_height + key_height > 5:
                    fits = False
                    break
                    
            if fits:
                fit_count += 1
                
    return fit_count

def solve_part2():
    pass

if __name__ == "__main__":
    input_data = read_input('/Users/mattfree/Desktop/AdventOfCode/day25/input.txt')
    locks, keys = process_input(input_data)

    result_part1 = solve_part1()
    print("Part 1:", result_part1)

    result_part2 = solve_part2()
    print("Part 2:", result_part2)