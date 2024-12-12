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
            nodes_count, open_edges, _ = dfs(visited, node)
            total_fencing_price += nodes_count * open_edges

    return total_fencing_price

def dfs(visited, node):
        stack = [node]
        nodes_count = 0
        open_edges = 0
        corners_count = 0
        while stack:
            x, y = stack.pop()
            if (x, y) not in visited:
                visited.add((x, y))
                nodes_count += 1
                adjacent_nodes = garden_graph[(x, y)]
                open_edges += 4 - len(adjacent_nodes)
                corners_count += calculate_corners(x, y, adjacent_nodes)
                for neighbor in adjacent_nodes:
                    if neighbor not in visited:
                        stack.append(neighbor)
        return nodes_count, open_edges, corners_count

def calculate_discounted_fence_price():
    visited = set()
    total_discounted_fence_price = 0

    for node in garden_graph:
        if node not in visited:
            print("Node: ", node)
            nodes_count, _, corners_count = dfs(visited, node)
            print("Nodes Count: ", nodes_count, "Corners Count: ", corners_count)
            discounted_fence_price = nodes_count * corners_count
            total_discounted_fence_price += discounted_fence_price

    return total_discounted_fence_price

def calculate_corners(x, y, adjacent_nodes):
    print("Checking corners for node: ", x, y)

    # All corners if no adjacent nodes
    if len(adjacent_nodes) == 0:
        print("No adjacent nodes, all corners")
        return 4
    
    # Two corners if one adjacent node
    if len(adjacent_nodes) == 1:
        print("One adjacent node, two corners")
        return 2
    
    corners_count = 0

    # One corner if two adjacent nodes are not stacked
    if len(adjacent_nodes) == 2:
        if not ((adjacent_nodes[0][0] == x and adjacent_nodes[1][0] == x) or (adjacent_nodes[0][1] == y and adjacent_nodes[1][1] == y)):
            print("Two adjacent nodes not stacked, one corner, continuing")
            corners_count += 1
        else:
            print("Two adjacent nodes stacked, no corners")
            return 0
    
    # Check for inside corners
    current_plant = garden[x][y]
    
    # Top-Left Inside Corner
    if (x > 0 and y > 0 and garden[x-1][y] == current_plant and garden[x][y-1] == current_plant):
        if garden[x-1][y-1] != current_plant:
            print("Top-Left Inside Corner, one corner, continuing")
            corners_count += 1
    
    # Top-Right Inside Corner
    if (x > 0 and y < len(garden[0]) - 1 and garden[x-1][y] == current_plant and garden[x][y+1] == current_plant):
        if garden[x-1][y+1] != current_plant:
            print("Top-Right Inside Corner, one corner, continuing")
            corners_count += 1
    
    # Bottom-Left Inside Corner
    if (x < len(garden) - 1 and y > 0 and garden[x+1][y] == current_plant and garden[x][y-1] == current_plant):
        if garden[x+1][y-1] != current_plant:
            print("Bottom-Left Inside Corner, one corner, continuing")
            corners_count += 1
    
    # Bottom-Right Inside Corner
    if (x < len(garden) - 1 and y < len(garden[0]) - 1 and garden[x+1][y] == current_plant and garden[x][y+1] == current_plant):
        if garden[x+1][y+1] != current_plant:
            print("Bottom-Right Inside Corner, one corner, continuing")
            corners_count += 1
    
    print("Inside Corners: ", corners_count)
    return corners_count

if __name__ == "__main__":
    input_data = read_input('/Users/mattfree/Desktop/AdventOfCode/day12/input.txt')
    garden = process_data(input_data)
    create_garden_graph()
    # total_fencing_price = calculate_total_fencing_price()
    # print(total_fencing_price)
    total_discounted_fence_price = calculate_discounted_fence_price()
    print(total_discounted_fence_price)