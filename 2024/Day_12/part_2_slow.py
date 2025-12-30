from pathlib import Path
from typing import List, Tuple, Set
import numpy as np
from numpy.typing import NDArray

from Day_12.const import DAY, EXAMPLE_INPUT_FILE_NAME, INPUT_FILE_NAME
from Day_12.load_input import load_input
from Day_12.part_1 import compute_regions, normalize_garden
from utils.grid import get_offset_indices
from utils.test import test

def compute_fense_price(garden: NDArray[str], region_indices: Set[Tuple[int, int]]) -> int:
    
    area = len(region_indices)

    offsets = [
        (0, 0), (0, 1), 
        (1, 0), (1, 1)
    ]

    corner_exception_1 = [
        True,  False,
        False, True
    ]
    corner_exception_2 = [
        False, True,
        True,  False
    ]

    num_corners = 0
    for i in range(garden.shape[0]-1):
        for j in range(garden.shape[1]-1):
            neighbor_indexes = get_offset_indices(garden, i, j, offsets)
            pattern = [(index in region_indices) for index in neighbor_indexes]
            if sum(pattern) % 2 == 1:
                num_corners += 1
            elif np.array_equal(pattern, corner_exception_1) or np.array_equal(pattern, corner_exception_2):
                num_corners += 2

    return area * num_corners      # number of corners == number of edges


def solution(garden: List[List[str]]) -> int:
    # convert repeated plot types into distinct regions
    garden = np.array(garden)
    regions = compute_regions(garden)
    normalized_garden = normalize_garden(garden, regions)

    # Easily access distinct regions
    regions_by_unique_ID = {
        int(region_ID): list(zip(*np.where(normalized_garden == region_ID)))
        for region_ID in np.unique(normalized_garden)
    }

    total = 0
    for region_ID, region_indices in regions_by_unique_ID.items():
        if region_ID == 0:
            # disregard padded region
            continue
        total += compute_fense_price(normalized_garden, region_indices)

    return total

if __name__ == "__main__":
    
    example_garden = load_input(Path(f"Day_{DAY:02d}/{EXAMPLE_INPUT_FILE_NAME}"))
    garden = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))

    expected_answer = 1206
    test(expected_answer, solution, example_garden)

    total = solution(garden)
    print("Puzzle Answer:", total)