from pathlib import Path
from typing import List

from Day_01.const import DAY, INPUT_FILE_NAME
from Day_01.const import EXAMPLE_INPUT_FILE_NAME_PART_1 as EXAMPLE_INPUT_FILE_NAME
from Day_01.load_input import load_input
from utils.solve import test, solve

def solution(instructions: List[int]) -> int:
    instructions = [-x if i % 2 else x for i, x in enumerate(instructions)]
    
    blocks = 0
    orientation = 1
    for instruction in instructions:
        blocks += orientation * instruction
        orientation *= 1 if instruction > 0 else -1
    
    return abs(blocks)

if __name__ == "__main__":
    example_instructions = load_input(Path(f"Day_{DAY:02d}/{EXAMPLE_INPUT_FILE_NAME}"))
    expected_answer = 12
    test(expected_answer, solution, example_instructions)

    instructions = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))
    solve(solution, instructions)