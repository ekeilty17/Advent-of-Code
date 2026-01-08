from pathlib import Path
from typing import List, Tuple
import numpy as np
from numpy.typing import NDArray

from Day_09.const import DAY, EXAMPLE_INPUT_FILE_NAME, INPUT_FILE_NAME
from Day_09.load_input import load_input
from Day_09.part_1 import compute_rectangle_area
from utils.solve import test, solve

# Just for debugging
def compute_polygon_boundary(vertices: List[Tuple[int, int]]) -> NDArray[np.bool_]:
    Xmin = min(x for x, _ in vertices)
    Xmax = max(x for x, _ in vertices)
    Ymin = min(y for _, y in vertices)
    Ymax = max(y for _, y in vertices)
    
    Xmin = Ymin = 0
    polygon_grid = np.zeros(((Xmax - Xmin)+1, (Ymax - Ymin)+1), dtype=bool)
    
    for k in range(len(vertices)):
        x1, y1 = vertices[k]
        x2, y2 = vertices[(k + 1) % len(vertices)]

        i1, j1 = x1 - Xmin, y1 - Ymin
        i2, j2 = x2 - Xmin, y2 - Ymin

        i1, i2 = min(i1, i2), max(i1, i2)
        j1, j2 = min(j1, j2), max(j1, j2)

        polygon_grid[i1:i2+1, j1:j2+1] = True

    print(np.where(polygon_grid, "X", ".").T)

    return polygon_grid

def is_contained_in_polygon(vertices: List[Tuple[int, int]], coord1: Tuple[int, int], coord2: Tuple[int, int]) -> bool:
    x1, y1 = coord1
    x2, y2 = coord2

    x1, x2 = min(x1, x2), max(x1, x2)
    y1, y2 = min(y1, y2), max(y1, y2)

    for k in range(len(vertices)):
        X1, Y1 = vertices[k]
        X2, Y2 = vertices[(k + 1) % len(vertices)]

        X1, X2 = min(X1, X2), max(X1, X2)
        Y1, Y2 = min(Y1, Y2), max(Y1, Y2)

        # Why this works is complicated, see the README.md
        if X1 == X2:
            X = X1
            if (x1 < X < x2) and max(y1, Y1) < min(y2, Y2):
                return False
        else:
            Y = Y1
            if max(x1, X1) < min(x2, X2) and (y1 < Y < y2):
                return False

    return True


def solution(grid_locations: List[Tuple[int, int]]) -> int:

    max_area = 0
    for i in range(len(grid_locations)):
        coord1 = grid_locations[i]
        for j in range(i+1, len(grid_locations)):
            coord2 = grid_locations[j]
            if is_contained_in_polygon(grid_locations, coord1, coord2):
                area = compute_rectangle_area(coord1, coord2)
                max_area = max(max_area, area)

    return max_area

if __name__ == "__main__":
    example_grid_locations = load_input(Path(f"Day_{DAY:02d}/{EXAMPLE_INPUT_FILE_NAME}"))
    expected_answer = 24
    test(expected_answer, solution, example_grid_locations)

    grid_locations = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))
    solve(solution, grid_locations)