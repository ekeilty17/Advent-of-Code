from pathlib import Path
from typing import List, Tuple
import numpy as np
from numpy.typing import NDArray

from Day_06.const import DAY, EXAMPLE_INPUT_FILE_NAME, INPUT_FILE_NAME
from Day_06.load_input import load_input
from utils.test import test

def rotate_guard(guard: str) -> str:
    guards = ["^", ">", "v", "<"]
    index = guards.index(guard)
    return guards[(index+1)%len(guards)]

def update_guard_position(map: NDArray[str], guard_index: Tuple[int, int]) -> Tuple[Tuple[int, int], bool]:
    m, n = map.shape
    i, j = guard_index
    guard = map[guard_index]
    guard_left = False

    if guard == "^":
        indexes = np.where(map[:i+1, j] == "#")[0]
        k = indexes[-1] if indexes.size > 0 else -1
        guard_index = (k+1, j)
        if k == -1:
            guard_left = True
    elif guard == ">":
        indexes = np.where(map[i, j:] == "#")[0]
        k = indexes[0] + j if indexes.size > 0  else n
        guard_index = (i, k-1)
        if k == n:
            guard_left = True
    elif guard == "v":
        indexes = np.where(map[i:, j] == "#")[0]
        k = indexes[0] + i if indexes.size > 0  else m
        guard_index = (k-1, j)
        if k == m:
            guard_left = True
    elif guard == "<":
        indexes = np.where(map[i, :j+1] == "#")[0]
        k = indexes[-1] if indexes.size > 0  else -1
        guard_index = (i, k+1)
        if k == -1:
            guard_left = True
    else:
        raise ValueError(f"Expected one of '^', '>', '<', 'v' as the guard value, but got '{guard}' instead.")

    return guard_index, guard_left

def compute_patrolled(map: NDArray[str], guard_start_index: Tuple[int, int]) -> Tuple[NDArray[bool], bool]:
    map = map.copy()
    patrolled = np.zeros_like(map, dtype=bool)

    guard_left = False
    guard_states = set([])

    guard_index = guard_start_index
    prev_guard_index = None
    while True:
        prev_guard_index = guard_index
        guard = map[guard_index]
        guard_index, guard_left = update_guard_position(map, guard_index)

        (r1, c1), (r2, c2) = prev_guard_index, guard_index
        patrolled[min(r1,r2):max(r1,r2)+1, min(c1,c2):max(c1,c2)+1] = True

        map[prev_guard_index] = "."
        if guard_left:
            break
        
        # Guard is in the same state as before, thus it has started looping
        if (guard, guard_index) in guard_states:
            break
        guard_states.add((guard, guard_index))

        guard = rotate_guard(guard)
        map[guard_index] = guard
    
    return patrolled, guard_left

def solution(map: List[List[str]]) -> int:
    map = np.array(map)

    try:
        i, j = np.where(map == "^")
        guard_start_index = i[0], j[0]
    except:
        raise ValueError("Failed to find '^' in the 2D array 'map'")
    
    patrolled, _ = compute_patrolled(map, guard_start_index)
    return np.sum(patrolled)


if __name__ == "__main__":
    
    example_map = load_input(Path(f"Day_{DAY:02d}/{EXAMPLE_INPUT_FILE_NAME}"))
    map = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))

    expected_answer = 41
    test(expected_answer, solution, example_map)

    total = solution(map)
    print("Puzzle Answer:", total)