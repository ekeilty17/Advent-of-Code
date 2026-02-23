from pathlib import Path
from typing import Tuple, Set, TypeAlias

from Day_06.const import DAY, EXAMPLE_INPUT_FILE_NAME, INPUT_FILE_NAME
from Day_06.load_input import load_input
from utils.solve import test, solve

Location: TypeAlias = Tuple[int, int]
Coordinate: TypeAlias = Tuple[int, int]

def manhattan_distance(coord1: Coordinate, coord2: Coordinate) -> int:
    x1, y1 = coord1
    x2, y2 = coord2
    return abs(x2 - x1) + abs(y2 - y1)

# Not used, but an interesting function
def get_manhattan_radius(coord: Coordinate, R: int) -> Set[Coordinate]:
    x, y = coord
    return set([(x+bx*dx, y+by*(R-dx)) for dx in range(R+1) for bx in [-1, 1] for by in [-1, 1]])

def is_manhattan_bounded(locations: Set[Location], location: Location) -> bool:
    x1, y1 = location
    return (
        any(x2 > x1 and abs(y2 - y1) <= abs(x2 - x1) for x2, y2 in locations)
        and any(x2 < x1 and abs(y2 - y1) <= abs(x2 - x1) for x2, y2 in locations)
        and any(y2 > y1 and abs(x2 - x1) <= abs(y2 - y1) for x2, y2 in locations)
        and any(y2 < y1 and abs(x2 - x1) <= abs(y2 - y1) for x2, y2 in locations)
    )

def get_dangerous_area(locations: Set[Location], start: Location) -> Set[Coordinate]:

    area = set([])
    queue = [(start, 0)]
    while queue:
        coord, distance = queue.pop(0)

        if coord in area:
            continue
        if any(manhattan_distance(coord, loc) <= distance for loc in locations if loc != start):
            continue
        area.add(coord)
            
        for offset in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
            neighbor = tuple([x1 + x2 for x1, x2 in zip(coord, offset)])
            queue.append( (neighbor, distance+1) )

    return area

def solution(locations: Set[Location]) -> int:
    bounded_locations = [location for location in locations if is_manhattan_bounded(locations, location)]
    bounded_location_areas = {location: get_dangerous_area(locations, location) for location in bounded_locations}
    max_area_Location, max_area_coordinates = max(bounded_location_areas.items(), key=lambda t: len(t[1]))
    return len(max_area_coordinates)

if __name__ == "__main__":
    example_locations = load_input(Path(f"Day_{DAY:02d}/{EXAMPLE_INPUT_FILE_NAME}"))
    expected_answer = 17
    test(expected_answer, solution, example_locations)

    locations = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))
    solve(solution, locations)