from pathlib import Path
from typing import List, Tuple

from Day_20.const import DAY, EXAMPLE_INPUT_FILE_NAME, INPUT_FILE_NAME
from Day_20.load_input import load_input
from Day_20.interval_set import InternvalSet
from utils.solve import test, solve

def solution(blacklist: List[Tuple[int, int]], IP_range: int) -> int:
    I = InternvalSet()

    for lower, upper in blacklist:
        I.add(lower, upper+1)
    
    total_IPs = sum(IP_range)+1
    total_blacklisted = sum([b-a for a, b in I])
    return total_IPs - total_blacklisted

if __name__ == "__main__":
    example_blacklist = load_input(Path(f"Day_{DAY:02d}/{EXAMPLE_INPUT_FILE_NAME}"))
    example_IP_range = (0, 9)       # inclusive
    expected_answer = 2
    test(expected_answer, solution, example_blacklist, example_IP_range)

    IP_range = (0, 4294967295)       # inclusive
    blacklist = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))
    solve(solution, blacklist, IP_range)