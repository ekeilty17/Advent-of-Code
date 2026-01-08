from pathlib import Path
from typing import List
import numpy as np

from Day_18.const import DAY, EXAMPLE_INPUT_FILE_NAME, INPUT_FILE_NAME
from Day_18.load_input import load_input
from Day_18.part_1 import conway_game_of_life_update
from utils.solve import test, solve

def solution(lights: List[List[str]], N: int) -> int:
    lights = np.array([[light == "#" for light in row] for row in lights], dtype=bool)
    always_on = [(0, 0), (0, -1), (-1, 0), (-1, -1)]
    lights[*zip(*always_on)] = True
    
    for _ in range(N):
        conway_game_of_life_update(lights)
        lights[*zip(*always_on)] = True
    
    return np.sum(lights)

if __name__ == "__main__":
    example_lights = load_input(Path(f"Day_{DAY:02d}/{EXAMPLE_INPUT_FILE_NAME}"))
    example_N = 5
    expected_answer = 17
    test(expected_answer, solution, example_lights, example_N)

    lights = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))
    N = 100
    solve(solution, lights, N)