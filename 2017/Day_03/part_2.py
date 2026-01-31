import numpy as np

from utils.grid import get_neighbor_indices
from utils.solve import solve

def solution(N: int) -> int:
    spiral = np.array([[1]])

    while True:

        # Add to right side
        line = [0] * spiral.shape[0]
        spiral = np.column_stack((spiral, line))
        for i in reversed(range(spiral.shape[0])):
            cell_idx = (i, -1)
            spiral[cell_idx] = sum([spiral[idx] for idx in get_neighbor_indices(spiral.shape, *cell_idx)])
            if spiral[cell_idx] > N:
                return spiral[cell_idx]

        # Top becomes the right, and recurse
        spiral = np.rot90(spiral, -1)

if __name__ == "__main__":
    N = 312051
    solve(solution, N)