from pathlib import Path
from typing import List

from Day_02.const import DAY, INPUT_FILE_NAME
from Day_02.const import EXAMPLE_INPUT_FILE_NAME_PART_1 as EXAMPLE_INPUT_FILE_NAME
from Day_02.load_input import load_input
from utils.solve import test, solve

def get_row_value(row: List[int]) -> int:
    return max(row) - min(row)

def solution(spreadsheet: List[List[int]]) -> int:
    return sum([get_row_value(row) for row in spreadsheet])

if __name__ == "__main__":
    example_spreadsheet = load_input(Path(f"Day_{DAY:02d}/{EXAMPLE_INPUT_FILE_NAME}"))
    expected_answer = 18
    test(expected_answer, solution, example_spreadsheet)

    spreadsheet = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))
    solve(solution, spreadsheet)