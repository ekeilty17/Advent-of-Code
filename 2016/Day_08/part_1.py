from pathlib import Path
from typing import List, Dict, Any, Tuple
import numpy as np
from numpy.typing import NDArray

from Day_08.const import DAY, EXAMPLE_INPUT_FILE_NAME, INPUT_FILE_NAME
from Day_08.load_input import load_input
from utils.solve import test, solve

def execute_instructions(instructions: List[Dict[str, Any]], screen_shape: Tuple[int, int]) -> NDArray[np.bool_]:
    screen = np.zeros(screen_shape, dtype=bool)

    for instruction in instructions:
        if instruction["type"] == "rect":
            x, y = instruction["shape"]
            screen[:y, :x] = True

        elif instruction["type"] == "rotate row":
            index = instruction["index"]
            shift = instruction["shift"]
            screen[index] = np.roll(screen[index], shift)
        
        elif instruction["type"] == "rotate column":
            index = instruction["index"]
            shift = instruction["shift"]
            screen[:, index] = np.roll(screen[:, index], shift)
        
    return screen

def solution(instructions: List[Dict[str, Any]], screen_shape: Tuple[int, int]) -> int:
    screen = execute_instructions(instructions, screen_shape)
    return np.sum(screen)

if __name__ == "__main__":
    example_instructions = load_input(Path(f"Day_{DAY:02d}/{EXAMPLE_INPUT_FILE_NAME}"))
    example_screen_shape = (3, 7)
    expected_answer = 6
    test(expected_answer, solution, example_instructions, example_screen_shape)

    screen_shape = (6, 50)
    instructions = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))
    solve(solution, instructions, screen_shape)