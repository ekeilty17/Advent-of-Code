from pathlib import Path
from typing import List, Tuple
import numpy as np
from numpy.typing import NDArray

from Day_04.const import DAY, EXAMPLE_INPUT_FILE_NAME, INPUT_FILE_NAME
from Day_04.load_input import load_input
from Day_04.part_1 import get_neighbor
from utils.test import test

def get_accessible_rolls(grid_of_rolls: NDArray[np.bool_], max_rolls: int) -> NDArray[np.bool_]:

    accessible_spots = np.zeros_like(grid_of_rolls, dtype=bool)

    for (i, j), value in np.ndenumerate(grid_of_rolls):
        neighbors = get_neighbor(grid_of_rolls, i, j)
        if np.sum(neighbors) < max_rolls:
            accessible_spots[i, j] = True
    
    accessible_rolls = accessible_spots & grid_of_rolls
    return accessible_rolls

# Not really sure how much faster I can make this. I could replace the np.arrays with actual bitmaps. But ugh too much effort
def solution(grid_of_rolls: NDArray[np.bool_], max_rolls: int) -> int:

    accessible_rolls = get_accessible_rolls(grid_of_rolls, max_rolls)
    rolls_removed = np.sum(accessible_rolls)

    while np.sum(accessible_rolls) > 0:
        grid_of_rolls = grid_of_rolls & (~accessible_rolls)
        accessible_rolls = get_accessible_rolls(grid_of_rolls, max_rolls)
        rolls_removed += np.sum(accessible_rolls)

    return int(rolls_removed)

if __name__ == "__main__":
    
    example_grid = load_input(Path(f"Day_{DAY:02d}/{EXAMPLE_INPUT_FILE_NAME}"))
    grid = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))

    max_rolls = 4

    expected_answer = 43
    test(expected_answer, solution, example_grid, max_rolls)

    total = solution(grid, max_rolls)
    print("Puzzle Answer:", total)