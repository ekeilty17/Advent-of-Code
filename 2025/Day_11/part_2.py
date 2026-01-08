from pathlib import Path
from typing import List, Dict, Optional, Set
from itertools import combinations
import math

from Day_11.const import DAY, INPUT_FILE_NAME
from Day_11.const import EXAMPLE_INPUT_FILE_NAME_PART_2 as EXAMPLE_INPUT_FILE_NAME
from Day_11.load_input import load_input
from Day_11.visualize_graph import visualize_graph
from Day_11.graph import Graph
from utils.solve import test, solve

def solution(devices: Dict[str, List[str]], start: str, intermediates: List[str], end:str) -> int:
    G = Graph.from_adjacency_list(devices)
    
    topological_order = G.topological_sort()
    sorted_intermediaries = list(sorted(intermediates, key=topological_order.index))
    
    path_counts = []

    sorted_nodes = [start] + sorted_intermediaries + [end]
    for u, v in zip(sorted_nodes[:-1], sorted_nodes[1:]):
        paths = G.all_paths_dag(u, v)
        path_counts.append(len(paths))
    
    return math.prod(path_counts)

if __name__ == "__main__":
    start_device = "svr"
    intermediate_devices = ["dac", "fft"]
    end_device = "out"

    example_devices = load_input(Path(f"Day_{DAY}/{EXAMPLE_INPUT_FILE_NAME}"))
    expected_answer = 2
    test(expected_answer, solution, example_devices, start_device, intermediate_devices, end_device)
    
    devices = load_input(Path(f"Day_{DAY}/{INPUT_FILE_NAME}"))
    # visualize_graph(devices, start_device, intermediate_devices, end_device)
    solve(solution, devices, start_device, intermediate_devices, end_device)