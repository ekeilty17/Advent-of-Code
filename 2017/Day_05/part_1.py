from pathlib import Path
from typing import List

from Day_05.const import DAY, EXAMPLE_INPUT_FILE_NAME, INPUT_FILE_NAME
from Day_05.load_input import load_input
from utils.solve import test, solve

def solution(jump_offsets: List[int]) -> int:
    total_jumps = 0
    
    position = 0
    while 0 <= position < len(jump_offsets):
        jump_offset = jump_offsets[position]
        jump_offsets[position] += 1
        position += jump_offset
        total_jumps += 1
    
    return total_jumps

if __name__ == "__main__":
    example_jump_offsets = load_input(Path(f"Day_{DAY:02d}/{EXAMPLE_INPUT_FILE_NAME}"))
    expected_answer = 10
    test(expected_answer, solution, example_jump_offsets)

    jump_offsets = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))
    solve(solution, jump_offsets)