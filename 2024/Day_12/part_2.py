from pathlib import Path
from typing import List, Tuple, Set, Dict
import numpy as np
from numpy.typing import NDArray

from Day_12.const import DAY, EXAMPLE_INPUT_FILE_NAME, INPUT_FILE_NAME
from Day_12.load_input import load_input
from Day_12.part_1 import compute_regions, normalize_garden
from utils.grid import get_offset_indices
from utils.test import test

def compute_number_of_corners(garden: NDArray[str], regions_by_unique_ID: Dict[int, Set[Tuple[int, int]]]) -> Dict[int, int]:
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

    num_corners_by_region = {region_ID: 0 for region_ID in regions_by_unique_ID.keys()}

    for i in range(garden.shape[0]-1):
        for j in range(garden.shape[1]-1):
            neighbor_indexes = get_offset_indices(garden, i, j, offsets)
            
            rows, cols = zip(*neighbor_indexes)
            unique_regions = set([int(x) for x in garden[rows, cols]])

            for region_ID in unique_regions:
                pattern = [(index in regions_by_unique_ID[region_ID]) for index in neighbor_indexes]
                if sum(pattern) % 2 == 1:
                    num_corners_by_region[region_ID] += 1
                elif np.array_equal(pattern, corner_exception_1) or np.array_equal(pattern, corner_exception_2):
                    num_corners_by_region[region_ID] += 2

    return num_corners_by_region


def compute_total_fense_price(garden: NDArray[str], regions_by_unique_ID: Dict[int, Set[Tuple[int, int]]]) -> int:
    
    num_corners_by_region = compute_number_of_corners(garden, regions_by_unique_ID)
    area_by_region = {ID: len(region_indices) for ID, region_indices in regions_by_unique_ID.items()}

    return sum([
        area_by_region[region_ID] * num_corners_by_region[region_ID]    # number of corners == number of edges
        for region_ID in regions_by_unique_ID.keys()
        if region_ID != 0                                               # disregard padded region
    ])

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

    return compute_total_fense_price(normalized_garden, regions_by_unique_ID)

if __name__ == "__main__":
    
    example_garden = load_input(Path(f"Day_{DAY:02d}/{EXAMPLE_INPUT_FILE_NAME}"))
    garden = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))

    expected_answer = 1206
    test(expected_answer, solution, example_garden)

    total = solution(garden)
    print("Puzzle Answer:", total)