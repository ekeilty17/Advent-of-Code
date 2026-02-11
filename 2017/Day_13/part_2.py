from pathlib import Path
from typing import Dict

from Day_13.const import DAY, EXAMPLE_INPUT_FILE_NAME, INPUT_FILE_NAME
from Day_13.load_input import load_input
from utils.solve import test, solve

# much faster than the part_1.py implementation
def is_caught_at_picosecond(picosecond: int, scan_range: int) -> bool:
    return picosecond % (2*(scan_range - 1)) == 0

def is_caught(firewall: Dict[int, int], delay: int) -> bool:
    for layer, scan_range in firewall.items():
        picosecond = delay + layer
        if is_caught_at_picosecond(picosecond, scan_range):
            return False
    
    return True

def brute_force(firewall: Dict[int, int]) -> int:
    delay = 0
    while True:
        if is_caught(firewall, delay):
            return delay
        delay += 1

def solution(firewall: Dict[int, int]) -> int:
    return brute_force(firewall)
    

if __name__ == "__main__":
    example_firewall = load_input(Path(f"Day_{DAY:02d}/{EXAMPLE_INPUT_FILE_NAME}"))
    expected_answer = 10
    test(expected_answer, solution, example_firewall)

    firewall = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))
    solve(solution, firewall)