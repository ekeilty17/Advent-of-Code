from pathlib import Path
from typing import List, Tuple

import os
import numpy as np

from Day_14.const import DAY, INPUT_FILE_NAME
from Day_14.load_input import load_input
from Day_14.part_1 import compute_final_position
from utils.display import display_np_bool
from utils.solve import solve

def display_robot_positions(floor_shape: Tuple[int, int], positions: List[Tuple[int, int]]) -> str:
    floor = np.zeros(floor_shape, dtype=int)
    for x, y in positions:
        floor[x, y] += 1
    
    floor = floor.T
    return display_np_bool(floor != 0)

def manual_search_for_christmas_tree(floor_shape: Tuple[int, int], initial_positions: List[Tuple[int, int]], velocities: List[Tuple[int, int]]) -> int:
    
    positions = initial_positions
    time = 0
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        display_robot_positions(floor_shape, positions)
        print()
        print("Current Time Step:", time)
        print()
        x = input("ENTER for next time step or type STOP: ")
        if x.lower().strip() == "stop":
            break
        positions = [
            compute_final_position(floor_shape, position, velocity)
            for position, velocity in zip(positions, velocities)
        ]
        time += 1
    
    return time
    
def compute_total_distance(positions: List[Tuple[int, int]]):
    def manhattan_distance(x1, y1, x2, y2):
        return abs(x2 - x1) + abs(y2 - y1)
    
    total = 0
    for i in range(len(positions)):
        x1, y1 = positions[i]
        for j in range(i+1, len(positions)):
            x2, y2 = positions[j]
            total += manhattan_distance(x1, y1, x2, y2)
    
    return total

def auto_search_for_christmas_tree(
        floor_shape: Tuple[int, int], 
        initial_positions: List[Tuple[int, int]], 
        velocities: List[Tuple[int, int]],
        max_time: int=10_000
    ) -> int:
    
    positions = initial_positions
    time_scores = []
    for time in range(max_time):
        score = compute_total_distance(positions)
        time_scores.append((score, time))
        positions = [
            compute_final_position(floor_shape, position, velocity)
            for position, velocity in zip(positions, velocities)
        ]

    _, min_score_time = min(time_scores)
    return min_score_time

def solution(floor_shape: Tuple[int, int], initial_positions: List[Tuple[int, int]], velocities: List[Tuple[int, int]]) -> int:
    # return manual_search_for_christmas_tree(floor_shape, initial_positions, velocities)
    return auto_search_for_christmas_tree(floor_shape, initial_positions, velocities)

if __name__ == "__main__":
    positions, velocities = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))
    floor_shape = (101, 103)
    solve(solution, floor_shape, positions, velocities)