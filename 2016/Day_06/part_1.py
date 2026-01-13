from pathlib import Path
from typing import List
from collections import Counter

from Day_06.const import DAY, EXAMPLE_INPUT_FILE_NAME, INPUT_FILE_NAME
from Day_06.load_input import load_input
from utils.solve import test, solve

def solution(rows: List[str]) -> int:
    cols = [[rows[i][j] for i in range(len(rows))] for j in range(len(rows[0]))]
    return "".join([Counter(col).most_common()[0][0] for col in cols])

if __name__ == "__main__":
    example_rows = load_input(Path(f"Day_{DAY:02d}/{EXAMPLE_INPUT_FILE_NAME}"))
    expected_answer = "easter"
    test(expected_answer, solution, example_rows)

    rows = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))
    solve(solution, rows)