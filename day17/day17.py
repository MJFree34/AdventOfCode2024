from typing import Tuple, Optional

class Instruction:
    def __init__(self, opcode: int, operand: int):
        self.opcode = int(opcode)
        self.operand = int(operand)

def read_input(file_path: str) -> list[str]:
    with open(file_path, 'r') as file:
        return file.read().strip().split('\n\n')

def process_input(input_data: list[str]) -> Tuple[int, int, int, list[Instruction], list[str]]:
    registers, instruction_line = input_data[0], input_data[1]
    a_reg, b_reg, c_reg = [int(line.split()[2]) for line in registers.split('\n')]
    instructions = []
    instruction_line = list(map(int, instruction_line.split(' ')[1].split(',')))
    for i in range(0, len(instruction_line), 2):
        opcode, operand = instruction_line[i], instruction_line[i+1]
        instructions.append(Instruction(opcode, int(operand)))
    return a_reg, b_reg, c_reg, instructions, instruction_line

def calc_combo_operand(a_reg: int, b_reg: int, c_reg: int, operand: int) -> int:
    if operand == 0 or operand == 1 or operand == 2 or operand == 3:
        return operand
    elif operand == 4:
        return a_reg
    elif operand == 5:
        return b_reg
    elif operand == 6:
        return c_reg
    elif operand == 7:
        # reserved
        return operand
    else:
        raise ValueError(f"Invalid operand: {operand}")
    
def run_instructions(a_reg: int, b_reg: int, c_reg: int, instructions: list[Instruction]) -> list[int]:
    pc = 0
    output = []

    while pc < len(instructions):
        instr = instructions[pc]
        combo_operand = calc_combo_operand(a_reg, b_reg, c_reg, instr.operand)
        if instr.opcode == 0:
            # adv
            a_reg = a_reg // 2 ** combo_operand
        elif instr.opcode == 1:
            # bxl
            b_reg = b_reg ^ instr.operand
        elif instr.opcode == 2:
            # bst
            b_reg = combo_operand % 8
        elif instr.opcode == 3:
            # jnz
            if a_reg != 0:
                pc = instr.operand
                continue
        elif instr.opcode == 4:
            # bxc
            b_reg = b_reg ^ c_reg
        elif instr.opcode == 5:
            # out
            val = combo_operand % 8
            output.append(val)
        elif instr.opcode == 6:
            # bdv
            b_reg = a_reg // 2 ** combo_operand
        elif instr.opcode == 7:
            # cdv
            c_reg = a_reg // 2 ** combo_operand
        else:
            raise ValueError(f"Invalid opcode: {instr.opcode}")
        pc += 1

    return output

def calculate_a_reg(instructions: list[Instruction], instruction_line: list[int], index: int, partial_a: int) -> Optional[int]:
    print("Testing input:", instruction_line[index:], "Index:", index, "Partial A:", partial_a)
    for i in range(8):
        output = run_instructions(partial_a * 8 + i, 0, 0, instructions)
        print("Output:", output)
        if run_instructions(partial_a * 8 + i, 0, 0, instructions) == instruction_line[index:]:
            print(f"Partial A: {partial_a * 8 + i}")
            if index == 0:
                return partial_a * 8 + i
            ret = calculate_a_reg(instructions, instruction_line, index - 1, partial_a * 8 + i)
            if ret is not None:
                return ret
    print(f"Failed at index {index}")
    return None

def solve_part1(a_reg: int, b_reg: int, c_reg: int, instructions: list[Instruction]) -> str:
    output = run_instructions(a_reg, b_reg, c_reg, instructions)
    return ','.join(map(str, output))

def solve_part2(instructions: list[Instruction], instruction_line: list[int]) -> int:
    calculate_a_reg(instructions, instruction_line, len(instruction_line) - 1, 0)
    # for i in range(238269496789770, 2382694967897800):
    #     print(f"Testing {i}")
    #     output = run_instructions(i, 0, 0, instructions)
    #     print(f"    Output: {output}")
    #     if output == instruction_line:
    #         return i

if __name__ == "__main__":
    input_data = read_input('/Users/mattfree/Desktop/AdventOfCode/day17/input.txt')
    a_reg, b_reg, c_reg, instructions, instruction_line = process_input(input_data)

    result_part1 = solve_part1(a_reg, b_reg, c_reg, instructions)
    print(f"Part 1: {result_part1}")

    result_part2 = solve_part2(instructions, instruction_line)
    print(f"Part 2: {result_part2}")