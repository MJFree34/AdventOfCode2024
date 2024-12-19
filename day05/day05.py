from collections import defaultdict, deque

def read_input(file_path):
    before_rules = defaultdict(set)
    after_rules = defaultdict(set)
    updates = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            if '|' in line:
                parts = line.strip().split('|')
                if len(parts) == 2 and parts[0].isdigit() and parts[1].isdigit():
                    before_rules[int(parts[1])].add(int(parts[0]))
                    after_rules[int(parts[0])].add(int(parts[1]))
            elif ',' in line:
                parts = line.strip().split(',')
                updates.append(list(map(int, parts)))
    return before_rules, after_rules, updates

def solve_part1(before_rules, updates):
    sorted_middle_pages_sum = 0

    for update in updates:
        is_sorted = True

        for i, x in enumerate(update):
            for j, y in enumerate(update):
                if i < j and y in before_rules[x]:
                    is_sorted = False
                    break
            if not is_sorted:
                break
        
        if is_sorted:
            sorted_middle_pages_sum += update[len(update) // 2]
    
    return sorted_middle_pages_sum

def solve_part2(before_rules, after_rules, updates):
    pass

if __name__ == "__main__":
    file_path = '/Users/mattfree/Desktop/AdventOfCode/day05/input.txt'
    before_rules, after_rules, updates = read_input(file_path)

    part1_result = solve_part1(before_rules, updates)
    print(f"Part 1: {part1_result}")