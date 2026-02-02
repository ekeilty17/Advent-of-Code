from pathlib import Path
from typing import List, Tuple

from Day_11.const import DAY, INPUT_FILE_NAME
from Day_11.load_input import load_input
from utils.solve import test, solve

def get_hex_distance(x: int, y: int) -> int:
    x, y = abs(x), abs(y)
    return x + max(y - x, 0) // 2

def update_hex_position(x: int, y:int, direction:str) -> Tuple[int, int]:
    displacement_map = {
        "n": (0, 2),
        "ne": (1, 1),
        "se": (1, -1),
        "s": (0, -2),
        "sw": (-1, -1),
        "nw": (-1, 1)
    }
    dx, dy = displacement_map[direction]
    x += dx
    y += dy
    
    return x, y

def solution(path: List[str]) -> int:

    x = y = 0
    for direction in path:
        x, y = update_hex_position(x, y, direction)

    return get_hex_distance(x, y)

if __name__ == "__main__":
    examples = [
        (["ne" , "ne", "ne"], 3),
        (["ne", "ne", "sw", "sw"], 0),
        (["ne", "ne", "s", "s"], 2),
        (["se", "sw", "se", "sw", "sw"], 3)
    ]
    for example_path, expected_answer in examples:
        test(expected_answer, solution, example_path)

    path = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))
    solve(solution, path)