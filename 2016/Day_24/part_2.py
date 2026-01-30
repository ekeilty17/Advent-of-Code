from pathlib import Path
from typing import List
from itertools import permutations

from Day_24.const import DAY, EXAMPLE_INPUT_FILE_NAME, INPUT_FILE_NAME
from Day_24.load_input import load_input
from Day_24.part_1 import initialize, compute_distance_graph, compute_path_weight
from utils.solve import test, solve

def solution(map: List[List[str]]) -> int:
    walls, start, targets = initialize(map)
    adj = compute_distance_graph(walls, start, targets)

    # Finding the minimum Hamiltonian Cycle
    min_cycle_weight = float("inf")
    min_cycle = None
    for path in permutations(targets):
        cycle_weight = adj[start][path[0]] + compute_path_weight(path, adj) + adj[path[-1]][start]
        if cycle_weight < min_cycle_weight:
            min_cycle_weight = cycle_weight
            min_cycle = [start] + list(path)
    
    # print(min_cycle)
    return min_cycle_weight

if __name__ == "__main__":
    example_map = load_input(Path(f"Day_{DAY:02d}/{EXAMPLE_INPUT_FILE_NAME}"))
    expected_answer = 14
    test(expected_answer, solution, example_map)

    map = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))
    solve(solution, map)