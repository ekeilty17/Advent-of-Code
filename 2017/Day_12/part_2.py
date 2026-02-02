from pathlib import Path
from typing import Dict, Set

from Day_12.const import DAY, EXAMPLE_INPUT_FILE_NAME, INPUT_FILE_NAME
from Day_12.load_input import load_input
from Day_12.part_1 import get_connected_component
from utils.solve import test, solve

def solution(connections: Dict[int, Set[int]]) -> int:
    groups = []
    for program_id in connections:
        if any(program_id in group for group in groups):
            continue
        group = get_connected_component(connections, program_id)
        groups.append(group)
    
    return len(groups)

if __name__ == "__main__":
    example_connections = load_input(Path(f"Day_{DAY:02d}/{EXAMPLE_INPUT_FILE_NAME}"))
    expected_answer = 2
    test(expected_answer, solution, example_connections)

    connections = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))
    solve(solution, connections)