from pathlib import Path
from typing import Dict

from Day_13.const import DAY, EXAMPLE_INPUT_FILE_NAME, INPUT_FILE_NAME
from Day_13.load_input import load_input
from utils.solve import test, solve

def get_scanner_position(picosecond: int, scan_range: int) -> int:
    scanner_position = picosecond % (scan_range-1)

    num_cycles = picosecond // (scan_range-1)
    if num_cycles % 2:
        scanner_position = (scan_range-1) - scanner_position
    
    return scanner_position

# See part_2.py for an alternative way of writing this function
def is_caught_at_picosecond(picosecond: int, scan_range: int) -> bool:
    scanner_position = get_scanner_position(picosecond, scan_range)
    return scanner_position == 0

def is_caught_at_picosecond_alt(picosecond: int, scan_range: int) -> bool:
    return picosecond % (2*(scan_range - 1)) == 0

def solution(firewall: Dict[int, int]) -> int:
    
    delay = 0
    severity = 0
    for layer, scan_range in firewall.items():
        picosecond = delay + layer
        if is_caught_at_picosecond(picosecond, scan_range):
            severity += picosecond * scan_range
    
    return severity

if __name__ == "__main__":
    example_firewall = load_input(Path(f"Day_{DAY:02d}/{EXAMPLE_INPUT_FILE_NAME}"))
    expected_answer = 24
    test(expected_answer, solution, example_firewall)

    firewall = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))
    solve(solution, firewall)