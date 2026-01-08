from pathlib import Path
from typing import List

from Day_24.const import DAY, EXAMPLE_INPUT_FILE_NAME, INPUT_FILE_NAME
from Day_24.load_input import load_input
from Day_17.part_2 import get_all_combinations
from utils.solve import test, solve

def solution(weights: List[int]) -> int:
    print(weights)
    group_weight = sum(weights) // 3
    print(group_weight)
    print(get_all_combinations(weights, group_weight))

if __name__ == "__main__":
    example_weights = load_input(Path(f"Day_{DAY:02d}/{EXAMPLE_INPUT_FILE_NAME}"))
    expected_answer = None
    test(expected_answer, solution, example_weights)

    weights = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))
    solve(solution, weights)