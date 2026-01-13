from pathlib import Path
from typing import List, Dict, Tuple

from Day_02.const import DAY, EXAMPLE_INPUT_FILE_NAME, INPUT_FILE_NAME
from Day_02.load_input import load_input
from utils.solve import test, solve

def update_position(
        curr_position: Tuple[int, int],
        move: str, 
        grid_shape: Tuple[int, int]
    ) -> Tuple[int, int]:
    
    move_to_offset = {
        "U": (-1, 0),
        "D": (1, 0),
        "L": (0, -1),
        "R": (0, 1)
    }

    dx, dy = move_to_offset[move]
    x, y = curr_position
    if 0 <= x+dx < grid_shape[0] and 0 <= y+dy < grid_shape[1]:
        return x+dx, y+dy
    return x, y

def simulate_bathroom_code(
        instructions: List[str], 
        keypad: List[List[int]], 
        start_position: Tuple[int, int],
    ) -> List[str]:
    
    keypad_shape = (len(keypad), len(keypad[0]))

    buttons = []
    x, y = start_position
    for instruction in instructions:
        for move in instruction:
            new_x, new_y = update_position((x, y), move, keypad_shape)
            if keypad[new_x][new_y]:
                x, y = new_x, new_y
        
        button = keypad[x][y]
        buttons.append(button)

    return buttons

def solution(instructions: List[str]) -> str:
    keypad = [
        ["1", "2", "3"],
        ["4", "5", "6"],
        ["7", "8", "9"]
    ]
    start_position = (1, 1)
    buttons = simulate_bathroom_code(instructions, keypad, start_position)
    return "".join(buttons)

if __name__ == "__main__":
    example_instructions = load_input(Path(f"Day_{DAY:02d}/{EXAMPLE_INPUT_FILE_NAME}"))
    expected_answer = "1985"
    test(expected_answer, solution, example_instructions)

    instructions = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))
    solve(solution, instructions)