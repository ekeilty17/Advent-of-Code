from pathlib import Path
from typing import List, Tuple

from Day_23.const import DAY, INPUT_FILE_NAME
from Day_23.load_input import load_input
from Day_23.part_1 import compile_program
from utils.solve import solve

def solution(instructions: List[Tuple[str, List[str|int]]], output_register: str) -> int:
    registers = {"a": 1, "b": 0}
    registers = compile_program(instructions, registers)
    return registers[output_register]

if __name__ == "__main__":
    instructions = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))
    output_register = "b"
    solve(solution, instructions, output_register)