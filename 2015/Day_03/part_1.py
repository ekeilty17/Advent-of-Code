from pathlib import Path
from typing import Tuple

from Day_03.const import DAY, EXAMPLE_INPUT_FILE_NAME, INPUT_FILE_NAME
from Day_03.load_input import load_input
from utils.test import test

def update_position(curr_pos: Tuple[int, int], move: str) -> Tuple[int, int]:
    i, j = curr_pos
    if move == ">":
        i += 1
    elif move == "<":
        i -= 1
    elif move == "^":
        j += 1
    elif move == "v":
        j -= 1
    else:
        raise ValueError(f"Expected one of '>', '<', '^', or 'v'. Instead got {move}")
    return i, j

def solution(moves: str) -> int:
    curr_pos = (0, 0)
    present_positions = {curr_pos}

    for move in moves:
        curr_pos = update_position(curr_pos, move)
        present_positions.add(curr_pos)
    
    return len(present_positions)

if __name__ == "__main__":
    
    example_moves = load_input(Path(f"Day_{DAY:02d}/{EXAMPLE_INPUT_FILE_NAME}"))
    moves = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))

    expected_answer = 4
    test(expected_answer, solution, example_moves)

    total = solution(moves)
    print("Puzzle Answer:", total)