from pathlib import Path
from typing import List

from Day_19.const import DAY, EXAMPLE_INPUT_FILE_NAME, INPUT_FILE_NAME
from Day_19.load_input import load_input
from utils.test import test


def towel_combinations(patterns: List[str], target: str) -> bool:
    
    combinations = [0] * (len(target)+1)

    for n in range(1, len(target)+1):         # n == length of substring
        subtarget = target[:n]
        for pattern in patterns:
            if len(pattern) > n:
                continue
            if pattern == subtarget:
                combinations[n] += 1
            elif pattern == subtarget[-len(pattern):]:
                combinations[n] += combinations[n - len(pattern)]
    
    return combinations[-1]

def solution(patterns: List[str], target_towels: List[str]) -> int:
    
    patterns = list(sorted(patterns, key=len))
    count = 0
    for target in target_towels:
        target_count = towel_combinations(patterns, target)
        count += target_count
    return count

if __name__ == "__main__":
    
    example_patterns, example_target_towels = load_input(Path(f"Day_{DAY:02d}/{EXAMPLE_INPUT_FILE_NAME}"))
    patterns, target_towels = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))

    expected_answer = 16
    test(expected_answer, solution, example_patterns, example_target_towels)

    total = solution(patterns, target_towels)
    print("Puzzle Answer:", total)