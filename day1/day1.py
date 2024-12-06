def parse_input(file_path):
    list1 = []
    list2 = []
    
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            parts = line.strip().split('  ')
            if len(parts) == 2:
                list1.append(int(parts[0]))
                list2.append(int(parts[1]))
    
    return list1, list2

def calculate_total_distance(list1, list2):
    total_distance = 0
    
    while list1 and list2:
        min1 = min(list1)
        min2 = min(list2)
        distance = abs(min1 - min2)
        total_distance += distance
        list1.remove(min1)
        list2.remove(min2)
    
    return total_distance

def calculate_similarity_score(list1, list2):
    total_score = 0

    for i in range(len(list1)):
        num = list1[i]
        count = list2.count(num)
        total_score += num * count

    return total_score


if __name__ == "__main__":
    file_path = 'input.txt'
    list1, list2 = parse_input(file_path)
    total_distance = calculate_total_distance(list1, list2)
    print("Total distance: ", total_distance)

    list1, list2 = parse_input(file_path)
    similarity_score = calculate_similarity_score(list1, list2)
    print("Similarity score: ", similarity_score)