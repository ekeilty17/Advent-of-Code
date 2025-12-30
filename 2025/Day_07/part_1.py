from pathlib import Path
from typing import List

from Day_07.const import DAY, EXAMPLE_INPUT_FILE_NAME, INPUT_FILE_NAME
from Day_07.load_input import load_input
from utils.test import test

def solution(tachyon_manifold: List[List[str]]) -> int:

    number_of_splits = 0
    for i, row in enumerate(tachyon_manifold[:-1]):
        for j, cell in enumerate(row):
            if cell == "S" or cell == "|":
                if tachyon_manifold[i+1][j] == "^":
                    tachyon_manifold[i+1][j-1] = "|"
                    tachyon_manifold[i+1][j+1] = "|"
                    number_of_splits += 1
                else:
                    tachyon_manifold[i+1][j] = "|"
    
    return number_of_splits

if __name__ == "__main__":
    
    example_tachyon_manifold = load_input(Path(f"Day_{DAY:02d}/{EXAMPLE_INPUT_FILE_NAME}"))
    tachyon_manifold = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))

    expected_answer = 21
    test(expected_answer, solution, example_tachyon_manifold)

    total = solution(tachyon_manifold)
    print("Puzzle Answer:", total)