from pathlib import Path
from typing import List, Tuple
import numpy as np
from numpy.typing import NDArray

from Day_10.const import DAY, EXAMPLE_INPUT_FILE_NAME, INPUT_FILE_NAME
from Day_10.load_input import load_input
from Day_10.part_2 import update_position
from Day_10.part_2 import solution as part_2_solution
from utils.solve import solve
from utils.display_np import display_np_bool

def construct_points_grid(positions: List[Tuple[int, int]]) -> NDArray[np.bool_]:
    X = [x for x, _ in positions]
    Y = [y for _, y in positions]

    Xmin, Xmax = min(X), max(X)
    Ymin, Ymax = min(Y), max(Y)
    points = np.zeros((Xmax - Xmin + 1, Ymax - Ymin + 1), dtype=bool)
    for x, y in positions:
        points[x - Xmin, y - Ymin] = True
    
    return points.T

def compute_score(positions: List[Tuple[int, int]]) -> int:
    X = [x for x, _ in positions]
    Y = [y for _, y in positions]

    X_diff = sum([abs(x2 - x1) for x2 in X for x1 in X])
    Y_diff = sum([abs(y2 - y1) for y2 in Y for y1 in Y])
    return X_diff + Y_diff

def solution(positions: List[Tuple[int, int]], velocities: List[Tuple[int, int]]) -> int:
    t = part_2_solution(positions, velocities)
    final_positions = [update_position(position, velocity, t) for position, velocity in zip(positions, velocities)]
    points = construct_points_grid(final_positions)
    return "\n" + display_np_bool(points, supress=True)

if __name__ == "__main__":
    example_positions, example_velocities = load_input(Path(f"Day_{DAY:02d}/{EXAMPLE_INPUT_FILE_NAME}"))
    print("Example:", end="")
    print(solution(example_positions, example_velocities))
    print()

    positions, velocities = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))
    solve(solution, positions, velocities)