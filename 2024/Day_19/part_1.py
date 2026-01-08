from pathlib import Path
from typing import List, Optional

from Day_19.const import DAY, EXAMPLE_INPUT_FILE_NAME, INPUT_FILE_NAME
from Day_19.load_input import load_input
from utils.solve import test, solve

def is_towel_possible(patterns: List[str], target: str, subdesign: Optional[str]=None) -> bool:
    if target == "":
        return False
    
    if subdesign is None:
        subdesign = ""

    if subdesign == target:
        return True
    
    if len(subdesign) > len(target):
        return False
    if subdesign != target[:len(subdesign)]:
        return False
    
    for pattern in patterns:
        nxt = subdesign + pattern
        if is_towel_possible(patterns, target, nxt):
            return True
    
    return False

def solution(patterns: List[str], target_towels: List[str]) -> int:
    count = 0
    for target in target_towels:
        if is_towel_possible(patterns, target):
            count += 1
    return count

if __name__ == "__main__":
    example_patterns, example_target_towels = load_input(Path(f"Day_{DAY:02d}/{EXAMPLE_INPUT_FILE_NAME}"))
    expected_answer = 6
    test(expected_answer, solution, example_patterns, example_target_towels)

    patterns, target_towels = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))
    solve(solution, patterns, target_towels)