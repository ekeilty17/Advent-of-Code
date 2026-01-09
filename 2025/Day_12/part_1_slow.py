from pathlib import Path
from typing import List, TypeAlias, Tuple
import numpy as np
from numpy.typing import NDArray

from Day_12.const import DAY, EXAMPLE_INPUT_FILE_NAME, INPUT_FILE_NAME
from Day_12.load_input import load_input
from utils.solve import test, solve

Present: TypeAlias = NDArray[np.bool_]
Region: TypeAlias = Tuple[Tuple[int, int], List[int]]

def get_present_orientations(present: Present) -> List[Present]:
    present = present.copy()

    present_orientations = [present.copy()]
    for _ in range(3):
        present = np.rot90(present)
        present_orientations.extend([
            present.copy(),
            np.flip(present.copy(), axis=0),
            np.flip(present.copy(), axis=1)
        ])

    unique_orientations = {}
    for orientation in present_orientations:
        key = tuple(orientation.flatten())
        unique_orientations[key] = orientation
    
    return list(unique_orientations.values())

def can_presents_fit_in_region(present_groups: List[List[Present]], region: Region):
    region_shape, present_quantities = region
    present_shape = present_groups[0][0].shape   # assume all presents are the same shape

    def dfs(state, present_quantity_remaining):
        W, L = state.shape
        w, l = present_shape

        if W <= 1 or L <= 1:
            return False

        for i in range(W-w+1):
            for j in range(L-l+1):
                for index, present_group in enumerate(present_groups):
                    if present_quantity_remaining[index] == 0:
                        continue

                    for present_orientation in present_group:
                        w, l = present_orientation.shape

                        overlap = (state[i:i+w, j:j+l] != 0) & present_orientation
                        if np.any(overlap):
                            continue
                        updated_state = state.copy()
                        updated_state[i:i+w, j:j+l] += np.where(present_orientation, index, 0)
                        updated_present_quantity_remaining = list(present_quantity_remaining)
                        updated_present_quantity_remaining[index] -= 1

                        if np.sum(updated_present_quantity_remaining) == 0:
                            return True
                        
                        solution_found = dfs(updated_state, updated_present_quantity_remaining)
                        if solution_found:
                            return True
        
        return False

    state = np.zeros(region_shape, dtype=int)
    return dfs(state, present_quantities)


def solution(presents: List[Present], regions: List[Region]) -> int:
    present_groups = []

    for present in presents:
        present_orientations = get_present_orientations(present)
        present_groups.append(present_orientations)

    total = 0
    for region in regions:
        if can_presents_fit_in_region(present_groups, region):
            total += 1
    
    return total

if __name__ == "__main__":
    # example_present_shapes, example_regions = load_input(Path(f"Day_{DAY}/{EXAMPLE_INPUT_FILE_NAME}"))
    # expected_answer = 2
    # test(expected_answer, solution, example_present_shapes, example_regions)

    present_shapes, regions = load_input(Path(f"Day_{DAY}/{INPUT_FILE_NAME}"))
    solve(solution, present_shapes, regions)