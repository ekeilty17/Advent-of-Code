from pathlib import Path
from typing import List, Tuple
import numpy as np

from Day_09.const import DAY, EXAMPLE_INPUT_FILE_NAME, INPUT_FILE_NAME
from Day_09.load_input import load_input
from utils.solve import test, solve

def compute_rectangle_area(coord1: Tuple[int, int], coord2: Tuple[int, int]) -> int:
    x1, y1 = coord1
    x2, y2 = coord2
    area = (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)
    return area

def solution(grid_locations: List[Tuple[int, int]]) -> int:

    max_area = 0
    for i in range(len(grid_locations)):
        coord1 = grid_locations[i]
        for j in range(i+1, len(grid_locations)):
            coord2 = grid_locations[j]
            area = compute_rectangle_area(coord1, coord2)
            max_area = max(max_area, area)

    return max_area

if __name__ == "__main__":
    example_grid_locations = load_input(Path(f"Day_{DAY:02d}/{EXAMPLE_INPUT_FILE_NAME}"))
    expected_answer = 50
    test(expected_answer, solution, example_grid_locations)

    grid_locations = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))
    solve(solution, grid_locations)