from pathlib import Path
from typing import List, Set
from itertools import combinations
import heapq

from Day_11.const import DAY, EXAMPLE_INPUT_FILE_NAME, INPUT_FILE_NAME
from Day_11.load_input import load_input
from Day_11.part_1 import Device, is_floor_safe, get_state, move_devices
from utils.solve import test, solve

# def heuristic(floors: List[Set[Device]], target_floor: int) -> int:
#     return sum([
#         abs(target_floor - floor_num) * len(floor) 
#         for floor_num, floor in enumerate(floors)
#     ]) // 2

def heuristic(floors: List[Set[Device]], target_floor: int) -> int:
    return sum([
        abs(target_floor - floor_num) * (len(floor) + (len(floor) - 1))
        for floor_num, floor in enumerate(floors)
        if floor
    ]) // 2

def a_star(floors: List[Set[Device]], elevator_start: int, target_floor: int) -> int | None:
    visited = {}
    
    frontier = []
    score = 0 + heuristic(floors, target_floor)
    heapq.heappush(frontier, (score, 0, elevator_start, floors) )
    visited[get_state(elevator_start, floors)] = 0

    while frontier:
        score, depth, elevator, floors = heapq.heappop(frontier)

        # This pruning step is actually accounted for in `move_devices()`
        # if not (0 <= elevator < len(floors)):
        #     continue
        if not all(is_floor_safe(floor) for floor in floors):
            continue
        if len(floors[target_floor]) and not any(len(floor) for i, floor in enumerate(floors) if i != target_floor):
            return depth
        
        # Move this to the neighbor function which is faster as we are not needlessly increasing the frontier
        # state = get_state(elevator, floors)
        # if visited.get(state, float("inf")) <= depth:
        #     continue
        # visited[state] = depth

        device_combinations = list(combinations(floors[elevator], 2)) + list(combinations(floors[elevator], 1))
        for devices in device_combinations:
            
            floors_down = [floor.copy() for floor in floors]
            if move_devices(floors_down, elevator, -1, *devices):
                state = get_state(elevator-1, floors_down)
                if visited.get(state, float("inf")) > depth + 1:
                    visited[state] = depth + 1
                    score = depth + 1 + heuristic(floors_down, target_floor)
                    heapq.heappush(frontier, (score, depth+1, elevator-1, floors_down))

            floors_up = [floor.copy() for floor in floors]
            if move_devices(floors_up, elevator, 1, *devices):
                state = get_state(elevator+1, floors_up)
                if visited.get(state, float("inf")) > depth + 1:
                    visited[state] = depth + 1
                    score = depth + 1 + heuristic(floors_up, target_floor)
                    heapq.heappush(frontier, (score, depth+1, elevator+1, floors_up))

    return None

def solution(floors: List[Set[Device]], elevator_start: int, target_floor: int) -> int:
    return a_star(floors, elevator_start-1, target_floor-1)

if __name__ == "__main__":
    elevator_start = 1
    target_floor = 4

    small_example_floors = load_input(Path(f"Day_{DAY:02d}/{EXAMPLE_INPUT_FILE_NAME}"))
    small_expected_answer = 11
    test(small_expected_answer, solution, small_example_floors, elevator_start, target_floor)

    example_floors = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))
    expected_answer = 33
    test(expected_answer, solution, example_floors, elevator_start, target_floor)
    # solve(solution, example_floors, elevator_start, target_floor)

    floors = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))
    missing_devices = [("elerium", "generator"), ("elerium", "microchip"), ("dilithium", "generator"), ("dilithium", "microchip")]
    floors[0].update(missing_devices)
    solve(solution, floors, elevator_start, target_floor)