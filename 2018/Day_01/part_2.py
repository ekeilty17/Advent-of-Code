from pathlib import Path
from typing import List

from Day_01.const import DAY, INPUT_FILE_NAME
from Day_01.load_input import load_input
from utils.solve import test, solve

def solution(start_frequency: int, frequency_changes: List[int]) -> int:
    repeats = set([start_frequency])

    frequency = start_frequency
    while True:
        for df in frequency_changes:
            frequency += df
            if frequency in repeats:
                return frequency
            repeats.add(frequency)

if __name__ == "__main__":
    start_frequency = 0

    examples = [
        ([1, -2, 3, 1], 2),
        ([1, -1], 0),
        ([3, 3, 4, -2, -4], 10),
        ([-6, 3, 8, 5, -6], 5),
        ([7, 7, -2, -7, -4], 14)
    ]
    for example_frequency_changes, expected_answer in examples:
        test(expected_answer, solution, start_frequency, example_frequency_changes)

    frequency_changes = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))
    solve(solution, start_frequency, frequency_changes)