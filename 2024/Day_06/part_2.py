from pathlib import Path
from typing import List
import numpy as np

from Day_06.const import DAY, EXAMPLE_INPUT_FILE_NAME, INPUT_FILE_NAME
from Day_06.load_input import load_input
from Day_06.part_1 import compute_patrolled
from utils.solve import test, solve

def solution(map: List[List[str]]) -> int:
    map = np.array(map)

    try:
        i, j = np.where(map == "^")
        guard_start_index = i[0], j[0]
    except:
        raise ValueError("Failed to find '^' in the 2D array 'map'")
    
    # We only have to check where the guard has patrolled
    # putting an additional obstical where the guard has does patrol will not change his path
    patrolled, _ = compute_patrolled(map, guard_start_index)

    count = 0
    rows, cols = np.where(patrolled == True)
    for i, j in zip(rows, cols):
        if (i, j) == guard_start_index:
            continue
        imap = map.copy()
        imap[i, j] = "#"
        _, guard_left = compute_patrolled(imap, guard_start_index)
        
        # If the guard did not leave, then they must have started looping
        if not guard_left:
            count += 1
    
    return count

if __name__ == "__main__":
    example_map = load_input(Path(f"Day_{DAY:02d}/{EXAMPLE_INPUT_FILE_NAME}"))
    expected_answer = 6
    test(expected_answer, solution, example_map)

    map = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))
    solve(solution, map)