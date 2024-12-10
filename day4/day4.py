def read_input(file_path):
    with open(file_path, 'r') as file:
        data = file.readlines()

    return [list(line.strip()) for line in data]

def check_sequence(sequence, direction, get_coords, target_seq):
    count = 0
    for i in range(len(sequence) - len(target_seq) + 1):
        current_seq = list(sequence[i:i + len(target_seq)])
        if current_seq == target_seq:
            count += 1
            start = get_coords(i)
            end = get_coords(i + len(target_seq) - 1)
            print(f"Found '{''.join(target_seq)}' from {start} to {end} ({direction})")
        if current_seq == target_seq[::-1]:
            count += 1
            start = get_coords(i)
            end = get_coords(i + len(target_seq) - 1)
            print(f"Found '{''.join(target_seq[::-1])}' from {start} to {end} ({direction})")
    return count

def calculate_total_xmas(char_2d_array):
    total_xmas = 0

    def check_xmas_sequence(sequence, direction, get_coords):
        target_seq = ['X', 'M', 'A', 'S']
        count = check_sequence(sequence, direction, get_coords, target_seq)
        nonlocal total_xmas
        total_xmas += count

    # Check rows (horizontal)
    for row_idx, row in enumerate(char_2d_array):
        check_xmas_sequence(row, 'horizontal', lambda i, row_idx=row_idx: (row_idx, i))

    # Check columns (vertical)
    for col_idx, col in enumerate(zip(*char_2d_array)):
        check_xmas_sequence(col, 'vertical', lambda i, col_idx=col_idx: (i, col_idx))

    # Check diagonals (top-left to bottom-right)
    for offset in range(-len(char_2d_array) + 1, len(char_2d_array)):
        diagonal = [row[i] for row_idx, row in enumerate(char_2d_array) if 0 <= (i := row_idx + offset) < len(row)]
        check_xmas_sequence(diagonal, 'diagonal TL-BR', lambda i, offset=offset: (i, i + offset))

    # Check diagonals (top-right to bottom-left)
    for offset in range(len(char_2d_array) * 2 - 1):
        diagonal = [char_2d_array[i][offset - i] for i in range(max(0, offset - len(char_2d_array) + 1), min(len(char_2d_array), offset + 1))]
        check_xmas_sequence(diagonal, 'diagonal TR-BL', lambda i, offset=offset: (i, offset - i))

    return total_xmas

def is_x_mas(char_2d_array, i, j):
    patterns = [
        # Pattern 1
        ['M', 'S', 'M', 'S'],
        # Pattern 2
        ['S', 'M', 'S', 'M'],
        # Pattern 3
        ['M', 'S', 'S', 'M'],
        # Pattern 4
        ['S', 'M', 'M', 'S']
    ]
    surrounding = [
        char_2d_array[i-1][j-1],
        char_2d_array[i-1][j+1],
        char_2d_array[i+1][j-1],
        char_2d_array[i+1][j+1]
    ]
    return surrounding in patterns

def calculate_total_x_mas(char_2d_array):
    def is_x_mas(char_2d_array, i, j):
        patterns = [
            # Pattern 1
            ['M', 'S', 'M', 'S'],
            # Pattern 2
            ['S', 'M', 'S', 'M'],
            # Pattern 3
            ['M', 'M', 'S', 'S'],
            # Pattern 4
            ['S', 'S', 'M', 'M'],
        ]
        surrounding = [
            char_2d_array[i-1][j-1],
            char_2d_array[i-1][j+1],
            char_2d_array[i+1][j-1],
            char_2d_array[i+1][j+1]
        ]
        return surrounding in patterns

    total_x_mas = 0
    rows = len(char_2d_array)
    cols = len(char_2d_array[0]) if rows > 0 else 0

    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            if char_2d_array[i][j] == 'A' and is_x_mas(char_2d_array, i, j):
                total_x_mas += 1
                print(f"Found 'X-MAS' centered at ({i}, {j})")
    return total_x_mas

if __name__ == "__main__":
    input_file = '/Users/mattfree/Desktop/AdventOfCode/day4/input.txt'
    char_2d_array = read_input(input_file)
    total_xmas = calculate_total_xmas(char_2d_array)
    print(f"Total 'XMAS' found: {total_xmas}")
    total_x_mas = calculate_total_x_mas(char_2d_array)
    print(f"Total 'X-MAS' found: {total_x_mas}")
