from pathlib import Path
from typing import List, Tuple

from Day_12.const import DAY, INPUT_FILE_NAME
from Day_12.load_input import load_input
from Day_12.part_1 import compile
from utils.solve import solve

def solution(instructions: List[Tuple[str, List[int|str]]], target_register: int) -> int:
    registers = {"a": 0, "b": 0, "c": 1, "d": 0}
    compile(registers, instructions)
    return registers[target_register]

if __name__ == "__main__":
    target_register = "a"
    instructions = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))
    solve(solution, instructions, target_register)