from pathlib import Path
from typing import List, TypeAlias, Tuple
import numpy as np
from numpy.typing import NDArray
import hashlib

from Day_12.const import DAY, EXAMPLE_INPUT_FILE_NAME, INPUT_FILE_NAME
from Day_12.load_input import load_input
from utils.solve import test, solve

PresentShape: TypeAlias = NDArray[np.bool_]
Region: TypeAlias = Tuple[int, int, List[int]]

def display_present_shape(present_shape):
    arr = np.where(present_shape, '#', '.')
    s = "\n".join("".join(row) for row in arr)
    print(s)

def hash_array(arr: np.ndarray) -> str:
    arr_bytes = arr.tobytes()
    info_bytes = str(arr.shape).encode() + str(arr.dtype).encode()
    combined = info_bytes + arr_bytes
    
    return hashlib.md5(combined).hexdigest()

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
        key = hash_array(orientation)
        unique_orientations[key] = orientation
    
    return list(unique_orientations.values())

def add_state_to_cache(cache, state, shape_quantity, value):
    all_state_orientations = get_shape_orientations(state)
    for oriented_state in all_state_orientations:
        key = (hash_array(oriented_state), tuple(shape_quantity))
        cache[key] = value

def get_row_placeability(state, all_orientations, orientation_indexes, shape_quantity):
    W, L = state.shape
    shape_placeable_in_row_indexes = [False] * state.shape[0]

    for index, orientation_group in zip(orientation_indexes, all_orientations):
        if shape_quantity[index] == 0:
            continue
        for present_orientation in orientation_group:
            w, l = present_orientation.shape
            
            for i in range(W - w + 1):
                if shape_placeable_in_row_indexes[i]:
                    continue

                shape_placeable_in_row = False
                for j in range(L - l + 1):
                    overlap = (state[i:i+w, j:j+l] != 0) & present_orientation
                    
                    if not np.any(overlap):
                        shape_placeable_in_row = True
                        break
                
                if shape_placeable_in_row:
                    shape_placeable_in_row_indexes[i] = True
        
        return shape_placeable_in_row_indexes

def can_shapes_fit_in_region(all_orientations, orientation_indexes, region):
    W, L, shape_quantity = region

    def dfs(state, shape_quantity_remaining):
        key = (hash_array(state), tuple(shape_quantity_remaining))
        if key in cache:
            return cache[key]
        
        W, L = state.shape
        if W <= 1 or L <= 1:
            add_state_to_cache(cache, state, shape_quantity_remaining, False)
            return False

        shape_placeable_in_row_indexes = get_row_placeability(state, all_orientations, orientation_indexes, shape_quantity_remaining)
        shape_placeable_in_col_indexes = get_row_placeability(state.T, all_orientations, orientation_indexes, shape_quantity_remaining)
        if not any(shape_placeable_in_row_indexes) or not any(shape_placeable_in_col_indexes):
            add_state_to_cache(cache, state, shape_quantity_remaining, False)
            return False

        print(shape_quantity_remaining)
        print("\n".join("".join([str(int(x)) for x in row]) for row in state))
        print([k for k, placeable in enumerate(shape_placeable_in_row_indexes) if placeable])
        print()

        for i in range(W):
            if not shape_placeable_in_row_indexes[i]:
                below_state = state[i+1:].copy()
                below_solution = dfs(below_state, shape_quantity_remaining)
                if below_solution:
                    return True
                continue
            
            for j in range(L):
                
                for index, orientation_group in zip(orientation_indexes, all_orientations):
                    if shape_quantity_remaining[index] == 0:
                        continue
                    
                    for present_orientation in orientation_group:
                        w, l = present_orientation.shape
                        if j+l >= L:
                            break

                        overlap = (state[i:i+w, j:j+l] != 0) & present_orientation
                        if np.any(overlap):
                            continue
                        updated_state = state.copy()
                        updated_state[i:i+w, j:j+l] += np.where(present_orientation, index, 0)
                        updated_shape_quantity_remaining = list(shape_quantity_remaining)
                        updated_shape_quantity_remaining[index] -= 1

                        if np.sum(updated_shape_quantity_remaining) == 0:
                            add_state_to_cache(cache, updated_state, updated_shape_quantity_remaining, True)
                            print("Solution Found")
                            print(updated_state)
                            return True
                        
                        solution_found = dfs(updated_state, updated_shape_quantity_remaining)
                        if solution_found:
                            return True
        
        add_state_to_cache(cache, state, shape_quantity_remaining, False)
        return False

    state = np.zeros((W, L))
    return dfs(state, shape_quantity)

cache = {}

def solution(present_shapes: List[PresentShape], regions: List[Region]) -> int:
    # max_region_width = max(W for W, _, _ in regions)
    # max_region_length = max(L for _, L, _ in regions)

    all_orientations = []
    orientation_indexes = []

    for index, present_shape in enumerate(present_shapes):
        shape_orientations = get_shape_orientations(present_shape)
        all_orientations.append(shape_orientations)
        orientation_indexes.append(index)

    count = 0
    for region in regions:
        if can_shapes_fit_in_region(all_orientations, orientation_indexes, region):
            count += 1
        else:
            print("No Solution :(")
    
    return count

if __name__ == "__main__":
    example_present_shapes, example_regions = load_input(Path(f"Day_{DAY}/{EXAMPLE_INPUT_FILE_NAME}"))
    expected_answer = 2
    test(expected_answer, solution, example_present_shapes, example_regions)

    # present_shapes, regions = load_input(Path(f"Day_{DAY}/{INPUT_FILE_NAME}"))
    # solve(solution, present_shapes, regions)