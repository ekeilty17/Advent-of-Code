from pathlib import Path
from typing import List, Tuple
import numpy as np
from numpy.typing import NDArray

from Day_15.const import DAY, EXAMPLE_INPUT_FILE_NAME, INPUT_FILE_NAME
from Day_15.const import SMALL_EXAMPLE_INPUT_FILE_NAME_PART_1 as SMALL_EXAMPLE_INPUT_FILE_NAME
from Day_15.load_input import load_input
from utils.test import test
from utils.grid import get_position_of_value

def make_move(warehouse: NDArray[str], robot_position: Tuple[int, int], move: str) -> Tuple[int, int]:
    i, j = robot_position
    if move == "^":
        indices = np.where(warehouse[:i, j] == ".")[0]
        if len(indices) == 0:
            return i, j
        k = max(indices)
        idx = (slice(k, i+1), j)
        if "#" in  warehouse[idx]:
            return i, j
        warehouse[idx] = np.roll(warehouse[idx], -1)
        return i-1, j

    if move == ">":
        indices = np.where(warehouse[i, j:] == ".")[0]
        if len(indices) == 0:
            return i, j
        k = min(indices)
        idx = (i, slice(j, j+k+1))
        if "#" in  warehouse[idx]:
            return i, j
        warehouse[idx] = np.roll(warehouse[idx], 1)
        return i, j+1

    if move == "v":
        indices = np.where(warehouse[i:, j] == ".")[0]
        if len(indices) == 0:
            return i, j
        k = min(indices)
        idx = (slice(i, i+k+1), j)
        if "#" in  warehouse[idx]:
            return i, j
        warehouse[idx] = np.roll(warehouse[idx], 1)
        return i+1, j

    if move == "<":
        indices = np.where(warehouse[i, :j] == ".")[0]
        if len(indices) == 0:
            return i, j
        k = max(indices)
        idx = (i, slice(k, j+1))
        if "#" in  warehouse[idx]:
            return i, j
        warehouse[idx] = np.roll(warehouse[idx], -1)
        return i, j-1

    raise ValueError(f"Expected one of '^', '>', 'v', '<'. Instead of '{move}'")

def lanternfish_distance_score(warehouse: NDArray[str], box_char: str) -> int:
    rows, cols = np.where(warehouse == box_char)
    return sum(100 * rows) + sum(cols)

def solution(warehouse: List[List[str]], moves: List[str]) -> int:
    warehouse = np.array(warehouse)
    
    robot_position = get_position_of_value(warehouse, '@')
    for move in moves:
        robot_position = make_move(warehouse, robot_position, move)

    return lanternfish_distance_score(warehouse, "O")

if __name__ == "__main__":
    
    small_example_warehouse, small_example_moves = load_input(Path(f"Day_{DAY:02d}/{SMALL_EXAMPLE_INPUT_FILE_NAME}"))
    example_warehouse, example_moves = load_input(Path(f"Day_{DAY:02d}/{EXAMPLE_INPUT_FILE_NAME}"))
    warehouse, moves = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))

    small_expected_answer = 2028
    test(small_expected_answer, solution, small_example_warehouse, small_example_moves)

    expected_answer = 10092
    test(expected_answer, solution, example_warehouse, example_moves)

    total = solution(warehouse, moves)
    print("Puzzle Answer:", total)