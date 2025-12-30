from pathlib import Path
from typing import List, Tuple
import heapq
import numpy as np
from numpy.typing import NDArray

from Day_20.const import DAY, EXAMPLE_INPUT_FILE_NAME, INPUT_FILE_NAME
from Day_20.load_input import load_input
from utils.test import test
from utils.grid import get_position_of_value, get_orthogonal_neighbor_indices

def Dijkstra(racetrack: NDArray[str], start: Tuple[int, int]) -> List[List[int]]:

    dist = [[np.inf for _ in range(racetrack.shape[1])] for _ in range(racetrack.shape[0])]
    dist[start[0]][start[1]] = 0

    pq = []
    heapq.heappush(pq, (dist[start[0]][start[1]], start))

    while pq:
        position_distance, position = heapq.heappop(pq)
        i, j = position
        
        if position_distance > dist[i][j]:
            continue
        
        for neighbor_position in get_orthogonal_neighbor_indices(racetrack, i, j):
            if racetrack[neighbor_position] == "#":
                continue

            x, y = neighbor_position
            neighbor_weight = 1

            total_neighbor_distance = dist[i][j] + neighbor_weight
            if total_neighbor_distance < dist[x][y]:
                dist[x][y] = total_neighbor_distance
                heapq.heappush(pq, (total_neighbor_distance, neighbor_position))

    return dist

def search_for_cheats(racetrack: NDArray[str], start_dist: List[List[int]], end_dist: List[List[int]]):

    cheats = []
    for i in range(racetrack.shape[0]):
        for j in range(racetrack.shape[1]):
            if racetrack[i, j] != "#":     # no time save if we aren't walling
                continue

            min_dist_to_start = np.inf
            for ni, nj in get_orthogonal_neighbor_indices(racetrack, i, j):
                if racetrack[ni, nj] == "#":
                    continue
                min_dist_to_start = min(min_dist_to_start, start_dist[ni][nj])

            min_dist_to_end = np.inf
            for ni, nj in get_orthogonal_neighbor_indices(racetrack, i, j):
                if racetrack[ni, nj] == "#":
                    continue
                min_dist_to_end = min(min_dist_to_end, end_dist[ni][nj])
            
            total_cheated_distance = min_dist_to_start + 2 + min_dist_to_end
            cheats.append(total_cheated_distance)

    return cheats


def solution(racetrack: List[List[str]], picoseconds_to_save: int) -> int:
    racetrack = np.array(racetrack)

    start_position = get_position_of_value(racetrack, "S")
    end_position = get_position_of_value(racetrack, "E")
    
    start_dist = Dijkstra(racetrack, start_position)
    end_dist = Dijkstra(racetrack, end_position)

    no_cheat_picoseconds = start_dist[end_position[0]][end_position[1]]
    cheats = search_for_cheats(racetrack, start_dist, end_dist)

    return sum([(no_cheat_picoseconds - cheated_picoseconds) >= picoseconds_to_save for cheated_picoseconds in cheats])


if __name__ == "__main__":
    
    example_racetrack = load_input(Path(f"Day_{DAY:02d}/{EXAMPLE_INPUT_FILE_NAME}"))
    racetrack = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))

    example_picoseconds_to_save = 64
    expected_answer = 1
    test(expected_answer, solution, example_racetrack, example_picoseconds_to_save)

    picoseconds_to_save = 100
    total = solution(racetrack, picoseconds_to_save)
    print("Puzzle Answer:", total)