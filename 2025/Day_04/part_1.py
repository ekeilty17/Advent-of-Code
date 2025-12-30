from pathlib import Path
from typing import List, Tuple
import numpy as np
from numpy.typing import NDArray

from Day_04.const import DAY, EXAMPLE_INPUT_FILE_NAME, INPUT_FILE_NAME
from Day_04.load_input import load_input
from utils.test import test

def get_neighbor(grid: NDArray[np.bool_], i: int, j: int) -> List[Tuple[int, int]]:
    neighbor_indexes = [(i+a, j+b) for a in range(-1, 2) for b in range(-1, 2) if not (a == 0 and b == 0)]
    neighbor_indexes = [(a, b) for a, b in neighbor_indexes if 0 <= a < grid.shape[0] and 0 <= b < grid.shape[1]]
    rows, cols = zip(*neighbor_indexes)
    neighbors = grid[list(rows), list(cols)]
    return neighbors

def solution(grid_of_rolls: NDArray[np.bool_], max_rolls: int) -> int:

    accessible_spots = np.zeros_like(grid_of_rolls, dtype=bool)

    for (i, j), value in np.ndenumerate(grid_of_rolls):
        neighbors = get_neighbor(grid_of_rolls, i, j)
        if np.sum(neighbors) < max_rolls:
            accessible_spots[i, j] = True
    
    accessible_rolls = accessible_spots & grid_of_rolls
    return int(np.sum(accessible_rolls))

if __name__ == "__main__":
    
    example_grid = load_input(Path(f"Day_{DAY:02d}/{EXAMPLE_INPUT_FILE_NAME}"))
    grid = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))

    max_rolls = 4

    expected_answer = 13
    test(expected_answer, solution, example_grid, max_rolls)

    total = solution(grid, max_rolls)
    print("Puzzle Answer:", total)