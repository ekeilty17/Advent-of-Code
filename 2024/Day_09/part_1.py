from pathlib import Path
from typing import List

from Day_09.const import DAY, EXAMPLE_INPUT_FILE_NAME, INPUT_FILE_NAME
from Day_09.load_input import load_input
from utils.solve import test, solve

def checksum(disk_map: List[int | None]):
    return sum([0 if n is None else i*n for i, n in enumerate(disk_map)])

def solution(disk_map: List[int | None]) -> int:

    l, r = 0, len(disk_map)-1
    while l < r:
        if disk_map[r] is None:
            r -= 1
            continue
        if disk_map[l] is not None:
            l += 1
            continue
        disk_map[l], disk_map[r] = disk_map[r], disk_map[l]
        l += 1
        r -= 1

    return checksum(disk_map)

if __name__ == "__main__":
    example_disk_map, _, _ = load_input(Path(f"Day_{DAY:02d}/{EXAMPLE_INPUT_FILE_NAME}"))
    expected_answer = 1928
    test(expected_answer, solution, example_disk_map)

    disk_map, _, _ = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))
    solve(solution, disk_map)