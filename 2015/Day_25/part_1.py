from pathlib import Path
from typing import List

from Day_25.const import DAY, INPUT_FILE_NAME
from Day_25.load_input import load_input
from utils.solve import test, solve

def get_triangle_number_index(row: int, col: int):
    height = row + col - 1
    T = height * (height + 1) // 2
    return T - (height - col)

def mod_exp(base: int, exponent: int, modulus: int, initial: int=1) -> int:
    if modulus == 1:
        return 0
    
    result = initial
    for _ in range(exponent):
        result = (result * base) % modulus
    return result

def solution(initial_code: int, multiplier: int, modulus: int, manual_row: int, manual_col: int) -> int:

    N = get_triangle_number_index(manual_row, manual_col)
    result = mod_exp(multiplier, N-1, modulus, initial_code)
    return result

if __name__ == "__main__":
    initial_code = 20151125
    multiplier = 252533
    modulus = 33554393

    expected_manual_row, expected_manual_col = 6, 6
    expected_answer = 27995004
    test(expected_answer, solution, initial_code, multiplier, modulus, expected_manual_row, expected_manual_col)

    manual_row, manual_col = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))
    solve(solution, initial_code, multiplier, modulus, manual_row, manual_col)