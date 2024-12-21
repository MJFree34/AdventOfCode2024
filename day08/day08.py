map: list[list[str]] = []

def read_input(file_path: str) -> list[str]:
    with open(file_path, 'r') as file:
        return file.readlines()

def process_input(input_data: list[str]) -> list[list[str]]:
    return [list(line.strip()) for line in input_data]

def print_map():
    for row in map:
        print(''.join(row))
    print()

def find_frequencies() -> dict[str, list[tuple[int, int]]]:
    frequencies = {}
    for row in range(len(map)):
        for col in range(len(map[0])):
            if map[row][col] != '.':
                if map[row][col] not in frequencies:
                    frequencies[map[row][col]] = [(row, col)]
                else:
                    frequencies[map[row][col]].append((row, col))
    return frequencies

def add_antinode(antinode_locs: set[tuple[int, int]], node_1: tuple[int, int], node_2: tuple[int, int]):
    x1, y1 = node_1
    x2, y2 = node_2
    diff = (x1 - x2, y1 - y2)
    antinode = (x1 + diff[0], y1 + diff[1])
    if antinode[0] >= 0 and antinode[0] < len(map) and antinode[1] >= 0 and antinode[1] < len(map[0]):
        antinode_locs.add(antinode)
        map[antinode[0]][antinode[1]] = '#'

def solve_part1():
    frequencies = find_frequencies()
    
    antinode_locs = set()

    for freq in frequencies:
        nodes = frequencies[freq]
        for i in range(len(nodes) - 1):
            for j in range(i + 1, len(nodes)):
                add_antinode(antinode_locs, nodes[i], nodes[j])
                add_antinode(antinode_locs, nodes[j], nodes[i])

    return len(antinode_locs)

def solve_part2():
    frequencies = find_frequencies()
    
    antinode_locs = set()

    for freq in frequencies:
        nodes = frequencies[freq]

        for node in nodes:
            antinode_locs.add(node)
        
        for i in range(len(nodes) - 1):
            for j in range(i + 1, len(nodes)):
                x1, y1 = nodes[i]
                x2, y2 = nodes[j]
                diff = (x1 - x2, y1 - y2)

                antinode = (x1 + diff[0], y1 + diff[1])
                while antinode[0] >= 0 and antinode[0] < len(map) and antinode[1] >= 0 and antinode[1] < len(map[0]):
                    antinode_locs.add(antinode)
                    map[antinode[0]][antinode[1]] = '#'
                    antinode = (antinode[0] + diff[0], antinode[1] + diff[1])

                antinode = (x2 - diff[0], y2 - diff[1])
                while antinode[0] >= 0 and antinode[0] < len(map) and antinode[1] >= 0 and antinode[1] < len(map[0]):
                    antinode_locs.add(antinode)
                    map[antinode[0]][antinode[1]] = '#'
                    antinode = (antinode[0] - diff[0], antinode[1] - diff[1])

    return len(antinode_locs)

if __name__ == "__main__":
    input_data = read_input('/Users/mattfree/Desktop/AdventOfCode/day08/input.txt')
    map = process_input(input_data)

    result_part1 = solve_part1()
    print("Part 1:", result_part1)
    
    map = process_input(input_data)
    result_part2 = solve_part2()
    print("Part 2:", result_part2)