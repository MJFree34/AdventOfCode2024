from enum import Enum

input_wires = []
gates = []

class Wire:
    name: str
    value: bool

    def __init__(self, name: str, value: bool):
        self.name = name
        self.value = value

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f"Wire(name='{self.name}', value={self.value})"

class Operation(Enum):
    AND = 0
    OR = 1
    XOR = 2

    def __str__(self):
        return self.name

class Gate:
    input1: str
    input2: str
    output: str
    operation: Operation

    def __init__(self, input1: str, input2: str, output: str, operation: Operation):
        self.input1 = input1
        self.input2 = input2
        self.output = output
        self.operation = operation

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f"Gate(input1='{self.input1}', input2='{self.input2}', output='{self.output}', operation={self.operation})"

def read_input(file_path: str) -> list[str]:
    with open(file_path, 'r') as file:
        return file.read().strip()

def process_input(input_data: str) -> tuple[list[Wire], list[Gate]]:
    input_wires, gates = input_data.split('\n\n')

    input_wires = input_wires.split('\n')
    input_wires = [Wire(name=line.split(": ")[0], value=bool(int(line.split(": ")[1]))) for line in input_wires]

    gates = gates.split('\n')
    gates = [Gate(*gate.split(" ")[:3:2], gate.split(" ")[4], Operation[gate.split(" ")[1]]) for gate in gates]

    return input_wires, gates

def solve_part1():
    curr_wires = input_wires.copy()  # Make a copy to avoid modifying the original
    curr_gates = gates.copy()

    while len(curr_gates) > 0:
        for gate in curr_gates[:]:  # Create a copy of the list to iterate over
            wire_dict = {wire.name: wire for wire in curr_wires}  # Create a dictionary for wire lookup
            if gate.input1 in wire_dict and gate.input2 in wire_dict:
                if gate.operation == Operation.AND:
                    curr_wires.append(Wire(gate.output, wire_dict[gate.input1].value and wire_dict[gate.input2].value))
                elif gate.operation == Operation.OR:
                    curr_wires.append(Wire(gate.output, wire_dict[gate.input1].value or wire_dict[gate.input2].value))
                elif gate.operation == Operation.XOR:
                    curr_wires.append(Wire(gate.output, wire_dict[gate.input1].value ^ wire_dict[gate.input2].value))
                curr_gates.remove(gate)

    # Get all wires that start with 'z' and sort them by their number
    z_wires = [wire for wire in curr_wires if wire.name.startswith('z')]
    z_wires.sort(key=lambda w: int(w.name[1:]))  # Sort by the number after 'z'
    
    # Combine the values into a binary number
    result = 0
    for i, wire in enumerate(z_wires):
        if wire.value:
            result |= (1 << i)  # Set the i-th bit if the wire is True
    
    return result

def solve_part2(part1_result: int):
    # Get all x and y wires and sort them by their number
    x_wires = [wire for wire in input_wires if wire.name.startswith('x')]
    y_wires = [wire for wire in input_wires if wire.name.startswith('y')]
    x_wires.sort(key=lambda w: int(w.name[1:]))
    y_wires.sort(key=lambda w: int(w.name[1:]))

    # Convert wire lists to binary numbers
    x_num = 0
    y_num = 0
    for i, wire in enumerate(x_wires):
        if wire.value:
            x_num |= (1 << i)
    for i, wire in enumerate(y_wires):
        if wire.value:
            y_num |= (1 << i)

    # Add the binary numbers
    sum_result = x_num + y_num
    
    # Find mismatched bits
    xor_result = sum_result ^ part1_result
    mismatched_bits = []
    
    for i in range(max(sum_result, part1_result).bit_length()):
        if xor_result & (1 << i):
            mismatched_bits.append(i)
            
    return mismatched_bits

if __name__ == "__main__":
    input_data = read_input('/Users/mattfree/Desktop/AdventOfCode/day24/input.txt')
    input_wires, gates = process_input(input_data)

    result_part1 = solve_part1()
    print("Part 1:", result_part1)

    result_part2 = solve_part2(result_part1)
    print("Part 2:", result_part2)