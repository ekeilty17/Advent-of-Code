from pathlib import Path
from typing import List

from Day_09.const import DAY, INPUT_FILE_NAME
from Day_09.load_input import load_input
from utils.solve import test, solve

def compute_score(stream: str) -> int:
    
    score = 0

    group_nesting_depth = 0
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
            i += 1
            continue
        
        # We are in non-garbage
        if char == "<":
            is_garbage = True
        elif char == "{":
            group_nesting_depth += 1
        elif char == "}":
            score += group_nesting_depth
            group_nesting_depth -= 1
        
        i += 1

    return score

def solution(stream: str) -> int:
    return compute_score(stream)

if __name__ == "__main__":
    examples = [
        (r"{}", 1),
        (r"{{{}}}", 6),
        (r"{{},{}}", 5),
        (r"{{{},{},{{}}}}", 16),
        (r"{<a>,<a>,<a>,<a>}", 1),
        (r"{{<ab>},{<ab>},{<ab>},{<ab>}}", 9),
        (r"{{<!!>},{<!!>},{<!!>},{<!!>}}", 9),
        (r"{{<a!>},{<a!>},{<a!>},{<ab>}}", 3),
    ]
    for example_stream, expected_answer in examples:
        test(expected_answer, solution, example_stream)

    stream = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))
    solve(solution, stream)