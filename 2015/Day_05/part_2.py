from pathlib import Path
from typing import List

from Day_05.const import DAY, INPUT_FILE_NAME
from Day_05.const import EXAMPLE_INPUT_FILE_NAME_PART_2 as EXAMPLE_INPUT_FILE_NAME
from Day_05.load_input import load_input
from utils.test import test

def is_nice(line: str) -> bool:
    
    condition_1 = False
    previous_pairs = set([])
    for i in range(len(line)-3):
        a, b, c, d = line[i:i+4]
        if a == b == c == d:
            condition_1 = True
            break
        if a == b == c:
            continue
        if (a, b) in previous_pairs:
            condition_1 = True
            break
        previous_pairs.add((a, b))
    
    # These got skipped by the for loop
    a, b, c, d = line[-4:]
    if not (b == c == d):
        if (b, c) in previous_pairs:
            condition_1 = True
        if (c, d) in previous_pairs:
            condition_1 = True

    condition_2 = False
    for i in range(len(line)-2):
        a, b, c = line[i:i+3]
        if a == c:
            condition_2 = True
            break
    
    return condition_1 and condition_2

def solution(text_file: List[str]) -> int:
    count = 0
    for line in text_file:
        if is_nice(line):
            count += 1
    
    return count

if __name__ == "__main__":
    
    example_text_file = load_input(Path(f"Day_{DAY:02d}/{EXAMPLE_INPUT_FILE_NAME}"))
    text_file = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))

    expected_answer = 3
    test(expected_answer, solution, example_text_file)

    total = solution(text_file)
    print("Puzzle Answer:", total)