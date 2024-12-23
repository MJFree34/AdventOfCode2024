from dataclasses import dataclass
from itertools import permutations
from functools import cache

@dataclass(frozen=True)
class Pos:
    i: int
    j: int
    def __add__(self, other):
        return Pos(self.i + other.i, self.j + other.j)
    def __sub__(self, other):
        return Pos(self.i - other.i, self.j - other.j)
    def __eq__(self, other):
        return isinstance(other, Pos) and self.i == other.i and self.j == other.j

numpad = {'7': Pos(0, 0), '8': Pos(0, 1), '9': Pos(0, 2),
          '4': Pos(1, 0), '5': Pos(1, 1), '6': Pos(1, 2),
          '1': Pos(2, 0), '2': Pos(2, 1), '3': Pos(2, 2),
                          '0': Pos(3, 1), 'A': Pos(3, 2)}
numpad_inv = {v: k for k, v in numpad.items()}

dirpad = {                '^': Pos(0, 1), 'A': Pos(0, 2),
          '<': Pos(1, 0), 'v': Pos(1, 1), '>': Pos(1, 2)}
dirpad_inv = {v: k for k, v in dirpad.items()}
dirs = {'^': Pos(-1, 0), 'v': Pos(1, 0), '<': Pos(0, -1), '>': Pos(0, 1)}

passwords: list[str] = []

def read_input(file_path: str) -> list[str]:
    with open(file_path, 'r') as file:
        return file.read().strip().split('\n')
    
@cache
def calculate_instrs(robot_id: int, curr_key: str, dest_key: str, total_robots: int) -> int:
    pad, pad_inv = (numpad, numpad_inv) if robot_id == 0 else (dirpad, dirpad_inv)
    curr_pos = pad[curr_key]
    dest_pos = pad[dest_key]
    delta = dest_pos - curr_pos
    if robot_id == total_robots - 1:
        return abs(delta.i) + abs(delta.j) + 1
    seq = []
    for _ in range(abs(delta.i)):
        seq.append('v' if delta.i > 0 else '^')
    for _ in range(abs(delta.j)):
        seq.append('>' if delta.j > 0 else '<')
    if not seq:
        return 1
    candidates = []
    for r in set(permutations(seq)):
        pos = curr_pos
        steps = 0
        for i, dir_key in enumerate(r):
            next_key = 'A' if i == 0 else r[i-1]
            steps += calculate_instrs(robot_id + 1, next_key, dir_key, total_robots)
            pos += dirs[dir_key]
            if pos not in pad_inv:
                break
        else:
            steps += calculate_instrs(robot_id + 1, r[-1], 'A', total_robots)
            candidates.append(steps)
    return min(candidates)

def solve_part1() -> int:
    total_complexity = 0
    for password in passwords:
        complexity = calculate_instrs(0, 'A', password[0], 3)
        for i in range(1, len(password)):
            complexity += calculate_instrs(0, password[i-1], password[i], 3)
        total_complexity += complexity * int(password[:-1])
    return total_complexity

def solve_part2():
    pass

if __name__ == "__main__":
    passwords = read_input('/Users/mattfree/Desktop/AdventOfCode/day21/input.txt')

    result_part1 = solve_part1()
    print("Part 1:", result_part1)

    result_part2 = solve_part2()
    print("Part 2:", result_part2)