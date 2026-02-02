from pathlib import Path
from typing import List

from Day_09.const import DAY, INPUT_FILE_NAME
from Day_09.load_input import load_input
from utils.solve import test, solve

def count_garbage(stream: str) -> int:

    total_garbage = 0
    is_garbage = False

    i = 0
    while i < len(stream):
        char = stream[i]
        
        # ! = ignore next character
        if char == "!":
            i += 2
            continue
        
        # characters during garbage time are ignored, except ">"
        if is_garbage:
            if char == ">":
                is_garbage = False
            else:
                total_garbage += 1
            i += 1
            continue
        
        # We are in non-garbage
        if char == "<":
            is_garbage = True
        
        i += 1

    return total_garbage

def solution(stream: str) -> int:
    return count_garbage(stream)

if __name__ == "__main__":
    examples = [
        (r"<>", 0),
        (r"<random characters>", 17),
        (r"<<<<>", 3),
        (r"<{!>}>", 2),
        (r"<!!>", 0),
        (r"<!!!>>", 0),
        (r'<{o"i!a,<{i<a>', 10),
    ]
    for example_stream, expected_answer in examples:
        test(expected_answer, solution, example_stream)

    stream = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))
    solve(solution, stream)