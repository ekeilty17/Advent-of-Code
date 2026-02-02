from pathlib import Path
from typing import List

from Day_06.const import DAY, EXAMPLE_INPUT_FILE_NAME, INPUT_FILE_NAME
from Day_06.load_input import load_input
from Day_06.part_1 import compute_redistribution
from utils.solve import test, solve

def solution(memory: List[int]) -> int:
    redistrubted_memory, history = compute_redistribution(memory)
    return len(history) - history[tuple(redistrubted_memory)]

if __name__ == "__main__":
    example_memory = load_input(Path(f"Day_{DAY:02d}/{EXAMPLE_INPUT_FILE_NAME}"))
    expected_answer = 4
    test(expected_answer, solution, example_memory)

    memory = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))
    solve(solution, memory)