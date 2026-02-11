from pathlib import Path
from typing import List, Tuple

from Day_18.const import DAY, INPUT_FILE_NAME
from Day_18.const import EXAMPLE_INPUT_FILE_NAME_PART_1 as EXAMPLE_INPUT_FILE_NAME
from Day_18.load_input import load_input
from Day_18.opcodes import OPCODES
from utils.solve import test, solve

def compile(instructions: List[Tuple[str, List[int|str]]]) -> List[int]:
    pc = 0
    output = []
    registers = {}
    while pc < len(instructions):
        opcode, operands = instructions[pc]
        
        if opcode == "snd":
            x = operands[0]
            x = registers.get(x, 0) if isinstance(x, str) else x
            output.append(x)
            pc_step = 1
        
        elif opcode == "rcv":
            x = operands[0]
            x = registers[x] if x in registers else x
            if x != 0:
                return output
        else:
            pc_step = OPCODES[opcode](registers, *operands)
        
        pc_step = 1 if pc_step is None else pc_step
        pc += pc_step

def solution(instructions: List[Tuple[str, List[int|str]]]) -> int:
    frequencies = compile(instructions)
    return frequencies[-1]

if __name__ == "__main__":
    example_instructions = load_input(Path(f"Day_{DAY:02d}/{EXAMPLE_INPUT_FILE_NAME}"))
    expected_answer = 4
    test(expected_answer, solution, example_instructions)

    instructions = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))
    solve(solution, instructions)