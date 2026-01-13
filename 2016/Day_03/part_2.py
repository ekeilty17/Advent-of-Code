from pathlib import Path
from typing import List

from Day_03.const import DAY, INPUT_FILE_NAME
from Day_03.load_input import load_input
from Day_03.part_1 import is_valid_triangle
from utils.solve import solve

def solution(rows: List[List[int]]) -> int:
    cols = [[rows[i][j] for i in range(len(rows))] for j in range(len(rows[0]))]
    
    triangles = []
    for col in cols:
        for k in range(0, len(col)-2, 3):
            triangles.append(tuple(col[k:k+3]))

    return sum(is_valid_triangle(a, b, c) for a, b, c in triangles)

if __name__ == "__main__":
    rows = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))
    solve(solution, rows)