from pathlib import Path
from typing import List, Tuple
import re

from Day_03.const import DAY, INPUT_FILE_NAME
from Day_03.const import EXAMPLE_INPUT_FILE_NAME_PART_1 as EXAMPLE_INPUT_FILE_NAME
from Day_03.load_input import load_input
from utils.solve import test, solve

def decode_instruction(corrupted_instruction: str) -> List[Tuple[int, int]]:
    pattern = r"mul\((\d+),(\d+)\)"
    matches = re.findall(pattern, corrupted_instruction)
    return [(int(a), int(b)) for a, b, in matches]

def solution(corrupted_instructions: List[str]) -> int:
    
    total = 0
    for corrupted_instruction in corrupted_instructions:
        instruction_list = decode_instruction(corrupted_instruction)
        total += sum([a*b for a, b in instruction_list])

    return total

if __name__ == "__main__":
    example_corrupted_instructions = load_input(Path(f"Day_{DAY:02d}/{EXAMPLE_INPUT_FILE_NAME}"))
    expected_answer = 161
    test(expected_answer, solution, example_corrupted_instructions)

    corrupted_instructions = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))
    solve(solution, corrupted_instructions)