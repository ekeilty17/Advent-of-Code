from pathlib import Path
from typing import List

from Day_24.const import DAY, EXAMPLE_INPUT_FILE_NAME, INPUT_FILE_NAME
from Day_24.load_input import load_input
from Day_24.part_1 import solution
from utils.solve import test, solve

if __name__ == "__main__":
    num_groups = 4

    example_weights = load_input(Path(f"Day_{DAY:02d}/{EXAMPLE_INPUT_FILE_NAME}"))
    expected_answer = 44
    test(expected_answer, solution, example_weights, num_groups)

    weights = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))
    solve(solution, weights, num_groups)