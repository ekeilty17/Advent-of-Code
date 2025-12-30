from pathlib import Path
from typing import List

from Day_02.const import DAY, EXAMPLE_INPUT_FILE_NAME, INPUT_FILE_NAME
from Day_02.load_input import load_input
from utils.test import test

def is_safe(report: List[int]) -> bool:

    increasing_and_safe = True
    decreasing_and_safe = True
    for i in range(len(report)-1):
        diff = report[i+1] - report[i]
        if not (1 <= diff <= 3):
            increasing_and_safe = False
        if not (-3 <= diff <= -1):
            decreasing_and_safe = False

        if not (increasing_and_safe or decreasing_and_safe):
            return False
    
    return increasing_and_safe or decreasing_and_safe

def solution(reports: List[List[int]]) -> int:
    
    count = 0
    for report in reports:
        for i in range(len(report)):
            dampened_report = report[:i] + report[i+1:]
            if is_safe(dampened_report):
                count += 1
                break
    
    return count

if __name__ == "__main__":
    
    example_reports = load_input(Path(f"Day_{DAY:02d}/{EXAMPLE_INPUT_FILE_NAME}"))
    reports = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))

    expected_answer = 4
    test(expected_answer, solution, example_reports)

    total = solution(reports)
    print("Puzzle Answer:", total)