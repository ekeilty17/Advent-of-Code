from pathlib import Path
from typing import List, Tuple
import numpy as np
from numpy.typing import NDArray

from Day_15.const import DAY, EXAMPLE_INPUT_FILE_NAME, INPUT_FILE_NAME
from Day_15.const import SMALL_EXAMPLE_INPUT_FILE_NAME_PART_1 as SMALL_EXAMPLE_INPUT_FILE_NAME
from Day_15.load_input import load_input
from Day_15.part_1 import lanternfish_distance_score
from utils.grid import get_position_of_value
from utils.solve import test, solve

def make_down_move(warehouse: NDArray[str], robot_position: Tuple[int, int]) -> Tuple[int, int]:
    i, j = robot_position

    indices = np.where(warehouse[i:, j] == ".")[0]
    if len(indices) == 0:
        return i, j
    
    k = min(indices)
    idx = (slice(i, i+k+1), j)
    if "#" in  warehouse[idx]:
        return i, j
    
    warehouse[idx] = np.roll(warehouse[idx], 1)
    return i+1, j

def make_move(warehouse: NDArray[str], robot_position: Tuple[int, int], move: str) -> Tuple[int, int]:
    if move == "^":
        warehouse = np.flipud(warehouse)
        robot_position = warehouse.shape[0] - (robot_position[0] + 1), robot_position[1]
        robot_position = make_down_move(warehouse, robot_position)
        return warehouse.shape[0] - (robot_position[0] + 1), robot_position[1]
    
    if move == ">":
        warehouse = warehouse.T
        robot_position = robot_position[1], robot_position[0]
        robot_position = make_down_move(warehouse, robot_position)
        warehouse = warehouse.T
        return robot_position[1], robot_position[0]

    if move == "v":
        return make_down_move(warehouse, robot_position)

    if move == "<":
        warehouse = warehouse.T
        robot_position = robot_position[1], robot_position[0]
        robot_position = make_move(warehouse, robot_position, move="^")
        warehouse = warehouse.T
        return robot_position[1], robot_position[0]
    
    raise ValueError(f"Expected one of '^', '>', 'v', '<'. Instead of '{move}'")

def solution(warehouse: List[List[str]], moves: List[str]) -> int:
    warehouse = np.array(warehouse)
    
    robot_position = get_position_of_value(warehouse, '@')
    for move in moves:
        robot_position = make_move(warehouse, robot_position, move)

    return lanternfish_distance_score(warehouse, "O")

if __name__ == "__main__":
    small_example_warehouse, small_example_moves = load_input(Path(f"Day_{DAY:02d}/{SMALL_EXAMPLE_INPUT_FILE_NAME}"))
    small_expected_answer = 2028
    test(small_expected_answer, solution, small_example_warehouse, small_example_moves)

    example_warehouse, example_moves = load_input(Path(f"Day_{DAY:02d}/{EXAMPLE_INPUT_FILE_NAME}"))
    expected_answer = 10092
    test(expected_answer, solution, example_warehouse, example_moves)

    warehouse, moves = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))
    solve(solution, warehouse, moves)