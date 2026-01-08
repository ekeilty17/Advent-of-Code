from pathlib import Path
from typing import List, Tuple

from Day_05.const import DAY, EXAMPLE_INPUT_FILE_NAME, INPUT_FILE_NAME
from Day_05.load_input import load_input
from Day_05.interval_set import InternvalSet
from utils.solve import test, solve

def solution(ingredient_id_ranges: List[Tuple[int, int]], ingredient_ids: List[int]) -> int:
    
    interval_set = InternvalSet()
    for ingredient_id_range in ingredient_id_ranges:
        interval_set.add(*ingredient_id_range)

    fresh_ingredient_ids = set()
    for ingredient_id in ingredient_ids:
        if ingredient_id in interval_set:
            fresh_ingredient_ids.add(ingredient_id)
    
    return len(fresh_ingredient_ids)

if __name__ == "__main__":
    example_ingredient_id_ranges, example_ingredient_ids = load_input(Path(f"Day_{DAY:02d}/{EXAMPLE_INPUT_FILE_NAME}"))
    expected_answer = 3
    test(expected_answer, solution, example_ingredient_id_ranges, example_ingredient_ids)

    ingredient_id_ranges, ingredient_ids = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))
    solve(solution, ingredient_id_ranges, ingredient_ids)