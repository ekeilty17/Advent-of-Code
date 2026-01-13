from pathlib import Path
from typing import List

from Day_03.const import DAY, INPUT_FILE_NAME
from Day_03.load_input import load_input
from utils.solve import solve

def is_valid_triangle(a: int, b: int, c: int) -> bool:
    return (a+b > c) and (b+c > a) and (c+a > b)

def solution(rows: List[List[int]]) -> int:
    triangles = [tuple(row) for row in rows]
    return sum(is_valid_triangle(a, b, c) for a, b, c in triangles)

if __name__ == "__main__":
    rows = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))
    solve(solution, rows)