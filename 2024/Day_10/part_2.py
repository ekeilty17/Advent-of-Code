from pathlib import Path
from typing import List, Tuple, Optional
import numpy as np
from numpy.typing import NDArray

from Day_10.const import DAY, EXAMPLE_INPUT_FILE_NAME, INPUT_FILE_NAME
from Day_10.load_input import load_input
from utils.test import test
from utils.grid import get_orthogonal_neighbor_indices

def compute_trail_paths(map: NDArray[bool], position: Tuple[int, int], path: Optional[List[bool]]=None):
    if path is None:
        path = []
    path.append(position)

    if map[position] == 9:
        return [path]

    paths = []
    for neighbor in get_orthogonal_neighbor_indices(map, *position):
        if neighbor in path:
            continue
        if map[neighbor] != map[position]+1:
            continue
        paths.extend( compute_trail_paths(map, neighbor, list(path)) )

    return paths

def solution(map: List[List[int]]) -> int:
    map = np.array(map)

    trailheads = [(int(x), int(y)) for x, y in list(zip(*np.where(map == 0)))]

    count = 0
    for trailhead in trailheads:
        trail_paths = compute_trail_paths(map, trailhead)
        count += len(trail_paths)

    return count

if __name__ == "__main__":
    
    example_map = load_input(Path(f"Day_{DAY:02d}/{EXAMPLE_INPUT_FILE_NAME}"))
    map = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))

    expected_answer = 81
    test(expected_answer, solution, example_map)

    total = solution(map)
    print("Puzzle Answer:", total)