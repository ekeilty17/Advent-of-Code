from pathlib import Path
from typing import List

from Day_22.const import DAY, EXAMPLE_INPUT_FILE_NAME, INPUT_FILE_NAME
from Day_22.load_input import load_input
from Day_22.part_1 import Coordinate, initialize, turn_left, turn_right, move_in_direction
from utils.solve import test, solve

def turn_around(direction: Coordinate) -> Coordinate:
    x, y = direction
    return -x, -y

def solution(map: List[List[str]], num_bursts: int) -> int:
    infected, virus_pos, virus_direction = initialize(map)
    state_by_node = {node: "I" for node in infected}

    num_bursts_causing_infections = 0
    for _ in range(num_bursts):
        state = state_by_node.get(virus_pos, "C")
        
        # cleaned
        if state == "C":
            state_by_node[virus_pos] = "W"
            virus_direction = turn_left(virus_direction)
        
        # weakened
        elif state == "W":
            state_by_node[virus_pos] = "I"
            num_bursts_causing_infections += 1
        
        # infected
        elif state == "I":
            state_by_node[virus_pos] = "F"
            virus_direction = turn_right(virus_direction)
        
        # flagged
        elif state == "F":
            state_by_node[virus_pos] = "C"          # You could also delete from the dictionary, not sure which is better
            virus_direction = turn_around(virus_direction)
        else:
            raise Exception(f"Unexpected node state: {state}")
        
        virus_pos = move_in_direction(virus_pos, virus_direction)

    return num_bursts_causing_infections

if __name__ == "__main__":
    num_bursts = 10_000_000

    example_map = load_input(Path(f"Day_{DAY:02d}/{EXAMPLE_INPUT_FILE_NAME}"))
    expected_answer = 2511944
    test(expected_answer, solution, example_map, num_bursts)

    map = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))
    solve(solution, map, num_bursts)