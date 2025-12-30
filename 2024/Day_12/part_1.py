from pathlib import Path
from typing import List, Tuple, Set
import numpy as np
from numpy.typing import NDArray

from Day_12.const import DAY, EXAMPLE_INPUT_FILE_NAME, INPUT_FILE_NAME
from Day_12.load_input import load_input
from utils.test import test
from utils.grid import get_orthogonal_neighbor_indices

# Essentially a DFS to get all connected components
def compute_regions(garden: NDArray[str]) -> List[Set[Tuple[int, int]]]:

    def dfs(garden, index, visited=None):
        if visited is None:
            visited = np.zeros_like(garden, dtype=bool)
        visited[index] = True

        for neighbor_index in get_orthogonal_neighbor_indices(garden, *index):
            if visited[neighbor_index]:
                continue
            if garden[neighbor_index] != garden[index]:
                continue
            dfs(garden, neighbor_index, visited)
        
        return visited
    
    regions = []
    for index in np.ndindex(garden.shape):
        if any([index in region for region in regions]):
            continue
        visited = dfs(garden, index)
        region = np.argwhere(visited)
        region = [(int(idx[0]), int(idx[1])) for idx in region]
        regions.append(set(region))

    return regions

def normalize_garden(garden: NDArray[str], regions: List[Set[Tuple[int, int]]]) -> NDArray[int]:
    normalized_garden = np.zeros_like(garden, dtype=int)

    for index, region_indices in enumerate(regions, 1):
        rows, cols = zip(*region_indices)
        normalized_garden[rows, cols] = index

    normalized_garden = np.pad(normalized_garden, pad_width=1)
    return normalized_garden

def compute_fense_price(garden: NDArray[str], region_indices: Set[Tuple[int, int]]) -> int:
    
    area = len(region_indices)

    perimeter = 0
    for i, j in region_indices:
        neighbor_indexes = get_orthogonal_neighbor_indices(garden, i, j)
        perimeter += sum([garden[a, b] != garden[i, j] for a, b in neighbor_indexes])
    
    return area * perimeter

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
            # padding doesn't contribute to total
            continue
        total += compute_fense_price(normalized_garden, region_indices)

    return total

if __name__ == "__main__":
    
    example_garden = load_input(Path(f"Day_{DAY:02d}/{EXAMPLE_INPUT_FILE_NAME}"))
    garden = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))

    expected_answer = 1930
    test(expected_answer, solution, example_garden)

    total = solution(garden)
    print("Puzzle Answer:", total)