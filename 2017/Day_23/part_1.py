from pathlib import Path
from typing import List, Tuple, Dict

from Day_23.const import DAY, INPUT_FILE_NAME
from Day_23.load_input import load_input
from Day_23.opcodes import OPCODES
from utils.solve import solve

def compile(instructions: List[Tuple[str, List[int|str]]]) -> Dict[str, int]:
    instruction_counts = {opcode: 0 for opcode in OPCODES}

    pc = 0
    registers = {}
    while pc < len(instructions):
        opcode, operands = instructions[pc]
        instruction_counts[opcode] += 1

        pc_step = OPCODES[opcode](registers, *operands)
        pc_step = 1 if pc_step is None else pc_step
        pc += pc_step
    
    return instruction_counts

def solution(instructions: List[Tuple[str, List[int|str]]], debug_instruction: str) -> int:
    instruction_counts = compile(instructions)
    return instruction_counts[debug_instruction]

if __name__ == "__main__":
    instructions = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))
    debug_instruction = "mul"
    solve(solution, instructions, debug_instruction)