from pathlib import Path
from typing import List, Tuple, Dict
from itertools import combinations, permutations
import heapq
import numpy as np
from numpy.typing import NDArray

from Day_24.const import DAY, EXAMPLE_INPUT_FILE_NAME, INPUT_FILE_NAME
from Day_24.load_input import load_input
from utils.grid import get_orthogonal_neighbor_indices
from utils.solve import test, solve

def initialize(map: List[List[str]]) -> Tuple[NDArray[np.bool_], Tuple[int, int], List[Tuple[int, int]]]:
    map = np.array(map)

    targets = []
    for index, value in np.ndenumerate(map):
        try:
            value = int(value)
            map[index] = "."
            if value == 0:
                start = index
            else:
                targets.append((value, index))
        except:
            pass
    
    walls = (map == "#")
    targets = [index for _, index in sorted(targets)]
    return walls, start, targets

def a_star(walls: NDArray[np.bool_], start: Tuple[int, int], end: Tuple[int, int]) -> int | None:
    
    def heuristic(pos: Tuple[int, int], end: Tuple[int, int]) -> int:
        x1, y1 = pos
        x2, y2 = end
        return abs(x2 - x1) + abs(y2 - y1)
    
    visited = {}
    frontier = []
    heapq.heappush(frontier, (heuristic(start, end), 0, start))

    while frontier:

        _, depth, pos = heapq.heappop(frontier)
        
        if pos == end:
            return depth
        
        if visited.get(pos, float("inf")) <= depth:
            continue
        visited[pos] = depth

        for neighbor_index in get_orthogonal_neighbor_indices(walls.shape, *pos):
            if walls[neighbor_index]:
                continue
            
            score = depth + 1 + heuristic(neighbor_index, end)
            heapq.heappush(frontier, (score, depth+1, neighbor_index))

    return None

def compute_distance_graph(walls: NDArray[np.bool_], start: Tuple[int, int], targets: List[Tuple[int, int]]) -> Dict[Tuple[int, int], Dict[Tuple[int, int], int]]:
    nodes = [start] + targets
    adj = {node: {} for node in nodes}

    for n1, n2 in combinations(nodes, 2):
        depth = a_star(walls, n1, n2)
        adj[n1][n2] = depth
        adj[n2][n1] = depth

    return adj

def compute_path_weight(path: List[Tuple[int, int]], adj: Dict[Tuple[int, int], Dict[Tuple[int, int], int]]) -> int:
    return sum([adj[n1][n2] for n1, n2 in zip(path[:-1], path[1:])])

def solution(map: List[List[str]]) -> int:
    walls, start, targets = initialize(map)
    adj = compute_distance_graph(walls, start, targets)

    # Finding the minimum Hamiltonian Path
    min_path_weight = float("inf")
    min_path = None
    for path in permutations(targets):
        path_weight = adj[start][path[0]] + compute_path_weight(path, adj)
        if path_weight < min_path_weight:
            min_path_weight = path_weight
            min_path = [start] + list(path)
    
    # print(min_path)
    return min_path_weight

if __name__ == "__main__":
    example_map = load_input(Path(f"Day_{DAY:02d}/{EXAMPLE_INPUT_FILE_NAME}"))
    expected_answer = 14
    test(expected_answer, solution, example_map)

    map = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))
    solve(solution, map)