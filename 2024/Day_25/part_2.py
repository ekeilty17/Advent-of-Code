from pathlib import Path
from typing import List

from Day_25.const import DAY, EXAMPLE_INPUT_FILE_NAME, INPUT_FILE_NAME
from Day_25.load_input import load_input
from utils.test import test

def solution() -> int:
    pass

if __name__ == "__main__":
    
    _ = load_input(Path(f"Day_{DAY:02d}/{EXAMPLE_INPUT_FILE_NAME}"))
    _ = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))

    expected_answer = None
    test(expected_answer, solution)

    total = solution()
    print("Puzzle Answer:", total)