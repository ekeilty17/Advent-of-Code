from pathlib import Path
from typing import List

from Day_08.const import DAY, EXAMPLE_INPUT_FILE_NAME, INPUT_FILE_NAME
from Day_08.load_input import load_input
from utils.solve import test, solve

def decode(string: str) -> int:
    return string[1:-1].encode().decode("unicode_escape")

def solution(strings: List[str]) -> int:
    total = 0
    for string in strings:
        decoded_string = decode(string)
        total += len(string) - len(decoded_string)
    
    return total

if __name__ == "__main__":
    example_strings = load_input(Path(f"Day_{DAY:02d}/{EXAMPLE_INPUT_FILE_NAME}"))
    expected_answer = 12
    test(expected_answer, solution, example_strings)

    strings = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))
    solve(solution, strings)