from pathlib import Path
from typing import List
import numpy as np

from Day_06.const import DAY, EXAMPLE_INPUT_FILE_NAME, INPUT_FILE_NAME
from Day_06.load_input import load_input
from utils.test import test

def solution(worksheet: List[List[str]]) -> int:
    worksheet = [[x.strip() for x in row] for row in worksheet]
    
    operations = worksheet[-1]
    digit_rows = np.array(worksheet[:-1], dtype=int).T

    totals = []
    for digits, operation in zip(digit_rows, operations):
        if operation == "+":
            totals.append(np.sum(digits))
        elif operation == "*":
            totals.append(np.prod(digits))
        else:
            raise ValueError(f"Unsupported operation {operation}")
    
    return np.sum(totals)

if __name__ == "__main__":
    
    example_worksheet = load_input(Path(f"Day_{DAY:02d}/{EXAMPLE_INPUT_FILE_NAME}"))
    worksheet = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))

    expected_answer = 4277556
    test(expected_answer, solution, example_worksheet)

    total = solution(worksheet)
    print("Puzzle Answer:", total)