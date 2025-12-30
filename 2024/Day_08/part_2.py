from pathlib import Path
from typing import List
import numpy as np
from numpy.typing import NDArray

from Day_08.const import DAY, EXAMPLE_INPUT_FILE_NAME, INPUT_FILE_NAME
from Day_08.load_input import load_input
from Day_08.part_1 import get_antenna_locations
from utils.test import test

def solution(map: List[List[str]]) -> int:
    map = np.array(map)
    m, n = map.shape
    
    antenna_locations_by_frequencies = get_antenna_locations(map)
    
    antinode_locations = set([])
    for frequency, antenna_locations in antenna_locations_by_frequencies.items():
        for i1, j1 in antenna_locations:
            for i2, j2 in antenna_locations:
                if i1 == i2 and j1 == j2:
                    continue
                antinode_locations.add((i1, j1))

                di = i2 - i1
                dj = j2 - j1

                antinode_i, antinode_j = i2 + di, j2 + dj
                while (0 <= antinode_i < m) and (0 <= antinode_j < n):
                    antinode_locations.add((antinode_i, antinode_j))
                    antinode_i, antinode_j = antinode_i + di, antinode_j + dj

    return len(antinode_locations)

if __name__ == "__main__":
    
    example_map = load_input(Path(f"Day_{DAY:02d}/{EXAMPLE_INPUT_FILE_NAME}"))
    map = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))

    expected_answer = 34
    test(expected_answer, solution, example_map)

    total = solution(map)
    print("Puzzle Answer:", total)