from pathlib import Path
from typing import List, Tuple, Dict

from Day_23.const import DAY, EXAMPLE_INPUT_FILE_NAME, INPUT_FILE_NAME
from Day_23.load_input import load_input
from Day_23.opcodes import OPCODES
from utils.solve import test, solve

def compile_program(instructions: List[Tuple[str, List[str|int]]], registers: Dict[str, int]) -> Dict[str, int]:
    pc = 0
    while pc < len(instructions):
        opcode, operands = instructions[pc]
        pc = OPCODES[opcode](registers, pc, *operands)
    
    return registers

def solution(instructions: List[Tuple[str, List[str|int]]], output_register: str) -> int:
    registers = {"a": 0, "b": 0}
    registers = compile_program(instructions, registers)
    return registers[output_register]

if __name__ == "__main__":
    example_instructions = load_input(Path(f"Day_{DAY:02d}/{EXAMPLE_INPUT_FILE_NAME}"))
    example_output_register = "a"
    expected_answer = 2
    test(expected_answer, solution, example_instructions, example_output_register)

    instructions = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))
    output_register = "b"
    solve(solution, instructions, output_register)