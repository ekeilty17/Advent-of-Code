from pathlib import Path
from typing import List, Tuple

from Day_05.const import DAY, EXAMPLE_INPUT_FILE_NAME, INPUT_FILE_NAME
from Day_05.load_input import load_input
from Day_05.interval_set import InternvalSet
from utils.test import test

def solution(ingredient_id_ranges: List[Tuple[int, int]]) -> int:
    
    interval_set = InternvalSet()
    for ingredient_id_range in ingredient_id_ranges:
        interval_set.add(*ingredient_id_range)

    fresh_ingredients_count = 0
    for a, b in interval_set:
        fresh_ingredients_count += (b - a + 1)

    return fresh_ingredients_count

if __name__ == "__main__":
    
    example_ingredient_id_ranges, _ = load_input(Path(f"Day_{DAY:02d}/{EXAMPLE_INPUT_FILE_NAME}"))
    ingredient_id_ranges, _ = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))

    expected_answer = 14
    test(expected_answer, solution, example_ingredient_id_ranges)

    total = solution(ingredient_id_ranges)
    print("Puzzle Answer:", total)