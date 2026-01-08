from pathlib import Path
from typing import List, Tuple
import numpy as np
from numpy.typing import NDArray

from Day_04.const import DAY, EXAMPLE_INPUT_FILE_NAME, INPUT_FILE_NAME
from Day_04.load_input import load_input
from utils.grid import get_neighbor_indices
from utils.solve import test, solve

def solution(grid_of_rolls: NDArray[np.bool_], max_rolls: int) -> int:

    accessible_spots = np.zeros_like(grid_of_rolls, dtype=bool)

    for (i, j), value in np.ndenumerate(grid_of_rolls):
        neighbor_indices = get_neighbor_indices(grid_of_rolls.shape, i, j)
        neighbors = grid_of_rolls[*zip(*neighbor_indices)]
        if np.sum(neighbors) < max_rolls:
            accessible_spots[i, j] = True
    
    accessible_rolls = accessible_spots & grid_of_rolls
    return int(np.sum(accessible_rolls))

if __name__ == "__main__":
    max_rolls = 4

    example_grid = load_input(Path(f"Day_{DAY:02d}/{EXAMPLE_INPUT_FILE_NAME}"))
    expected_answer = 13
    test(expected_answer, solution, example_grid, max_rolls)

    grid = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))
    solve(solution, grid, max_rolls)