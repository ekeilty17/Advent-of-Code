from typing import Set, Tuple
import numpy as np
from numpy.typing import NDArray

from Day_10.part_2 import knot_hash
from utils.grid import get_orthogonal_neighbor_indices
from utils.solve import test, solve
from utils.display_np import display_np_bool

def construct_disk(key_string: str) -> NDArray[np.bool_]:
    N = 128
    disk = np.zeros((N, N), dtype=bool)

    for row_index in range(N):
        hex_string = knot_hash(f"{key_string}-{row_index}")
        row = int(hex_string, 16)
        row_binary_string = bin(row)[2:].zfill(N)
        row_binary_digits = list(map(int, row_binary_string))
        disk[row_index] = row_binary_digits

    return disk

def get_connected_component(disk: NDArray[np.bool_], start: Tuple[int, int]) -> Set[Tuple[int, int]]:
    component = set([])
    stack = [start]

    while stack:
        node = stack.pop()

        if node in component:
            continue
        component.add(node)

        for neighbor in get_orthogonal_neighbor_indices(disk.shape, *node):
            if disk[neighbor]:
                stack.append(neighbor)
    
    return component

def solution(key_string: str) -> int:
    disk = construct_disk(key_string)

    components = []
    for index in np.ndindex(disk.shape):
        if not disk[index]:
            continue
        if any(index in component for component in components):
            continue
        component = get_connected_component(disk, index)
        components.append(component)
    
    # For debugging
    # component_disk = np.zeros_like(disk, dtype=int)
    # for i, component in enumerate(components, 1):
    #     for index in component:
    #         component_disk[index] = i
    
    return len(components)

if __name__ == "__main__":
    example_key_string = "flqrgnkx"
    expected_answer = 1242
    test(expected_answer, solution, example_key_string)

    key_string = "hwlqcszp"
    solve(solution, key_string)