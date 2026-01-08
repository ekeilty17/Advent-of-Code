from pathlib import Path
from typing import List, Tuple
import heapq
import numpy as np
from numpy.typing import NDArray

from Day_18.const import DAY, EXAMPLE_INPUT_FILE_NAME, INPUT_FILE_NAME
from Day_18.load_input import load_input
from utils.grid import get_orthogonal_neighbor_indices
from utils.solve import test, solve

def Dijkstra(memory: NDArray[str], start: Tuple[int, int]) -> List[List[int]]:

    dist = [[np.inf for _ in range(memory.shape[1])] for _ in range(memory.shape[0])]
    dist[start[0]][start[1]] = 0

    pq = []
    heapq.heappush(pq, (dist[start[0]][start[1]], start))

    while pq:
        position_distance, position = heapq.heappop(pq)
        i, j = position
        
        if position_distance > dist[i][j]:
            continue
        
        for neighbor_position in get_orthogonal_neighbor_indices(memory, i, j):
            if memory[neighbor_position] == "#":
                continue

            x, y = neighbor_position
            neighbor_weight = 1

            total_neighbor_distance = dist[i][j] + neighbor_weight
            if total_neighbor_distance < dist[x][y]:
                dist[x][y] = total_neighbor_distance
                heapq.heappush(pq, (total_neighbor_distance, neighbor_position))

    return dist

def solution(positions: List[Tuple[int]], memory_shape: Tuple[int, int], num_corrupt_bits: int) -> int:
    positions = positions[:num_corrupt_bits]
    memory = np.full(memory_shape, ".")
    memory[*zip(*positions)] = "#"

    dist = Dijkstra(memory, (0, 0))
    return dist[-1][-1]

if __name__ == "__main__":
    example_positions = load_input(Path(f"Day_{DAY:02d}/{EXAMPLE_INPUT_FILE_NAME}"))
    example_memory_shape = (7, 7)
    example_num_corrupt_bits = 12
    expected_answer = 22
    test(expected_answer, solution, example_positions, example_memory_shape, example_num_corrupt_bits)

    positions = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))
    memory_shape = (71, 71)
    num_corrupt_bits = 1024
    solve(solution, positions, memory_shape, num_corrupt_bits)