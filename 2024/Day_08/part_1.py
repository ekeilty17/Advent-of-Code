from pathlib import Path
from typing import List, Dict, Tuple
import numpy as np
from numpy.typing import NDArray

from Day_08.const import DAY, EXAMPLE_INPUT_FILE_NAME, INPUT_FILE_NAME
from Day_08.load_input import load_input
from utils.test import test

def get_antenna_locations(map: NDArray[str]) -> Dict[str, List[Tuple[int, int]]]:
    frequencies = [x for x in np.unique(map) if x != '.']
    return {
        frequency: [(int(i), int(j)) for i, j in list(zip(*np.where(map == frequency)))]
        for frequency in frequencies
    }

def solution(map: List[List[str]]) -> int:
    map = np.array(map)
    m, n = map.shape
    
    antenna_locations_by_frequencies = get_antenna_locations(map)
    
    antinode_locations = set([])
    for antenna_locations in antenna_locations_by_frequencies.values():
        for i1, j1 in antenna_locations:
            for i2, j2 in antenna_locations:
                if i1 == i2 and j1 == j2:
                    continue
                
                di = i2 - i1
                dj = j2 - j1
                antinode_i, antinode_j = i2 + di, j2 + dj

                if (0 <= antinode_i < m) and (0 <= antinode_j < n):
                    antinode_locations.add((antinode_i, antinode_j))
    
    return len(antinode_locations)

if __name__ == "__main__":
    
    example_map = load_input(Path(f"Day_{DAY:02d}/{EXAMPLE_INPUT_FILE_NAME}"))
    map = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))

    expected_answer = 14
    test(expected_answer, solution, example_map)

    total = solution(map)
    print("Puzzle Answer:", total)