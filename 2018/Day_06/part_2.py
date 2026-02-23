from pathlib import Path
from typing import Set

from Day_06.const import DAY, EXAMPLE_INPUT_FILE_NAME, INPUT_FILE_NAME
from Day_06.load_input import load_input
from Day_06.part_1 import Location, Coordinate, manhattan_distance
from utils.solve import test, solve

def get_total_manhattan_distance(locations: Set[Location], coord: Coordinate):
    return sum(manhattan_distance(coord, loc) for loc in locations)

def get_safe_region(locations: Set[Location], safe_distance: int) -> Set[Coordinate]:

    safe_region = set([])
    queue = [loc for loc in locations]
    while queue:
        coord = queue.pop(0)

        if coord in safe_region:
            continue
        if get_total_manhattan_distance(locations, coord) >= safe_distance:
            continue
        safe_region.add(coord)
            
        for offset in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
            neighbor = tuple([x1 + x2 for x1, x2 in zip(coord, offset)])
            queue.append(neighbor)

    return safe_region


def solution(locations: Set[Location], safe_distance: int) -> int:
    region = get_safe_region(locations, safe_distance)
    return len(region)

if __name__ == "__main__":
    example_locations = load_input(Path(f"Day_{DAY:02d}/{EXAMPLE_INPUT_FILE_NAME}"))
    example_safe_distance = 32
    expected_answer = 16
    test(expected_answer, solution, example_locations, example_safe_distance)

    locations = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))
    safe_distance = 10000
    solve(solution, locations, safe_distance)