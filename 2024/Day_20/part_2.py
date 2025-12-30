from pathlib import Path
from typing import List, Tuple
import heapq
import numpy as np
from numpy.typing import NDArray

from Day_20.const import DAY, EXAMPLE_INPUT_FILE_NAME, INPUT_FILE_NAME
from Day_20.load_input import load_input
from Day_20.part_1 import Dijkstra
from utils.test import test
from utils.grid import get_position_of_value

def manhattan_distance(x1, y1, x2, y2):
    return abs(x2 - x1) + abs(y2 - y1)

def search_for_cheats(racetrack: NDArray[str], start_dist: List[List[int]], end_dist: List[List[int]], invisibility_length: int):

    cheats = []
    for i in range(racetrack.shape[0]):
        for j in range(racetrack.shape[1]):
            if racetrack[i, j] == "#":
                continue
            min_dist_to_start = start_dist[i][j]
            
            for x in range(max(0, i - invisibility_length), min(i + invisibility_length + 1, racetrack.shape[0])):
                for y in range(max(0, j - invisibility_length), min(j + invisibility_length + 1, racetrack.shape[1])):
                    if racetrack[x, y] == "#":
                        continue
                    if manhattan_distance(i, j, x, y) > invisibility_length:
                        continue

                    min_dist_to_end = end_dist[x][y]
                    total_cheated_distance = min_dist_to_start + manhattan_distance(i, j, x, y) + min_dist_to_end
                    cheats.append(total_cheated_distance)

    return cheats

def solution(racetrack: List[List[str]], picoseconds_to_save: int, invisibility_length: int) -> int:
    racetrack = np.array(racetrack)

    start_position = get_position_of_value(racetrack, "S")
    end_position = get_position_of_value(racetrack, "E")
    
    start_dist = Dijkstra(racetrack, start_position)
    end_dist = Dijkstra(racetrack, end_position)

    no_cheat_picoseconds = start_dist[end_position[0]][end_position[1]]
    cheats = search_for_cheats(racetrack, start_dist, end_dist, invisibility_length)

    return sum([(no_cheat_picoseconds - cheated_picoseconds) >= picoseconds_to_save for cheated_picoseconds in cheats])


if __name__ == "__main__":
    
    example_racetrack = load_input(Path(f"Day_{DAY:02d}/{EXAMPLE_INPUT_FILE_NAME}"))
    racetrack = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))

    example_picoseconds_to_save = 76
    example_invisibility_length = 20
    expected_answer = 3
    test(expected_answer, solution, example_racetrack, example_picoseconds_to_save, example_invisibility_length)

    picoseconds_to_save = 100
    invisibility_length = 20
    total = solution(racetrack, picoseconds_to_save, invisibility_length)
    print("Puzzle Answer:", total)