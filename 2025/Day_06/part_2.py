from pathlib import Path
from typing import List
import numpy as np

from Day_06.const import DAY, EXAMPLE_INPUT_FILE_NAME, INPUT_FILE_NAME
from Day_06.load_input import load_input
from utils.test import test

def solution(worksheet: List[List[str]]) -> int:
    operations = worksheet[-1]
    operations = [x.strip() for x in operations]
    
    data = np.array(worksheet[:-1])
    digit_rows = []
    for col in data.T:
        expanded_col = np.array([[char for char in num] for num in col])
        corrected_digits = [''.join(col).replace(' ', '') for col in expanded_col.T]
        digit_rows.append([int(x) for x in corrected_digits])

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

    expected_answer = 3263827
    test(expected_answer, solution, example_worksheet)

    total = solution(worksheet)
    print("Puzzle Answer:", total)