from functools import cache
from typing import Dict, List, Tuple

towels: List[str] = []
designs: List[str] = []

def read_input(file_path: str) -> List[str]:
    with open(file_path, 'r') as file:
        return file.read().strip().split('\n\n')

def process_input(input_data: List[str]) -> Tuple[List[str], List[str]]:
    towels = input_data[0].split(', ')
    designs = input_data[1].split('\n')
    return towels, designs

@cache
def is_possible(design: str) -> bool:
    if not design:
        return True
    return any(is_possible(design[len(towel):]) 
              for towel in towels 
              if design.startswith(towel))

def solve_part1() -> int:
    return sum(is_possible(design) for design in designs)

def solve_part2():
    pass

if __name__ == "__main__":
    input_data = read_input('/Users/mattfree/Desktop/AdventOfCode/day19/input.txt')
    towels, designs = process_input(input_data)

    result_part1 = solve_part1()
    print("Part 1:", result_part1)

    result_part2 = solve_part2()
    print("Part 2:", result_part2)