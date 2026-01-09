from pathlib import Path
from typing import List, TypeAlias, Tuple
import numpy as np
from numpy.typing import NDArray

from Day_12.const import DAY, EXAMPLE_INPUT_FILE_NAME, INPUT_FILE_NAME
from Day_12.load_input import load_input
from utils.solve import test, solve

Present: TypeAlias = NDArray[np.bool_]
Region: TypeAlias = Tuple[Tuple[int, int], List[int]]

def fit_without_interlocking(present_shape: Tuple[int, int], region_shape: Tuple[int, int], present_quantities: List[int]) -> bool:
    present_area = present_shape[0] * present_shape[1] * sum(present_quantities)
    
    region_area = 1
    region_area *= (region_shape[0] // present_shape[0]) * present_shape[0]
    region_area *= (region_shape[1] // present_shape[1]) * present_shape[1]

    return present_area <= region_area

def too_large_to_fit(presents: Present, region_shape: Tuple[int, int], present_quantities: List[int]) -> bool:
    present_area = 0
    for present, quantity in zip(presents, present_quantities):
        present_area += np.sum(present) * quantity
    
    region_area = region_shape[0] * region_shape[1]
    return present_area > region_area

def solution(presents: List[Present], regions: List[Region]) -> int:
    present_shape = presents[0].shape   # assume all shapes are the same size

    total = 0
    for region_shape, present_quantities in regions:
        if fit_without_interlocking(present_shape, region_shape, present_quantities):
            total += 1
        elif too_large_to_fit(presents, region_shape, present_quantities):
            continue
        else:
            raise Exception(f"Simple checks failed and the search space is too large - {region_shape}, {present_quantities}.")
    
    return total

if __name__ == "__main__":
    # example_present_shapes, example_regions = load_input(Path(f"Day_{DAY}/{EXAMPLE_INPUT_FILE_NAME}"))
    # expected_answer = 2
    # test(expected_answer, solution, example_present_shapes, example_regions)

    present_shapes, regions = load_input(Path(f"Day_{DAY}/{INPUT_FILE_NAME}"))
    solve(solution, present_shapes, regions)