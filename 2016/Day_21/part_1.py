from pathlib import Path
from typing import Dict, Any

from Day_21.const import DAY, EXAMPLE_INPUT_FILE_NAME, INPUT_FILE_NAME
from Day_21.load_input import load_input
from Day_21.operations import OPERATIONS
from utils.solve import test, solve

def solution(password: str, operations: Dict[str, Any]) -> str:
    password = list(password)

    for operation in operations:
        password = OPERATIONS[operation["operation"]](password, **operation)

    return "".join(password)

if __name__ == "__main__":
    example_operations = load_input(Path(f"Day_{DAY:02d}/{EXAMPLE_INPUT_FILE_NAME}"))
    example_password = "abcde"
    expected_answer = "decab"
    test(expected_answer, solution, example_password, example_operations)

    operations = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))
    password = "abcdefgh"
    solve(solution, password, operations)