stones_map = {}

def read_input(file_path):
    with open(file_path, 'r') as file:
        return file.readlines()

def process_data(data):
    stones_list = list(map(int, data.pop().strip().split(' ')))
    stones_map = {}
    for stone in stones_list:
        if stone not in stones_map:
            stones_map[stone] = 1
        else:
            stones_map[stone] += 1
    return stones_map

def calculate_stones_count():
    print("Initial Stones Map:", stones_map)

    for day in range(75):
        blink(day)
    return sum(stones_map.values())

def blink(day):
    items = list(stones_map.items())

    for stone, count in items:
        handle_stone(stone, count)
    
    print("Updated Stones Map:", stones_map)
    
    total_stones = sum(stones_map.values())
    print(f"Day {day + 1}: {total_stones} stones")

def handle_stone(stone, count):
    str_stone = str(stone)
    if stone == 0:
        update_stone(stone, 1, count)
    elif len(str_stone) % 2 == 0:
        middle = len(str_stone) // 2
        update_stone(stone, int(str_stone[:middle]), count)
        add_stone(int(str_stone[middle:]), count)
    else:
        update_stone(stone, stone * 2024, count)

def update_stone(stone, new_stone, count):
    if stones_map.get(stone, 0) == count:
        del stones_map[stone]
    else:
        stones_map[stone] -= count
    add_stone(new_stone, count)

def add_stone(stone, count):
    if stone not in stones_map:
        stones_map[stone] = count
    else:
        stones_map[stone] += count

if __name__ == "__main__":
    input_data = read_input('/Users/mattfree/Desktop/AdventOfCode/day11/input.txt')
    stones_map = process_data(input_data)
    
    final_stones_map_length = calculate_stones_count()
    print(f"Final Number of Stones: {final_stones_map_length}")