from pathlib import Path
import numpy as np
from numpy.typing import NDArray

from Day_04.const import DAY, EXAMPLE_INPUT_FILE_NAME, INPUT_FILE_NAME
from Day_04.load_input import load_input
from utils.solve import test, solve

def check_rows(crossword: NDArray[str], pattern: str) -> int:
    reverse_pattern = pattern[::-1]
    count = 0
    for i, row in enumerate(crossword):
        for j in range(len(row) - len(pattern)+1):
            subrow = "".join(row[j:j+len(pattern)])
            if subrow == pattern or subrow == reverse_pattern:
                count += 1
    return count

def check_columns(crossword: NDArray[str], pattern: str) -> int:
    return check_rows(crossword.T, pattern)

def check_main_diagonals(crossword: NDArray[str], pattern: str) -> int:
    reverse_pattern = pattern[::-1]
    count = 0

    m, n = crossword.shape
    for k in range(-m + 1, n):
        diag = crossword.diagonal(offset=k)
        for j in range(len(diag) - len(pattern)+1):
            subrow = "".join(diag[j:j+len(pattern)])
            if subrow == pattern or subrow == reverse_pattern:
                count += 1
    return count

def check_anti_diagonals(crossword: NDArray[str], pattern: str) -> int:
    return check_main_diagonals(np.fliplr(crossword), pattern)

def solution(crossword: NDArray[str], pattern: str) -> int:

    count = 0
    count += check_rows(crossword, pattern)
    count += check_columns(crossword, pattern)
    count += check_main_diagonals(crossword, pattern)
    count += check_anti_diagonals(crossword, pattern)
    return count

if __name__ == "__main__":
    pattern = "XMAS"

    example_crossword = load_input(Path(f"Day_{DAY:02d}/{EXAMPLE_INPUT_FILE_NAME}"))
    expected_answer = 18
    test(expected_answer, solution, example_crossword, pattern)

    crossword = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))
    solve(solution, crossword, pattern)