from pathlib import Path
from typing import List

from Day_19.const import DAY, EXAMPLE_INPUT_FILE_NAME, INPUT_FILE_NAME
from Day_19.load_input import load_input
from Day_19.part_1 import simulate_packets
from utils.solve import test, solve

def solution(routing_diagram: List[List[str]]) -> int:
    _, steps = simulate_packets(routing_diagram)
    return steps

if __name__ == "__main__":
    example_routing_diagram = load_input(Path(f"Day_{DAY:02d}/{EXAMPLE_INPUT_FILE_NAME}"))
    expected_answer = 38
    test(expected_answer, solution, example_routing_diagram)

    routing_diagram = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))
    solve(solution, routing_diagram)