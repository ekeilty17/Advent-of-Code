from pathlib import Path
from typing import List

from Day_01.const import DAY, EXAMPLE_INPUT_FILE_NAME, INPUT_FILE_NAME
from Day_01.load_input import load_input
from utils.test import test

def similarity(ID1: int, count_ID2: int) -> int:
    return ID1 * count_ID2

def solution(left_location_ids: List[int], right_location_ids: List[int]) -> int:
    
    right_location_id_counts = {}
    for ID2 in right_location_ids:
        if ID2 in right_location_id_counts:
            right_location_id_counts[ID2] += 1
        else:
            right_location_id_counts[ID2] = 1
    
    return sum([similarity(ID1, right_location_id_counts.get(ID1, 0)) for ID1 in left_location_ids])
    
if __name__ == "__main__":
    
    example_left_location_ids, example_right_location_ids = load_input(Path(f"Day_{DAY:02d}/{EXAMPLE_INPUT_FILE_NAME}"))
    left_location_ids, right_location_ids = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))

    example_answer = 31
    test(example_answer, solution, example_left_location_ids, example_right_location_ids)

    answer = solution(left_location_ids, right_location_ids)
    print("Puzzle Answer:", answer)