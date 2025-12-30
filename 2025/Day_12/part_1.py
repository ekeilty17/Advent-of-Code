from pathlib import Path
from typing import List, TypeAlias, Tuple
import numpy as np
from numpy.typing import NDArray
import hashlib

from Day_12.const import DAY, EXAMPLE_INPUT_FILE_NAME, INPUT_FILE_NAME
from Day_12.load_input import load_input
from utils.test import test

PresentShape: TypeAlias = NDArray[np.bool_]
Region: TypeAlias = Tuple[int, int, List[int]]

def display_present_shape(present_shape):
    arr = np.where(present_shape, '#', '.')
    s = "\n".join("".join([str(x) for x in row]) for row in arr)
    print(s)

def get_shape_orientations(present_shape):
    present_shape = present_shape.copy()

    shape_orientations = [present_shape.copy()]
    for _ in range(3):
        present_shape = np.rot90(present_shape)
        shape_orientations.extend([
            present_shape.copy(),
            np.flip(present_shape.copy(), axis=0),
            np.flip(present_shape.copy(), axis=1)
        ])

    unique_orientations = {}
    for orientation in shape_orientations:
        key = tuple(orientation.flatten())
        unique_orientations[key] = orientation
    
    return list(unique_orientations.values())

# def get_row_placeability(state, all_orientations, orientation_indexes, shape_quantity):
#     W, L = state.shape
#     shape_placeable_in_row_indexes = [False] * state.shape[0]

#     for index, orientation_group in zip(orientation_indexes, all_orientations):
#         if shape_quantity[index] == 0:
#             continue
#         for present_orientation in orientation_group:
#             w, l = present_orientation.shape
            
#             for i in range(W - w + 1):
#                 if shape_placeable_in_row_indexes[i]:
#                     continue

#                 shape_placeable_in_row = False
#                 for j in range(L - l + 1):
#                     overlap = (state[i:i+w, j:j+l] != 0) & present_orientation
                    
#                     if not np.any(overlap):
#                         shape_placeable_in_row = True
#                         break
                
#                 if shape_placeable_in_row:
#                     shape_placeable_in_row_indexes[i] = True
        
#         return shape_placeable_in_row_indexes

def can_shapes_fit_in_region(shape_groups, region):
    W, L, final_shape_quantity = region

    # let's assume all shapes are the same dimensions (which they are)

    zero_shape_quantity = [0]*len(final_shape_quantity)
    D = [
            [
                {
                    tuple(zero_shape_quantity): [np.zeros((x, y))] if x != 0 and y != 0 else []
                } 
                for y in range(L+1)
            ] 
            for x in range(W+1)
        ]

    x = 3
    y = 3
    for shape_quantity, states in D[x][y].items():
        if all(a == b for a, b in zip(shape_quantity, final_shape_quantity)):
            return True
        if any(a > b for a, b in zip(shape_quantity, final_shape_quantity)):
            continue
        
        for state in states:
            for index, shape_group in enumerate(shape_groups):
                for oriented_shape in shape_group:
                    w, l = oriented_shape.shape
                    if x > w or y > l:
                        continue

                    updated_shape_quantity = list(shape_quantity)
                    updated_shape_quantity[index] += 1

                    for i in range(x-w+1):
                        for j in range(y-l+1):
                            D[w][l][tuple(updated_shape_quantity)].append(oriented_shape)

                            overlap = (state != 0) & oriented_shape
                            if np.any(overlap):
                                continue
                            updated_state = state.copy()
                            updated_state[i:i+w, j:j+l] += np.where(present_orientation, index, 0)
                            updated_shape_quantity_remaining = list(shape_quantity_remaining)
                            updated_shape_quantity_remaining[index] -= 1

    # for j in range(l+1, L):


    # for j in range(l+1, L):
    #     for key, shapes in D.items():
            
        
    for i, row in enumerate(D):
        for j, cell in enumerate(row):
            for key, values in cell.items():
                print(i, j, key)
                for shape in values:
                    display_present_shape(shape)
                    print()
    
    return None

def solution(present_shapes: List[PresentShape], regions: List[Region]) -> int:
    # max_region_width = max(W for W, _, _ in regions)
    # max_region_length = max(L for _, L, _ in regions)

    shape_groups = []

    for present_shape in present_shapes:
        shape_orientations = get_shape_orientations(present_shape)
        shape_groups.append(shape_orientations)
        # for shape in shape_orientations:
        #     display_present_shape(shape)
        #     print()
        # print("-"*50)

    count = 0
    for region in regions:
        if can_shapes_fit_in_region(shape_groups, region):
            count += 1
        else:
            print("No Solution :(")
        break
    
    return count

if __name__ == "__main__":
    
    example_present_shapes, example_regions = load_input(Path(f"Day_{DAY}/{EXAMPLE_INPUT_FILE_NAME}"))
    present_shapes, regions = load_input(Path(f"Day_{DAY}/{INPUT_FILE_NAME}"))

    expected_answer = 2
    test(expected_answer, solution, example_present_shapes, example_regions)

    # total = solution(present_shapes, regions)
    # print("Puzzle Answer:", total)