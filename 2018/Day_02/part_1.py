from pathlib import Path
from typing import List, Dict

from Day_02.const import DAY, INPUT_FILE_NAME
from Day_02.const import EXAMPLE_INPUT_FILE_NAME_PART_1 as EXAMPLE_INPUT_FILE_NAME
from Day_02.load_input import load_input
from utils.solve import test, solve

def get_letter_counts(string: str) -> Dict[str, int]:
    counts = {}
    for char in string:
        counts[char] = counts.get(char, 0) + 1
    return counts

def solution(IDs: List[str]) -> int:
    num_IDs_with_exactly_2 = 0
    num_IDs_with_exactly_3 = 0

    for ID in IDs:
        letter_counts = get_letter_counts(ID)
        if 2 in letter_counts.values():
            num_IDs_with_exactly_2 += 1
        if 3 in letter_counts.values():
            num_IDs_with_exactly_3 += 1
    
    return num_IDs_with_exactly_2 * num_IDs_with_exactly_3

if __name__ == "__main__":
    example_IDs = load_input(Path(f"Day_{DAY:02d}/{EXAMPLE_INPUT_FILE_NAME}"))
    expected_answer = 12
    test(expected_answer, solution, example_IDs)

    IDs = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))
    solve(solution, IDs)