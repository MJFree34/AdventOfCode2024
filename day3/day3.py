import re

def parse_input(file_path):
    memory = ""
    
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            memory += line.strip()
    
    return memory

def calculate_total_sum(memory):
    pattern = r"(do\(\)|don't\(\)|mul\(\d+,\d+\))"
    matches = re.findall(pattern, memory)

    total_sum = 0
    counting = True
    for match in matches:
        if match == "do()":
            counting = True
        elif match == "don't()":
            counting = False
        elif counting and match.startswith("mul("):
            numbers = re.findall(r"\d+", match)
            product = int(numbers[0]) * int(numbers[1])
            total_sum += product
    return total_sum

if __name__ == "__main__":
    file_path = 'day3/input.txt'
    memory = parse_input(file_path)
    total_sum = calculate_total_sum(memory)
    print(total_sum)