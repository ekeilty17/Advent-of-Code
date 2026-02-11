from pathlib import Path
from typing import List, Tuple
import numpy as np

from Day_19.const import DAY, EXAMPLE_INPUT_FILE_NAME, INPUT_FILE_NAME
from Day_19.load_input import load_input
from utils.grid import get_positions_of_value
from utils.solve import test, solve

def is_in_bounds(shape: Tuple[int, int], i, j):
    return 0 <= i < shape[0] and 0 <= j < shape[1]

def simulate_packets(routing_diagram: List[List[str]]) -> Tuple[int, str]:
    routing_diagram = np.array(routing_diagram)
    
    start_col = get_positions_of_value(routing_diagram[0], "|")[0][0]
    start = (0, start_col)
    start_direction = (1, 0)
    state = (start, start_direction)

    sequence = []
    steps = 0
    while state:

        pos, direction = state
        steps += 1

        if routing_diagram[pos] not in ["|", "-", "+", " "]:
            sequence.append(routing_diagram[pos])
    
        left_direction = (-direction[1], -direction[0])
        right_direction = (direction[1], direction[0])
        forward = tuple([x+dx for x, dx in zip(pos, direction)])
        left = tuple([x+dx for x, dx in zip(pos, left_direction)])
        right = tuple([x+dx for x, dx in zip(pos, right_direction)])

        # Important to check `forward` direction first
        if is_in_bounds(routing_diagram.shape, *forward) and routing_diagram[forward] != " ":
            state = (forward, direction)

        # left/right don't matter. There should only be 1 of either
        elif is_in_bounds(routing_diagram.shape, *left) and routing_diagram[left] != " ":
            state = (left, left_direction)
        elif is_in_bounds(routing_diagram.shape, *right) and routing_diagram[right] != " ":
            state = (right, right_direction)
        else:
            state = None

    return "".join(sequence), steps

def solution(routing_diagram: List[List[str]]) -> str:
    sequence, _ = simulate_packets(routing_diagram)
    return sequence

if __name__ == "__main__":
    example_routing_diagram = load_input(Path(f"Day_{DAY:02d}/{EXAMPLE_INPUT_FILE_NAME}"))
    expected_answer = "ABCDEF"
    test(expected_answer, solution, example_routing_diagram)

    routing_diagram = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))
    solve(solution, routing_diagram)