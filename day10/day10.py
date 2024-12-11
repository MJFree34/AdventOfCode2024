def read_input(input_file):
    with open(input_file, 'r') as f:
        topographic_map = [list(line.strip()) for line in f]
    return topographic_map

def calculate_total_score(topographic_map):
    total_score = 0
    for row in range(len(topographic_map)):
        for col in range(len(topographic_map[row])):
            if topographic_map[row][col] == '0':
                print(f'Found a 0 at row {row} and col {col}')
                trailends_map = {}
                total_score += score_trailhead(topographic_map, trailends_map, row, col)
    return total_score

def score_trailhead(topographic_map, trailends_map, row, col):
    score = 0
    value = topographic_map[row][col]
    # Check if we are at the end of the trail
    if value == '9':
        trailend_current_score = trailends_map.get(f"({row},{col})", 0)
        trailends_map.update({f"({row},{col})": trailend_current_score + 1})
        return 1
    # Traverse up, down, left, right to find the next trailhead
    if row > 0 and topographic_map[row - 1][col] == f'{int(value) + 1}':
        print(f'Traversing up from row {row} and col {col}')
        score += score_trailhead(topographic_map, trailends_map, row-1, col)
    if col > 0 and topographic_map[row][col - 1] == f'{int(value) + 1}':
        print(f'Traversing left from row {row} and col {col}')
        score += score_trailhead(topographic_map, trailends_map, row, col-1)
    if row < len(topographic_map) - 1 and topographic_map[row + 1][col] == f'{int(value) + 1}':
        print(f'Traversing down from row {row} and col {col}')
        score += score_trailhead(topographic_map, trailends_map, row+1, col)
    if col < len(topographic_map[row]) - 1 and topographic_map[row][col + 1] == f'{int(value) + 1}':
        print(f'Traversing right from row {row} and col {col}')
        score += score_trailhead(topographic_map, trailends_map, row, col+1)

    return score

if __name__ == "__main__":
    input_file = '/Users/mattfree/Desktop/AdventOfCode/day10/input.txt'
    topographic_map = read_input(input_file)
    total_score = calculate_total_score(topographic_map)
    print(f'The total score is: {total_score}')