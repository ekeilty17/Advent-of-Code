from pathlib import Path
from typing import List, Tuple, Dict, Any
import numpy as np
from numpy.typing import NDArray

from Day_21.const import DAY, EXAMPLE_INPUT_FILE_NAME, INPUT_FILE_NAME
from Day_21.load_input import load_input
from utils.solve import test, solve
from utils.display_np import *

def pattern_to_ndarray(pattern: str) -> NDArray[np.bool_]:
    return np.array([[x == "#" for x in row] for row in pattern.split("/")])

def hash_ndarray(arr: NDArray[np.bool_]):
    return tuple(arr.flatten())

def get_orientated_rules(input_pattern: str, output_pattern: str) -> Dict[Any, NDArray[np.bool_]]:
    input_pattern = pattern_to_ndarray(input_pattern)
    output_pattern = pattern_to_ndarray(output_pattern)

    all_orientations = [(input_pattern.copy(), output_pattern.copy())]
    for _ in range(3):
        input_pattern = np.rot90(input_pattern)
        all_orientations.extend([
            (input_pattern.copy(), output_pattern.copy()),
            (np.flip(input_pattern.copy(), axis=0), output_pattern.copy()),
            (np.flip(input_pattern.copy(), axis=1), output_pattern.copy())
        ])

    unique_orientations = {}
    for input_pattern, output_pattern in all_orientations:
        key = hash_ndarray(input_pattern)
        unique_orientations[key] = output_pattern
    
    return unique_orientations

def preprocess_rules(rules: Dict[str, str]) -> Dict[int, Dict[Any, NDArray[np.bool_]]]:
    rules_by_size = {}
    for input_pattern, output_pattern in rules:
        size = len(input_pattern.split("/"))
        if size not in rules_by_size:
            rules_by_size[size] = {}

        oriented_rules = get_orientated_rules(input_pattern, output_pattern)
        rules_by_size[size].update(oriented_rules)
    
    return rules_by_size

def partition_by_size_and_apply_rules(grid: NDArray[np.bool_], rules: Dict[Any, NDArray[np.bool_]], size: int) -> List[List[NDArray[np.bool_] | None]]:
    replaced_sub_grids = []
    for i in range(0, grid.shape[0], size):
        replaced_sub_grids.append([])
        
        for j in range(0, grid.shape[1], size):
            sub_grid = grid[i:i+size, j:j+size]
            sub_input_pattern = hash_ndarray(sub_grid)
            output_pattern = rules.get(sub_input_pattern)
            replaced_sub_grids[-1].append(output_pattern)
    
    return replaced_sub_grids

def merge_subgrids(sub_grids: List[List[NDArray[np.bool_]]]):
    """
    sub_grids is assumed to be square
    also each element in sub_grids is assumed to be square

    I'm sure there is some numpy function that would do this, but I decided to do it myself
    """
    sub_grid_shape = sub_grids[0][0].shape[0]
    new_grid_shape = sub_grid_shape * len(sub_grids)
    
    new_grid = np.zeros((new_grid_shape, new_grid_shape), dtype=bool)
    for I in range(len(sub_grids)):
        for J in range(len(sub_grids[I])):
            i1, i2 = sub_grid_shape*I, sub_grid_shape*I+sub_grid_shape
            j1, j2 = sub_grid_shape*J, sub_grid_shape*J+sub_grid_shape
            new_grid[i1:i2, j1: j2] = sub_grids[I][J]

    return new_grid

def apply_rules(grid: NDArray[np.bool_], rules_by_size: Dict[int, Dict[Any, NDArray[np.bool_]]]) -> NDArray[np.bool_]:
    for size, size_rules in sorted(rules_by_size.items()):
        if grid.shape[0] % size != 0:
            continue
        
        replaced_sub_grids = partition_by_size_and_apply_rules(grid, size_rules, size)
        
        if all([sub_grid is not None for row in replaced_sub_grids for sub_grid in row]):
            return merge_subgrids(replaced_sub_grids)

def solution(rules: Dict[str, str], start_pattern: str, N: int) -> int:
    rules_by_size = preprocess_rules(rules)
    grid = pattern_to_ndarray(start_pattern)
    for _ in range(N):
        grid = apply_rules(grid, rules_by_size)
        
    return np.sum(grid)

if __name__ == "__main__":
    start_pattern = ".#./..#/###"

    example_rules = load_input(Path(f"Day_{DAY:02d}/{EXAMPLE_INPUT_FILE_NAME}"))
    example_N = 2
    expected_answer = 12
    test(expected_answer, solution, example_rules, start_pattern, example_N)

    rules = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))
    N = 5
    solve(solution, rules, start_pattern, N)