from pathlib import Path
import numpy as np
from numpy.typing import NDArray

from Day_04.const import DAY, EXAMPLE_INPUT_FILE_NAME, INPUT_FILE_NAME
from Day_04.load_input import load_input
from utils.solve import test, solve

def get_unique_orientations(pattern):
    pattern = pattern.copy()

    orientations = [pattern.copy()]
    for _ in range(3):
        pattern = np.rot90(pattern)
        orientations.extend([
            pattern.copy(),
            np.flip(pattern.copy(), axis=0),
            np.flip(pattern.copy(), axis=1)
        ])

    unique_orientations = {}
    for orientation in orientations:
        key = np.array2string(orientation)
        unique_orientations[key] = orientation
    
    return list(unique_orientations.values())

def convolution_check(crossword: NDArray[str], pattern: NDArray[str]) -> int:
    M, N = crossword.shape
    m, n = pattern.shape
    
    count = 0
    for i in range(M - m + 1):
        for j in range(N - n + 1):
            sub_array = crossword[i:i+n, j:j+m].copy()
            sub_array[np.where(pattern == '.')] = '.'
            if np.array_equal(sub_array, pattern):
                count += 1
    return count

def solution(crossword: NDArray[str], pattern: NDArray[str]) -> int:
    count = 0
    for oriented_pattern in get_unique_orientations(pattern):
        count += convolution_check(crossword, oriented_pattern)
    
    return count

if __name__ == "__main__":
    pattern = np.array([
        ['M', '.', 'S'],
        ['.', 'A', '.'],
        ['M', '.', 'S'],
    ])

    example_crossword = load_input(Path(f"Day_{DAY:02d}/{EXAMPLE_INPUT_FILE_NAME}"))
    expected_answer = 9
    test(expected_answer, solution, example_crossword, pattern)

    crossword = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))
    solve(solution, crossword, pattern)