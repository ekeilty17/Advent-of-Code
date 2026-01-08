from pathlib import Path
from typing import List, Tuple
import numpy as np
from numpy.typing import NDArray

from Day_06.const import DAY, INPUT_FILE_NAME
from Day_06.const import EXAMPLE_INPUT_FILE_NAME_PART_2 as EXAMPLE_INPUT_FILE_NAME 
from Day_06.load_input import load_input
from utils.solve import test, solve

def execute_instruction(
        brightness: NDArray[int], 
        instruction_type: str, 
        coord_1: Tuple[int, int], 
        coord_2: Tuple[int, int]
    ):
    x1, y1 = coord_1
    x2, y2 = coord_2

    sub_brightness = brightness[x1:x2+1, y1:y2+1]
    if instruction_type == "turn on":
        sub_brightness += 1
    elif instruction_type == "turn off":
        sub_brightness -= 1 
        np.maximum(sub_brightness, 0, out=sub_brightness)
    elif instruction_type == "toggle":
        sub_brightness += 2
    else:
        raise ValueError(f"Expected instruction type of 'turn on', 'turn off', or 'toggle'. Instead got {instruction_type}.")

    return brightness

def solution(
        instructions: List[Tuple[str, Tuple[int, int], Tuple[int, int]]],
        grid_shape: Tuple[int, int]
    ) -> int:
    
    brightness = np.zeros(grid_shape, dtype=int)
    for instruction in instructions:
        brightness = execute_instruction(brightness, *instruction)

    return np.sum(brightness)

if __name__ == "__main__":
    grid_shape = (1000, 1000)

    example_instructions = load_input(Path(f"Day_{DAY:02d}/{EXAMPLE_INPUT_FILE_NAME}"))
    expected_answer = 2000001
    test(expected_answer, solution, example_instructions, grid_shape)

    instructions = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))
    solve(solution, instructions, grid_shape)