from pathlib import Path
from typing import List

from Day_01.const import DAY, EXAMPLE_INPUT_FILE_NAME, INPUT_FILE_NAME
from Day_01.load_input import load_input
from utils.solve import test, solve

def distance(ID1: int, ID2: int) -> int:
    return abs(ID2 - ID1)

def solution(left_location_ids: List[int], right_location_ids: List[int]) -> int:
    return sum(distance(ID1, ID2) for ID1, ID2 in zip(sorted(left_location_ids), sorted(right_location_ids)))

if __name__ == "__main__":
    example_left_location_ids, example_right_location_ids = load_input(Path(f"Day_{DAY:02d}/{EXAMPLE_INPUT_FILE_NAME}"))
    example_answer = 11
    test(example_answer, solution, example_left_location_ids, example_right_location_ids)

    left_location_ids, right_location_ids = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))
    solve(solution, left_location_ids, right_location_ids)