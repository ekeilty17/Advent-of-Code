from pathlib import Path
from typing import List, Tuple
import re

from Day_03.const import DAY, INPUT_FILE_NAME
from Day_03.const import EXAMPLE_INPUT_FILE_NAME_PART_2 as EXAMPLE_INPUT_FILE_NAME
from Day_03.load_input import load_input
from utils.test import test

def decode_instruction(corrupted_instruction: str, enabled: bool=True) -> List[Tuple[int, int]]:
    pattern = r"(do\(\))|(don't\(\))|(mul\((\d+),(\d+)\))"
    matches = re.findall(pattern, corrupted_instruction)
    
    instruction_list = []
    for is_do, is_dont, _, a, b in matches:
        if is_do:
            enabled = True
            continue
        if is_dont:
            enabled = False
            continue
        if enabled:
            instruction_list.append((int(a), int(b)))

    return instruction_list, enabled

def solution(corrupted_instructions: List[str]) -> int:
    
    total = 0
    enabled = True
    for corrupted_instruction in corrupted_instructions:
        instruction_list, enabled = decode_instruction(corrupted_instruction, enabled)
        total += sum([a*b for a, b in instruction_list])

    return total

if __name__ == "__main__":
    
    example_corrupted_instructions = load_input(Path(f"Day_{DAY:02d}/{EXAMPLE_INPUT_FILE_NAME}"))
    corrupted_instructions = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))

    expected_answer = 48
    test(expected_answer, solution, example_corrupted_instructions)

    total = solution(corrupted_instructions)
    print("Puzzle Answer:", total)