from typing import Tuple

class Instruction:
    def __init__(self, opcode: str, operand: int):
        self.opcode = int(opcode)
        self.operand = int(operand)

def read_input(file_path: str) -> list[str]:
    with open(file_path, 'r') as file:
        return file.read().strip().split('\n\n')

def process_input(input_data: list[str]) -> Tuple[int, int, int, list[Instruction]]:
    registers, instruction_line = input_data[0], input_data[1]
    a_reg, b_reg, c_reg = [int(line.split()[2]) for line in registers.split('\n')]
    instructions = []
    instruction_line = instruction_line.split(' ')[1].split(',')
    for i in range(0, len(instruction_line), 2):
        opcode, operand = instruction_line[i], instruction_line[i+1]
        instructions.append(Instruction(opcode, int(operand)))
    return a_reg, b_reg, c_reg, instructions

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

def solve_part1(a_reg: int, b_reg: int, c_reg: int, instructions: list[Instruction]) -> str:
    pc = 0
    output = ""

    while pc < len(instructions):
        instr = instructions[pc]
        combo_operand = calc_combo_operand(a_reg, b_reg, c_reg, instr.operand)
        print("executing", instr.opcode, instr.operand)
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
            if output == "":
                output = str(val)
            else:
                output += ',' + str(val)
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

def solve_part2(data):
    # Implement the solution for part 2
    pass

if __name__ == "__main__":
    input_data = read_input('/Users/mattfree/Desktop/AdventOfCode/day17/input.txt')
    a_reg, b_reg, c_reg, instructions = process_input(input_data)

    result_part1 = solve_part1(a_reg, b_reg, c_reg, instructions)
    print(f"Part 1: {result_part1}")

    result_part2 = solve_part2(input_data)
    print(f"Part 2: {result_part2}")