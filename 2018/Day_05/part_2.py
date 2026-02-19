from pathlib import Path
from typing import List

from Day_05.const import DAY, EXAMPLE_INPUT_FILE_NAME, INPUT_FILE_NAME
from Day_05.load_input import load_input
from Day_05.part_1 import reduce_polymer
from utils.solve import test, solve

def solution(polymer: str) -> int:
    min_length_polymer = float("inf")

    for unit in sorted(set(polymer.lower())):
        reduced_polymer = reduce_polymer([x for x in list(polymer) if x.lower() != unit])
        min_length_polymer = min(min_length_polymer, len(reduced_polymer))
    
    return min_length_polymer

if __name__ == "__main__":
    example_polymer = load_input(Path(f"Day_{DAY:02d}/{EXAMPLE_INPUT_FILE_NAME}"))
    expected_answer = 4
    test(expected_answer, solution, example_polymer)

    polymer = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))
    solve(solution, polymer)