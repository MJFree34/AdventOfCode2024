import heapq
from collections import defaultdict
from collections.abc import Iterator

def read_input(file_path):
    with open(file_path, 'r') as file:
        data = file.read().strip().split('\n')
    return data

def parse_input(input_data):
    return [list(line) for line in input_data]

def find_start_end(maze):
    for r in range(len(maze)):
        for c in range(len(maze[0])):
            if maze[r][c] == 'S':
                start = (r, c)
            if maze[r][c] == 'E':
                end = (r, c)
    return start, end

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def dijkstras(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    open_set = []
    heapq.heappush(open_set, (0, start, 'R'))  # (current_cost, position, direction)
    g_score = {(start, 'R'): 0}
    prev_states = defaultdict(set)
    
    while open_set:
        current_cost, current, current_dir = heapq.heappop(open_set)

        if current == end:
            break

        for dr, dc, direction in [(-1, 0, 'U'), (1, 0, 'D'), (0, -1, 'L'), (0, 1, 'R')]:
            neighbor = (current[0] + dr, current[1] + dc)
            if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols and maze[neighbor[0]][neighbor[1]] != '#':
                move_cost = 1
                if current_dir and direction != current_dir:
                    move_cost += 1000  # Cost for making a turn
                tentative_g_score = g_score.get((current, current_dir), float('inf')) + move_cost
                neighbor_state = (neighbor, direction)
                prev_g_score = g_score.get(neighbor_state, float('inf'))
                if tentative_g_score < prev_g_score:
                    g_score[neighbor_state] = tentative_g_score
                    heapq.heappush(open_set, (tentative_g_score, neighbor, direction))
                    prev_states[neighbor_state].add((current, current_dir))
                elif tentative_g_score == prev_g_score:
                    prev_states[neighbor_state].add((current, current_dir))
    
    current_state = (current, current_dir)

    def walk(state) -> Iterator:
        node, *_ = state
        if node == start:
            yield [state]
            return
        for prev_state in prev_states[state]:
            for path in walk(prev_state):
                yield path + [state]

    return current_cost, walk(current_state)

def solve_part1(maze):
    start, end = find_start_end(maze)
    score, _ = dijkstras(maze, start, end)
    return score

def solve_part2(maze):
    start, end = find_start_end(maze)
    _, paths = dijkstras(maze, start, end)
    return len({pos for path in paths for pos, _ in path})

if __name__ == "__main__":
    input_data = read_input('/Users/mattfree/Desktop/AdventOfCode/day16/input.txt')
    
    maze = parse_input(input_data)
    
    result_part1 = solve_part1(maze)
    print(f"Part 1: {result_part1}")
    
    result_part2 = solve_part2(maze)
    print(f"Part 2: {result_part2}")