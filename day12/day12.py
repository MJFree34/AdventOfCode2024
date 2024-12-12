garden = []
garden_graph = {}

def read_input(file_path):
    with open(file_path, 'r') as file:
        return file.readlines()

def process_data(data):
    data = [[char for char in line.strip()] for line in data]
    return data

def create_garden_graph():
    rows = len(garden)
    cols = len(garden[0])
    for r in range(rows):
        for c in range(cols):
            if (r, c) not in garden_graph:
                garden_graph[(r, c)] = []
            if r > 0 and garden[r-1][c] == garden[r][c]:
                garden_graph[(r, c)].append((r-1, c))
            if r < rows - 1 and garden[r+1][c] == garden[r][c]:
                garden_graph[(r, c)].append((r+1, c))
            if c > 0 and garden[r][c-1] == garden[r][c]:
                garden_graph[(r, c)].append((r, c-1))
            if c < cols - 1 and garden[r][c+1] == garden[r][c]:
                garden_graph[(r, c)].append((r, c+1))

def calculate_total_fencing_price():
    visited = set()
    total_fencing_price = 0

    for node in garden_graph:
        if node not in visited:
            nodes_count, open_edges = dfs(node)
            total_fencing_price += nodes_count * open_edges

    return total_fencing_price

def dfs(node):
        stack = [node]
        nodes_count = 0
        open_edges = 0
        while stack:
            x, y = stack.pop()
            if (x, y) not in visited:
                visited.add((x, y))
                nodes_count += 1
                adjacent_nodes = garden_graph[(x, y)]
                open_edges += 4 - len(adjacent_nodes)
                for neighbor in adjacent_nodes:
                    if neighbor not in visited:
                        stack.append(neighbor)
        return nodes_count, open_edges

if __name__ == "__main__":
    input_data = read_input('/Users/mattfree/Desktop/AdventOfCode/day12/input.txt')
    garden = process_data(input_data)
    create_garden_graph()
    total_fencing_price = calculate_total_fencing_price()
    print(total_fencing_price)