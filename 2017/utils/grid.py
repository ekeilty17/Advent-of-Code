from typing import List, Tuple, Any
import numpy as np
from numpy.typing import NDArray

def get_offset_indices(shape: Tuple[int, int], i: int, j: int, offsets: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    neighbor_indexes = [(i+a, j+b) for a, b in offsets]
    neighbor_indexes = [(a, b) for a, b in neighbor_indexes if 0 <= a < shape[0] and 0 <= b < shape[1]]
    return neighbor_indexes

def get_orthogonal_neighbor_indices(shape: Tuple[int, int], i: int, j: int) -> List[Tuple[int, int]]:
    offsets = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    return get_offset_indices(shape, i, j, offsets)

def get_diagonal_neighbor_indices(shape: Tuple[int, int], i: int, j: int) -> List[Tuple[int, int]]:
    offsets = [(-1, -1), (1, -1), (-1, 1), (1, 1)]
    return get_offset_indices(shape, i, j, offsets)

def get_neighbor_indices(shape: Tuple[int, int], i: int, j: int) -> List[Tuple[int, int]]:
    return get_orthogonal_neighbor_indices(shape, i, j) + get_diagonal_neighbor_indices(shape, i, j)

def get_positions_of_value(grid: NDArray[Any], value: Any) -> List[Tuple[int, int]]:
    indices = np.where(grid == value)
    indices = list(zip(*indices))
    return [tuple([int(x) for x in index]) for index in indices]