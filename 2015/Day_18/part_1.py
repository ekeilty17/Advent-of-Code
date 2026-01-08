from pathlib import Path
from typing import List
import numpy as np
from numpy.typing import NDArray

from Day_18.const import DAY, EXAMPLE_INPUT_FILE_NAME, INPUT_FILE_NAME
from Day_18.load_input import load_input
from utils.solve import test, solve
from utils.grid import get_neighbor_indices

def conway_game_of_life_update(state: NDArray[bool]) -> None:
    state_copy = state.copy()
    for (i, j), value in np.ndenumerate(state):
        neighbor_indices = get_neighbor_indices(state.shape, i, j)
        neighor_values = state_copy[*zip(*neighbor_indices)]
        if sum(neighor_values) == 3:
            state[i, j] = True
        elif value and sum(neighor_values) != 2:
            state[i, j] = False

def solution(lights: List[List[str]], N: int) -> int:
    lights = np.array([[light == "#" for light in row] for row in lights], dtype=bool)
    
    for _ in range(N):
        conway_game_of_life_update(lights)
    
    return np.sum(lights)

if __name__ == "__main__":
    example_lights = load_input(Path(f"Day_{DAY:02d}/{EXAMPLE_INPUT_FILE_NAME}"))
    example_N = 4
    expected_answer = 4
    test(expected_answer, solution, example_lights, example_N)

    lights = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))
    N = 100
    solve(solution, lights, N)