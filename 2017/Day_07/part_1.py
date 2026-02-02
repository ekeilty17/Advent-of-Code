from pathlib import Path
from typing import List, Tuple, Dict

from Day_07.const import DAY, EXAMPLE_INPUT_FILE_NAME, INPUT_FILE_NAME
from Day_07.load_input import load_input
from utils.solve import test, solve

def compute_parents(children_by_program:  Dict[str, List[str]]) -> Dict[str, List[str]]:
    parent_by_program = {}
    for parent, children in children_by_program.items():
        for child in children:
            parent_by_program[child] = parent
    
    return parent_by_program

def get_roots(children_by_program: Dict[str, List[str]]) -> List[str]:
    parent_by_program = compute_parents(children_by_program)
    return list(set(children_by_program) - set(parent_by_program))

def solution(children_by_program: Dict[str, List[str]]) -> str:
    return get_roots(children_by_program)[0]

if __name__ == "__main__":
    _, example_children_by_program = load_input(Path(f"Day_{DAY:02d}/{EXAMPLE_INPUT_FILE_NAME}"))
    expected_answer = "tknk"
    test(expected_answer, solution, example_children_by_program)

    _, children_by_program = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))
    solve(solution, children_by_program)