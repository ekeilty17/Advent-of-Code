from pathlib import Path
from typing import List, Tuple

from Day_11.const import DAY, INPUT_FILE_NAME
from Day_11.load_input import load_input
from Day_11.part_1 import get_hex_distance, update_hex_position
from utils.solve import test, solve

def solution(path: List[str]) -> int:
    max_distance = 0

    x = y = 0
    for direction in path:
        x, y = update_hex_position(x, y, direction)
        max_distance = max(max_distance, get_hex_distance(x, y))

    return max_distance

if __name__ == "__main__":
    path = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))
    solve(solution, path)