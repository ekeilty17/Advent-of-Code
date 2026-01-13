from pathlib import Path
from typing import List, Tuple

from Day_07.const import DAY, INPUT_FILE_NAME
from Day_07.const import EXAMPLE_INPUT_FILE_NAME_PART_1 as EXAMPLE_INPUT_FILE_NAME
from Day_07.load_input import load_input
from utils.solve import test, solve

def is_abba(string: str) -> bool:
    for i in range(len(string)-3):
        a, b, c, d = string[i:i+4]
        if a == b == c == d:
            return False
        if a == d and b == c:
            return True
    return False

def is_ip_support_tls(IP: Tuple[str, str, str]) -> bool:
    supernet, hypernet = IP         # supernet == outside brackets, hypernet == inside brackets
    if any(is_abba(s) for s in hypernet):
        return False
    return any(is_abba(s) for s in supernet)

def solution(IPs: List[Tuple[str, str, str]]) -> int:
    return sum(is_ip_support_tls(IP) for IP in IPs)

if __name__ == "__main__":
    example_IPs = load_input(Path(f"Day_{DAY:02d}/{EXAMPLE_INPUT_FILE_NAME}"))
    expected_answer = 2
    test(expected_answer, solution, example_IPs)

    IPs = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))
    solve(solution, IPs)