from pathlib import Path
from typing import List, Tuple, Dict
import heapq
import numpy as np
from numpy.typing import NDArray

from Day_16.const import DAY, SMALL_EXAMPLE_INPUT_FILE_NAME, EXAMPLE_INPUT_FILE_NAME, INPUT_FILE_NAME
from Day_16.load_input import load_input
from utils.grid import get_position_of_value
from utils.solve import test, solve

DIRECTIONS = {
    "^": (-1, 0),
    ">": (0, 1),
    "v": (1, 0),
    "<": (0, -1)
}

def get_maze_neighbors(maze: NDArray[str], position: Tuple[int, int]) -> Dict[str, Tuple[int, int]]:
    
    return {
        direction: (position[0] + offset[0], position[1] + offset[1])
        for direction, offset in DIRECTIONS.items()
        if (0 <= position[0] + offset[0] < maze.shape[0]) \
            and (0 <= position[1] + offset[1] < maze.shape[1]) \
            and (maze[position] != "#")
    }

def compute_neighbor_weight(direction: str, neighbor_direction: str) -> int:
    neighbor_weight = 1
    if direction != neighbor_direction:
        neighbor_weight += 1000
    return neighbor_weight

def Dijkstra(maze: NDArray[str], start: Tuple[int, int], start_direction: str, end: Tuple[int, int]) -> int:

    dist = np.full(maze.shape, np.inf)
    dist[start] = 0

    pq = []
    heapq.heappush(pq, (dist[start], start, start_direction))

    while pq:
        position_distance, position, direction = heapq.heappop(pq)
        
        if position_distance > dist[position]:
            continue

        neighbor_dict = get_maze_neighbors(maze, position)
        for neighbor_direction, neighbor_position in neighbor_dict.items():
            neighbor_weight = compute_neighbor_weight(direction, neighbor_direction)

            total_neighbor_distance = dist[position] + neighbor_weight
            if total_neighbor_distance < dist[neighbor_position]:
                dist[neighbor_position] = total_neighbor_distance
                heapq.heappush(pq, (total_neighbor_distance, neighbor_position, neighbor_direction))

    return int(dist[end])

def solution(maze: List[List[str]]) -> int:
    maze = np.array(maze)

    start_position = get_position_of_value(maze, "S")
    end_position = get_position_of_value(maze, "E")
    start_direction = ">"   # problem says it starts facing east
    return Dijkstra(maze, start_position, start_direction, end_position)

if __name__ == "__main__":
    small_example_maze = load_input(Path(f"Day_{DAY:02d}/{SMALL_EXAMPLE_INPUT_FILE_NAME}"))
    small_expected_answer = 7036
    test(small_expected_answer, solution, small_example_maze)

    example_maze = load_input(Path(f"Day_{DAY:02d}/{EXAMPLE_INPUT_FILE_NAME}"))
    expected_answer = 11048
    test(expected_answer, solution, example_maze)

    maze = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))
    total = solution(maze)
    print("Puzzle Answer:", total)