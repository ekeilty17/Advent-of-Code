from pathlib import Path
from typing import List

from Day_18.const import DAY, SMALL_EXAMPLE_INPUT_FILE_NAME, EXAMPLE_INPUT_FILE_NAME, INPUT_FILE_NAME
from Day_18.load_input import load_input
from utils.solve import test, solve

def is_trap(left: bool, center: bool, right: bool) -> bool:
    return (left or right) and (not left or not right)

def is_safe(left: bool, center: bool, right: bool) -> bool:
    return (not left or right) and (left or not right)

def update(safe_tiles: List[str]) -> List[str]:
    padded_safe_tiles = [True, *safe_tiles, True]
    return [is_safe(*padded_safe_tiles[i:i+3]) for i in range(len(padded_safe_tiles)-2)]

def solution(tiles: str, num_rows: int) -> int:
    safe_tiles = [t == "." for t in tiles]
    num_safe_tiles = sum(safe_tiles)
    # print("".join(["." if t else "^" for t in safe_tiles]))

    for _ in range(num_rows-1):
        safe_tiles = update(safe_tiles)
        num_safe_tiles += sum(safe_tiles)
        # print("".join(["." if t else "^" for t in safe_tiles]))

    return num_safe_tiles

if __name__ == "__main__":
    small_example_tiles = load_input(Path(f"Day_{DAY:02d}/{SMALL_EXAMPLE_INPUT_FILE_NAME}"))
    small_example_num_rows = 3
    small_expected_answer = 6
    test(small_expected_answer, solution, small_example_tiles, small_example_num_rows)

    example_tiles = load_input(Path(f"Day_{DAY:02d}/{EXAMPLE_INPUT_FILE_NAME}"))
    example_num_rows = 10
    expected_answer = 38
    test(expected_answer, solution, example_tiles, example_num_rows)

    tiles = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))
    num_rows = 40
    solve(solution, tiles, num_rows)