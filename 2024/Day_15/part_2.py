from pathlib import Path
from typing import List, Tuple, Set
import numpy as np

from Day_15.const import DAY, EXAMPLE_INPUT_FILE_NAME, INPUT_FILE_NAME
from Day_15.const import SMALL_EXAMPLE_INPUT_FILE_NAME_PART_2 as SMALL_EXAMPLE_INPUT_FILE_NAME
from Day_15.load_input import load_input
from Day_15.part_1 import lanternfish_distance_score
from utils.test import test
from utils.grid import get_position_of_value
from utils.display import *

def expand_warehouse(warehouse: List[List[str]]):
    expansion_map = {
        "#": "##",
        "O": "[]",
        ".": "..",
        "@": "@.",
    }
    expanded_warehouse = []
    for row in warehouse:
        expanded_row = []
        for cell in row:
            expanded_row.extend(list(expansion_map[cell]))
        expanded_warehouse.append(expanded_row)
    
    return expanded_warehouse

def get_connected_boxes(warehouse: NDArray[str], start: Tuple[int, int]) -> Set[Tuple[int, int]]:
    box_positions = set([])
    stack = [start]
    while stack:
        position = stack.pop()
        x, y = position
        
        if position in box_positions:
            continue

        if warehouse[position] in ["#", "."]:
            continue

        if warehouse[position] == "@":
            stack.append((x+1, y))
            continue

        if warehouse[position] == "[":
            box_positions.add(position)
            stack.append((x, y+1))
            stack.append((x+1, y))
            continue
        
        if warehouse[position] == "]":
            box_positions.add(position)
            stack.append((x, y-1))
            stack.append((x+1, y))
            continue
    
    return box_positions

def make_down_move(warehouse: NDArray[str], robot_position: Tuple[int, int]) -> Tuple[int, int]:
    i, j = robot_position

    connected_box_positions = get_connected_boxes(warehouse, robot_position)
    
    position_updates = {
        (x, y): (x+1, y) for x, y in connected_box_positions | {robot_position}
    }
    
    updated_warehouse = warehouse.copy()
    for (x1, y1), (x2, y2) in position_updates.items():
        if warehouse[x2, y2] == "#":
            return robot_position
        updated_warehouse[x2, y2] = warehouse[x1, y1]

    empty_cells = set(position_updates.keys()) - set(position_updates.values())
    for x, y in empty_cells:
        updated_warehouse[x, y] = "."

    warehouse[:] = updated_warehouse
    return i+1, j

def make_right_move(warehouse: NDArray[str], robot_position: Tuple[int, int]) -> Tuple[int, int]:
    i, j = robot_position

    indices = np.where(warehouse[i, j:] == ".")[0]
    if len(indices) == 0:
        return i, j
    
    k = min(indices)
    idx = (i, slice(j, j+k+1))
    if "#" in  warehouse[idx]:
        return i, j
    
    warehouse[idx] = np.roll(warehouse[idx], 1)
    return i, j+1

def make_move(warehouse: NDArray[str], robot_position: Tuple[int, int], move: str) -> Tuple[int, int]:
    
    if move == "^":
        warehouse = np.flipud(warehouse)
        robot_position = warehouse.shape[0] - (robot_position[0] + 1), robot_position[1]
        robot_position = make_down_move(warehouse, robot_position)
        return warehouse.shape[0] - (robot_position[0] + 1), robot_position[1]
    
    if move == ">":
        return make_right_move(warehouse, robot_position)

    if move == "v":
        return make_down_move(warehouse, robot_position)

    if move == "<":
        warehouse = np.fliplr(warehouse)
        robot_position = robot_position[0], warehouse.shape[1] - (robot_position[1] + 1)
        robot_position = make_right_move(warehouse, robot_position)
        return robot_position[0], warehouse.shape[1] - (robot_position[1] + 1)

    raise ValueError(f"Expected one of '^', '>', 'v', '<'. Instead of '{move}'")

def solution(warehouse: List[List[str]], moves: List[str]) -> int:
    warehouse = np.array(expand_warehouse(warehouse))

    robot_position = get_position_of_value(warehouse, '@')
    for move in moves:
        robot_position = make_move(warehouse, robot_position, move)

    return lanternfish_distance_score(warehouse, "[")

if __name__ == "__main__":
    
    small_example_warehouse, small_example_moves = load_input(Path(f"Day_{DAY:02d}/{SMALL_EXAMPLE_INPUT_FILE_NAME}"))
    example_warehouse, example_moves = load_input(Path(f"Day_{DAY:02d}/{EXAMPLE_INPUT_FILE_NAME}"))
    warehouse, moves = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))

    small_expected_answer = 618
    test(small_expected_answer, solution, small_example_warehouse, small_example_moves)

    expected_answer = 9021
    test(expected_answer, solution, example_warehouse, example_moves)

    total = solution(warehouse, moves)
    print("Puzzle Answer:", total)