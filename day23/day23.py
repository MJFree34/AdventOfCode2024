from networkx.algorithms.clique import find_cliques
import networkx as nx

graph: dict[str, set[str]] = {}

def read_input(file_path: str) -> list[str]:
    with open(file_path, 'r') as file:
        return file.read().strip().split('\n')

def process_input(input_data: list[str]):
    for line in input_data:
        u, v = line.split('-')
        if u not in graph:
            graph[u] = set()
        graph[u].add(v)
        if v not in graph:
            graph[v] = set()
        graph[v].add(u)
    # print(graph)

def solve_part1() -> int:
    three_sets_count = 0
    for a in graph:
        connected_nodes = list(graph[a])
        for i in range(len(connected_nodes) - 1):
            for j in range(i + 1, len(connected_nodes)):
                b = connected_nodes[i]
                c = connected_nodes[j]
                if c in graph[b] and (a.startswith('t') or b.startswith('t') or c.startswith('t')):
                    three_sets_count += 1
                    # print(a, b, c)
        
    return three_sets_count // 3

def solve_part2() -> str:
    G = nx.Graph()
    for node, neighbors in graph.items():
        for neighbor in neighbors:
            G.add_edge(node, neighbor)
    cliques = list(find_cliques(G))
    max_clique = sorted(max(cliques, key=len))
    return ','.join(node for node in max_clique)

if __name__ == "__main__":
    input_data = read_input('/Users/mattfree/Desktop/AdventOfCode/day23/input.txt')
    process_input(input_data)

    result_part1 = solve_part1()
    print("Part 1:", result_part1)

    result_part2 = solve_part2()
    print("Part 2:", result_part2)