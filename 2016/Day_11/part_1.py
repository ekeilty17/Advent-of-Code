from pathlib import Path
from typing import List, Tuple, Set, Any, TypeAlias
from itertools import combinations
import queue

from Day_11.const import DAY, EXAMPLE_INPUT_FILE_NAME, INPUT_FILE_NAME
from Day_11.load_input import load_input
from utils.solve import test, solve

Device: TypeAlias = Tuple[str, str]

def is_floor_safe(floor: Set[Device]) -> bool:
    """
    if a chip is ever left in the same area as another RTG, 
    and it's not connected to its own RTG, the chip will be fried
    """

    microchips = {name for name, type in floor if type == "microchip"}
    generators = {name for name, type in floor if type == "generator"}

    for name in microchips:
        if name not in generators and len(generators) > 0:
            return False

    return True

# def get_state(elevator: int, floors: List[Set[Device]]) -> Any:
#     return (elevator, tuple([tuple(sorted(floor)) for floor in floors]))

def get_state(elevator: int, floors: List[Set[Device]]) -> Any:
    positions = {}

    for floor_num, floor in enumerate(floors):
        for name, type in floor:
            if name not in positions:
                positions[name] = [-1, -1]
            if type == "microchip":
                positions[name][0] = floor_num
            else:
                positions[name][1] = floor_num

    pairs = tuple(sorted((chip, gen) for chip, gen in positions.values()))
    return (elevator, pairs)

def move_devices(floors: List[Set[Device]], elevator: int, displacement: int, *devices: Device) -> bool:
    if not (0 <= elevator+displacement < len(floors)):
        return False
    
    for device in devices:
        if not device[0]:
            continue
        floors[elevator].remove(device)
        floors[elevator+displacement].add(device)
        
    return True
    

def bfs(floors: List[Set[Device]], elevator_start: int, target_floor: int) -> int | None:
    visited = set([])
    
    q = queue.Queue()
    q.put( (0, elevator_start, floors) )

    while not q.empty():

        depth, elevator, floors = q.get()
        
        # This pruning step is actually accounted for in `move_devices()`
        # if not (0 <= elevator < len(floors)):
        #     continue
        if not all(is_floor_safe(floor) for floor in floors):
            continue
        if len(floors[target_floor]) and not any(len(floor) for i, floor in enumerate(floors) if i != target_floor):
            return depth

        state = get_state(elevator, floors)
        if state in visited:
            continue
        visited.add(state)

        device_combinations = list(combinations(floors[elevator], 2)) + list(combinations(floors[elevator], 1))
        for devices in device_combinations:

            floors_down = [floor.copy() for floor in floors]
            if move_devices(floors_down, elevator, -1, *devices):
                q.put( (depth+1, elevator-1, floors_down) )

            floors_up = [floor.copy() for floor in floors]
            if move_devices(floors_up, elevator, 1, *devices):
                q.put( (depth+1, elevator+1, floors_up) )

    return None

def solution(floors: List[Set[Device]], elevator_start: int, target_floor: int) -> int:
    return bfs(floors, elevator_start-1, target_floor-1)

if __name__ == "__main__":
    elevator_start = 1
    target_floor = 4

    example_floors = load_input(Path(f"Day_{DAY:02d}/{EXAMPLE_INPUT_FILE_NAME}"))
    expected_answer = 11
    test(expected_answer, solution, example_floors, elevator_start, target_floor)

    floors = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))
    solve(solution, floors, elevator_start, target_floor)