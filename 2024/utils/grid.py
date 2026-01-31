from typing import List, Tuple, Set
import numpy as np
from numpy.typing import NDArray

def get_offset_indices(grid: NDArray[str], i: int, j: int, offsets: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    i = i % grid.shape[0]
    j = j % grid.shape[1]
    neighbor_indexes = [(i+a, j+b) for a, b in offsets]
    neighbor_indexes = [(a, b) for a, b in neighbor_indexes if 0 <= a < grid.shape[0] and 0 <= b < grid.shape[1]]
    return neighbor_indexes

def get_orthogonal_neighbor_indices(grid: NDArray[str], i: int, j: int) -> List[Tuple[int, int]]:
    offsets = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    return get_offset_indices(grid, i, j, offsets)

def get_diagonal_neighbor_indices(grid: NDArray[str], i: int, j: int) -> List[Tuple[int, int]]:
    offsets = [(-1, -1), (1, -1), (-1, 1), (1, 1)]
    return get_offset_indices(grid, i, j, offsets)

def get_neighbor_indices(grid: NDArray[str], i: int, j: int) -> List[Tuple[int, int]]:
    return get_orthogonal_neighbor_indices(grid, i, j) + get_diagonal_neighbor_indices(grid, i, j)

def get_position_of_value(grid: NDArray[str], char: str) -> Tuple[int, int]:
    indices = np.where(grid == char)
    indices = list(zip(*indices))

    if len(indices) == 0:
        raise ValueError(f"Did not find '{char}' inside of the grid")
    if len(indices) > 1:
        raise ValueError(f"Found multiple instances of '{char}' inside of the grid")
    
    index = indices[0]
    return tuple([int(x) for x in index])