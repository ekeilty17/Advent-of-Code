from pathlib import Path
from typing import List, Tuple, Set, TypeAlias
import numpy as np
import heapq

from Day_08.const import DAY, EXAMPLE_INPUT_FILE_NAME, INPUT_FILE_NAME
from Day_08.load_input import load_input
from Day_08.part_1 import get_squared_distance, get_manhattan_distance, get_circuit
from utils.solve import test, solve

BoxCoordinate: TypeAlias = Tuple[int, int, int]

def solution(junction_box_positions: List[BoxCoordinate]) -> int:
    
    # Heap data structure to always get the next closest pair of boxes
    sorted_distances: List[Tuple[int, BoxCoordinate, BoxCoordinate]] = []
    for coord1 in junction_box_positions:
        for coord2 in junction_box_positions:
            if coord1 >= coord2:
                continue
            element = (get_squared_distance(coord1, coord2), coord1, coord2)
            heapq.heappush(sorted_distances, element)

    # list of sets of circuits
    circuits: List[Set[BoxCoordinate]] = [set([coord]) for coord in junction_box_positions]
    
    while len(circuits) > 1:
        # get next pair
        _, coord1, coord2 = heapq.heappop(sorted_distances)

        # get corresponding ciruits
        i1, circuit1 = get_circuit(circuits, coord1)
        i2, circuit2 = get_circuit(circuits, coord2)
        
        # if they are already in the same circuit, then continue
        if i1 == i2:
            continue
        
        # merge the two circuits
        circuit1.update(circuit2)       # in place update
        del circuits[i2]

    x1, _, _ = coord1
    x2, _, _ = coord2
    return x1 * x2


if __name__ == "__main__":
    example_junction_box_positions = load_input(Path(f"Day_{DAY:02d}/{EXAMPLE_INPUT_FILE_NAME}"))
    expected_answer = 25272
    test(expected_answer, solution, example_junction_box_positions)

    junction_box_positions = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))
    solve(solution, junction_box_positions)