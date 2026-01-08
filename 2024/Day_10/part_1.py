from pathlib import Path
from typing import List, Tuple, Optional
import numpy as np
from numpy.typing import NDArray

from Day_10.const import DAY, EXAMPLE_INPUT_FILE_NAME, INPUT_FILE_NAME
from Day_10.load_input import load_input
from utils.grid import get_orthogonal_neighbor_indices
from utils.solve import test, solve

def compute_trail(map: NDArray[bool], position: Tuple[int, int], visited: Optional[List[bool]]=None):
    if visited is None:
        visited = np.zeros_like(map, dtype=bool)
    visited[position] = True

    for neighbor in get_orthogonal_neighbor_indices(map, *position):
        if visited[neighbor]:
            continue
        if map[neighbor] != map[position]+1:
            continue
        compute_trail(map, neighbor, visited)

    return visited

def solution(map: List[List[int]]) -> int:
    map = np.array(map)

    trailheads = [(int(x), int(y)) for x, y in list(zip(*np.where(map == 0)))]
    peaks = (map == 9)

    count = 0
    for trailhead in trailheads:
        trail = compute_trail(map, trailhead)
        count += len(map[trail & peaks])
    
    return count

if __name__ == "__main__":
    example_map = load_input(Path(f"Day_{DAY:02d}/{EXAMPLE_INPUT_FILE_NAME}"))
    expected_answer = 36
    test(expected_answer, solution, example_map)

    map = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))
    solve(solution, map)