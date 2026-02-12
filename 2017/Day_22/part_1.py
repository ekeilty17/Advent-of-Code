from pathlib import Path
from typing import List, Tuple, Set, TypeAlias

from Day_22.const import DAY, EXAMPLE_INPUT_FILE_NAME, INPUT_FILE_NAME
from Day_22.load_input import load_input
from utils.solve import test, solve

Coordinate: TypeAlias = Tuple[int, int]

def turn_left(direction: Coordinate) -> Coordinate:
    x, y = direction
    return -y, x

def turn_right(direction: Coordinate) -> Coordinate:
    x, y = direction
    return y, -x

def move_in_direction(pos: Coordinate, direction: Coordinate) -> Coordinate:
    x, y = pos
    dx, dy = direction
    return x+dx, y+dy

def initialize(map: List[List[str]]) -> Tuple[Set[Coordinate], Coordinate, Coordinate]:
    infected = set([])
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == "#":
                infected.add((i, j))
    
    virus_pos = (len(map)//2, len(map[0])//2)   # start in middle of grid
    virus_direction = (-1, 0)                   # facing "up"

    return infected, virus_pos, virus_direction

def solution(map: List[List[str]], num_bursts: int) -> int:
    infected, virus_pos, virus_direction = initialize(map)

    num_bursts_causing_infections = 0
    for _ in range(num_bursts):
        if virus_pos in infected:
            infected.remove(virus_pos)
            virus_direction = turn_right(virus_direction)
            
        else:
            infected.add(virus_pos)
            virus_direction = turn_left(virus_direction)
            num_bursts_causing_infections += 1
        
        virus_pos = move_in_direction(virus_pos, virus_direction)

    return num_bursts_causing_infections

if __name__ == "__main__":
    num_bursts = 10_000

    example_map = load_input(Path(f"Day_{DAY:02d}/{EXAMPLE_INPUT_FILE_NAME}"))
    expected_answer = 5587
    test(expected_answer, solution, example_map, num_bursts)

    map = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))
    solve(solution, map, num_bursts)