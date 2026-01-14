from pathlib import Path
from typing import List, Tuple, Dict

from Day_12.const import DAY, EXAMPLE_INPUT_FILE_NAME, INPUT_FILE_NAME
from Day_12.load_input import load_input
from Day_12.opcodes import OPCODES
from utils.solve import test, solve

def compile(registers: Dict[str, int], instructions: List[Tuple[str, List[int|str]]]) -> Dict[str, int]:
    pc = 0
    while pc < len(instructions):
        opcode, operands = instructions[pc]
        pc_step = OPCODES[opcode](registers, *operands)
        
        pc_step = 1 if pc_step is None else pc_step
        pc += pc_step
    
    return registers

def solution(instructions: List[Tuple[str, List[int|str]]], target_register: int) -> int:
    registers = {"a": 0, "b": 0, "c": 0, "d": 0}
    compile(registers, instructions)
    return registers[target_register]

if __name__ == "__main__":
    target_register = "a"

    example_instructions = load_input(Path(f"Day_{DAY:02d}/{EXAMPLE_INPUT_FILE_NAME}"))
    expected_answer = 42
    test(expected_answer, solution, example_instructions, target_register)

    instructions = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))
    solve(solution, instructions, target_register)