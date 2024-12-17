import heapq

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

def a_star_search(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    open_set = []
    heapq.heappush(open_set, (0, start, 'R'))  # (f_score, position, direction)
    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, end)}
    
    while open_set:
        current_f, current, current_dir = heapq.heappop(open_set)

        if current == end:
            path = []
            while (current, current_dir) in came_from:
                path.append(current)
                current, current_dir = came_from[(current, current_dir)]
            path.append(start)
            path.reverse()
            return path, current_f
        
        for dr, dc, direction in [(-1, 0, 'U'), (1, 0, 'D'), (0, -1, 'L'), (0, 1, 'R')]:
            neighbor = (current[0] + dr, current[1] + dc)
            if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols and maze[neighbor[0]][neighbor[1]] != '#':
                move_cost = 1
                if current_dir and direction != current_dir:
                    move_cost += 1000  # Cost for making a turn
                tentative_g_score = g_score.get(current, float('inf')) + move_cost
                if tentative_g_score < g_score.get(neighbor, float('inf')):
                    came_from[neighbor] = (current, current_dir)
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = tentative_g_score + heuristic(neighbor, end)
                    heapq.heappush(open_set, (f_score[neighbor], neighbor, direction))

    return None, None

def solve_part1(maze):
    start, end = find_start_end(maze)
    _, score = a_star_search(maze, start, end)
    return score

def solve_part2(maze):
    pass

if __name__ == "__main__":
    input_data = read_input('/Users/mattfree/Desktop/AdventOfCode/day16/input.txt')
    
    maze = parse_input(input_data)
    print(maze)
    
    result_part1 = solve_part1(maze)
    print(f"Part 1: {result_part1}")
    
    result_part2 = solve_part2(maze)
    print(f"Part 2: {result_part2}")