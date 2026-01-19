from pathlib import Path
from typing import List, Tuple

from Day_20.const import DAY, EXAMPLE_INPUT_FILE_NAME, INPUT_FILE_NAME
from Day_20.load_input import load_input
from Day_20.interval_set import InternvalSet
from utils.solve import test, solve

def solution(blacklist: List[Tuple[int, int]]) -> int:
    I = InternvalSet()

    for lower, upper in blacklist:
        I.add(lower, upper+1)
    
    lowest_internval = min(I.intervals)
    return lowest_internval[1]

if __name__ == "__main__":
    example_blacklist = load_input(Path(f"Day_{DAY:02d}/{EXAMPLE_INPUT_FILE_NAME}"))
    expected_answer = 3
    test(expected_answer, solution, example_blacklist)

    blacklist = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))
    solve(solution, blacklist)