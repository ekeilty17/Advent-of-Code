from pathlib import Path
from typing import List

from Day_02.const import DAY, INPUT_FILE_NAME
from Day_02.const import EXAMPLE_INPUT_FILE_NAME_PART_2 as EXAMPLE_INPUT_FILE_NAME
from Day_02.load_input import load_input
from utils.solve import test, solve

def get_common_letters(string1: str, string2: str) -> str:
    common_string = ""
    for char1, char2 in zip(string1, string2):
        if char1 == char2:
            common_string += char1
    return common_string

def solution(IDs: List[str]) -> str | None:
    ID_length = len(IDs[0])

    for i in range(len(IDs)):
        for j in range(i+1, len(IDs)):
            common = get_common_letters(IDs[i], IDs[j])
            if len(common) == ID_length - 1:        # differ by exactly 1 character
                return common

if __name__ == "__main__":
    example_IDs = load_input(Path(f"Day_{DAY:02d}/{EXAMPLE_INPUT_FILE_NAME}"))
    expected_answer = "fgij"
    test(expected_answer, solution, example_IDs)

    IDs = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))
    solve(solution, IDs)