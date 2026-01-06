from pathlib import Path
from typing import List
import json

from Day_08.const import DAY, EXAMPLE_INPUT_FILE_NAME, INPUT_FILE_NAME
from Day_08.load_input import load_input
from utils.test import test

def escape_using_json(string: str) -> str:
    return json.dumps(string)

def escape(string: str) -> str:
    return '"' + string.replace('\\', '\\\\').replace('"', '\\"') + '"'

def solution(strings: List[str]) -> int:
    total = 0
    for string in strings:
        escaped_string = escape(string)
        total += len(escaped_string) - len(string)
    
    return total

if __name__ == "__main__":
    
    example_strings = load_input(Path(f"Day_{DAY:02d}/{EXAMPLE_INPUT_FILE_NAME}"))
    strings = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))

    expected_answer = 19
    test(expected_answer, solution, example_strings)

    total = solution(strings)
    print("Puzzle Answer:", total)