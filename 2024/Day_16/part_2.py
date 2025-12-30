from pathlib import Path
from typing import List, Tuple
import heapq
import numpy as np
from numpy.typing import NDArray

from Day_16.const import DAY, SMALL_EXAMPLE_INPUT_FILE_NAME, EXAMPLE_INPUT_FILE_NAME, INPUT_FILE_NAME
from Day_16.load_input import load_input
from Day_16.part_1 import get_maze_neighbors, compute_neighbor_weight, DIRECTIONS
from utils.test import test
from utils.grid import get_position_of_value

def Dijkstra(maze: NDArray[str], start: Tuple[int, int], start_direction: str) -> int:

    dist = [[{direction: np.inf for direction in DIRECTIONS} for _ in range(maze.shape[1])] for _ in range(maze.shape[0])]
    pred = [[{direction: [] for direction in DIRECTIONS}     for _ in range(maze.shape[1])] for _ in range(maze.shape[0])]

    dist[start[0]][start[1]][start_direction] = 0

    pq = []
    heapq.heappush(pq, (dist[start[0]][start[1]][start_direction], start, start_direction))

    while pq:
        position_distance, position, direction = heapq.heappop(pq)
        pi, pj = position

        if position_distance > dist[pi][pj][direction]:
            continue

        neighbor_dict = get_maze_neighbors(maze, position)
        for neighbor_direction, neighbor_position in neighbor_dict.items():
            ni, nj = neighbor_position

            neighbor_weight = compute_neighbor_weight(direction, neighbor_direction)
            total_neighbor_distance = dist[pi][pj][direction] + neighbor_weight

            if total_neighbor_distance < dist[ni][nj][neighbor_direction]:
                dist[ni][nj][neighbor_direction] = total_neighbor_distance
                pred[ni][nj][neighbor_direction] = set([position])
                heapq.heappush(pq, (total_neighbor_distance, neighbor_position, neighbor_direction))
            
            if total_neighbor_distance == dist[ni][nj][neighbor_direction]:
                pred[ni][nj][neighbor_direction].add(position)

    return dist, pred

def backtrack(
        dist: List[List[List[Tuple[int, int]]]], 
        pred: List[List[List[Tuple[int, int]]]], 
        position: Tuple[int, int], 
        direction: str
    ) -> List[List[Tuple[int, int]]]:
    
    i, j = position

    paths = []
    for pred_direction in DIRECTIONS:
        for pred_position in pred[i][j][direction]:
            x, y = pred_position
            
            # prevents loops
            if dist[i][j][direction] < dist[x][y][pred_direction]:
                continue

            pred_paths = backtrack(dist, pred, pred_position, pred_direction)
            
            for path in pred_paths:
                path.append(position)
            paths.extend( pred_paths )
    
    # base case essentially
    if len(paths) == 0:
        paths = [[position]]

    return paths

def solution(maze: List[List[str]]) -> int:
    maze = np.array(maze)

    start_position = get_position_of_value(maze, "S")
    end_position = get_position_of_value(maze, "E")
    start_direction = ">"   # problem says it starts facing east
    dist, pred = Dijkstra(maze, start_position, start_direction)
    
    paths = []
    min_dist = min(dist[end_position[0]][end_position[1]].values())
    for end_direction, end_distance in dist[end_position[0]][end_position[1]].items():
        if end_distance > min_dist:
            continue
        paths.extend( backtrack(dist, pred, end_position, end_direction) )
    
    unique_positions = set([])
    for path in paths:
        unique_positions.update(path)
    
    return len(unique_positions)

if __name__ == "__main__":
    
    small_example_maze = load_input(Path(f"Day_{DAY:02d}/{SMALL_EXAMPLE_INPUT_FILE_NAME}"))
    example_maze = load_input(Path(f"Day_{DAY:02d}/{EXAMPLE_INPUT_FILE_NAME}"))
    maze = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))

    small_expected_answer = 45
    test(small_expected_answer, solution, small_example_maze)

    expected_answer = 64
    test(expected_answer, solution, example_maze)

    total = solution(maze)
    print("Puzzle Answer:", total)