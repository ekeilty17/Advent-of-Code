from pathlib import Path
from typing import List

from Day_05.const import DAY, INPUT_FILE_NAME
from Day_05.const import EXAMPLE_INPUT_FILE_NAME_PART_1 as EXAMPLE_INPUT_FILE_NAME
from Day_05.load_input import load_input
from utils.test import test

def is_nice(line: str) -> bool:
    
    vowels = "aeiou"
    condition_1 = len([c for c in line if c in vowels]) >= 3
    
    condition_2 = any(a == b for a, b in zip(line[:-1], line[1:]))

    blacklist = set(["ab", "cd", "pq", "xy"])
    condition_3 = not any((a + b) in blacklist for a, b in zip(line[:-1], line[1:]))

    return condition_1 and condition_2 and condition_3

def solution(text_file: List[str]) -> int:
    count = 0
    for line in text_file:
        if is_nice(line):
            count += 1
    
    return count

if __name__ == "__main__":
    
    example_text_file = load_input(Path(f"Day_{DAY:02d}/{EXAMPLE_INPUT_FILE_NAME}"))
    text_file = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))

    expected_answer = 2
    test(expected_answer, solution, example_text_file)

    total = solution(text_file)
    print("Puzzle Answer:", total)