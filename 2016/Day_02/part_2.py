from pathlib import Path
from typing import List

from Day_02.const import DAY, EXAMPLE_INPUT_FILE_NAME, INPUT_FILE_NAME
from Day_02.load_input import load_input
from Day_02.part_1 import simulate_bathroom_code
from utils.solve import test, solve

def solution(instructions: List[str]) -> int:
    keypad = [
        [None, None, "1", None, None],
        [None, "2",  "3", "4",  None],
        ["5",  "6",  "7", "8",  "9"],
        [None, "A",  "B", "C",  None],
        [None, None, "D", None, None],
    ]
    start_position = (2, 0)
    buttons = simulate_bathroom_code(instructions, keypad, start_position)
    return "".join(buttons)

if __name__ == "__main__":
    example_instructions = load_input(Path(f"Day_{DAY:02d}/{EXAMPLE_INPUT_FILE_NAME}"))
    expected_answer = "5DB3"
    test(expected_answer, solution, example_instructions)

    instructions = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))
    solve(solution, instructions)