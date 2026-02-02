from pathlib import Path
from typing import Dict, Set

from Day_12.const import DAY, EXAMPLE_INPUT_FILE_NAME, INPUT_FILE_NAME
from Day_12.load_input import load_input
from utils.solve import test, solve

def get_connected_component(adj: Dict[int, Set[int]], start: int) -> Set[int]:
    connected = set([])
    stack = [start]

    while stack:
        node = stack.pop()

        if node in connected:
            continue
        connected.add(node)

        for neighbor in adj[node]:
            stack.append(neighbor)
    
    return connected

def solution(connections: Dict[int, Set[int]], program_id: int) -> int:
    group = get_connected_component(connections, program_id)
    return len(group)

if __name__ == "__main__":
    program_id = 0    

    example_connections = load_input(Path(f"Day_{DAY:02d}/{EXAMPLE_INPUT_FILE_NAME}"))
    expected_answer = 6
    test(expected_answer, solution, example_connections, program_id)

    connections = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))
    solve(solution, connections, program_id)