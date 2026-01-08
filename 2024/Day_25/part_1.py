from pathlib import Path
from typing import List
import numpy as np
from numpy.typing import NDArray

from Day_25.const import DAY, EXAMPLE_INPUT_FILE_NAME, INPUT_FILE_NAME
from Day_25.load_input import load_input
from utils.solve import test, solve
from utils.display import *

def get_height(schematic: NDArray[str]) -> NDArray[int]:
    return np.array([np.sum(col == "#")-1 for col in schematic.T])

def solution(locks: List[List[List[str]]], keys: List[List[List[str]]]) -> int:
    locks = [np.array(lock) for lock in locks]
    keys = [np.array(key) for key in keys]

    locks_by_height = [get_height(lock) for lock in locks]
    keys_by_height = [get_height(key) for key in keys]

    count = 0
    for lock_height in locks_by_height:
        for key_height in keys_by_height:
            if all((lock_height + key_height) <= 5):
                count += 1

    return count

if __name__ == "__main__":
    example_locks, example_keys = load_input(Path(f"Day_{DAY:02d}/{EXAMPLE_INPUT_FILE_NAME}"))
    expected_answer = 3
    test(expected_answer, solution, example_locks, example_keys)

    locks, keys = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))
    solve(solution, locks, keys)