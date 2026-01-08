from pathlib import Path
from typing import List, Dict, Optional

from Day_11.const import DAY, INPUT_FILE_NAME
from Day_11.const import EXAMPLE_INPUT_FILE_NAME_PART_1 as EXAMPLE_INPUT_FILE_NAME
from Day_11.load_input import load_input
from Day_11.graph import Graph
from utils.solve import test, solve

def solution(devices: Dict[str, List[str]], start: str, end:str) -> int:
    G = Graph.from_adjacency_list(devices)
    paths = G.all_paths(start, end)
    return len(paths)

if __name__ == "__main__":
    start_device = "you"
    end_device = "out"

    example_devices = load_input(Path(f"Day_{DAY}/{EXAMPLE_INPUT_FILE_NAME}"))
    expected_answer = 5
    test(expected_answer, solution, example_devices, start_device, end_device)

    devices = load_input(Path(f"Day_{DAY}/{INPUT_FILE_NAME}"))
    solve(solution, devices, start_device, end_device)