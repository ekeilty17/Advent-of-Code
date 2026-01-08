from pathlib import Path
from typing import List

from Day_01.const import DAY, EXAMPLE_INPUT_FILE_NAME, INPUT_FILE_NAME
from Day_01.load_input import load_input
from utils.solve import test, solve

def apply_rotation(dial_start: int, rotation: int) -> int:
    return (dial_start + rotation) % 100

def solution(dial_start: int, rotations: List[int]) -> int:
    count_0 = 0

    dial = dial_start
    if dial == 0:
        count_0 += 1
    for rotation in rotations:
        dial = apply_rotation(dial, rotation)
        if dial == 0:
            count_0 += 1
    
    return count_0

if __name__ == "__main__":
    dial_start = 50

    example_rotations = load_input(Path(f"Day_{DAY:02d}/{EXAMPLE_INPUT_FILE_NAME}"))
    example_answer = 3
    test(example_answer, solution, dial_start, example_rotations)

    rotations = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))
    solve(solution, dial_start, rotations)