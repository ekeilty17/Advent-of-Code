from pathlib import Path
from typing import List, Tuple

from Day_07.const import DAY, INPUT_FILE_NAME
from Day_07.const import EXAMPLE_INPUT_FILE_NAME_PART_2 as EXAMPLE_INPUT_FILE_NAME
from Day_07.load_input import load_input
from utils.solve import test, solve

def get_all_aba(string: str) -> bool:
    aba = []
    for i in range(len(string)-2):
        a, b, c = string[i:i+3]
        if a == b == c:
            continue
        if a == c:
            aba.append(string[i:i+3])
    return aba

def is_ip_support_ssl(IP: Tuple[str, str, str]) -> bool:
    supernet, hypernet = IP     # supernet == outside brackets, hypernet == inside brackets
    
    supernet_aba = set([aba for s in supernet for aba in get_all_aba(s)])
    hypernet_aba = set([aba for s in hypernet for aba in get_all_aba(s)])

    supernet_bab = set([b + a + b for a, b, _ in supernet_aba])
    return bool(supernet_bab & hypernet_aba)

def solution(IPs: List[Tuple[str, str, str]]) -> int:
    return sum(is_ip_support_ssl(IP) for IP in IPs)

if __name__ == "__main__":
    example_IPs = load_input(Path(f"Day_{DAY:02d}/{EXAMPLE_INPUT_FILE_NAME}"))
    expected_answer = 3
    test(expected_answer, solution, example_IPs)

    IPs = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))
    solve(solution, IPs)