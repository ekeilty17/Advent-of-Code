from pathlib import Path
from typing import List, Tuple, Set, TypeAlias
import numpy as np
import heapq

from Day_08.const import DAY, EXAMPLE_INPUT_FILE_NAME, INPUT_FILE_NAME
from Day_08.load_input import load_input
from utils.solve import test, solve

BoxCoordinate: TypeAlias = Tuple[int, int, int]

def get_squared_distance(coord1: BoxCoordinate, coord2: BoxCoordinate) -> int:
    x1, y1, z1 = coord1
    x2, y2, z2 = coord2
    return (x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2

def get_manhattan_distance(coord1: BoxCoordinate, coord2: BoxCoordinate) -> int:
    x1, y1, z1 = coord1
    x2, y2, z2 = coord2
    return abs(x2 - x1) + abs(y2 - y1) + abs(z2 - z1)

def get_circuit(circuits: List[Set[BoxCoordinate]], coord: BoxCoordinate):
    for i, circuit in enumerate(circuits):
        if coord in circuit:
            return i, circuit
    
    raise RuntimeError(f"Did not find circuit with coordinate {coord}\n{circuits}")

def solution(junction_box_positions: List[BoxCoordinate], num_pairs: int) -> int:
    
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

    for _ in range(num_pairs):
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
    
    sorted_circuits = sorted(circuits, key=len, reverse=True)
    sorted_circuit_lengths = [len(circuit) for circuit in sorted_circuits]
    return np.prod(sorted_circuit_lengths[:3])

if __name__ == "__main__":
    example_junction_box_positions = load_input(Path(f"Day_{DAY:02d}/{EXAMPLE_INPUT_FILE_NAME}"))
    num_pairs = 10
    expected_answer = 40
    test(expected_answer, solution, example_junction_box_positions, num_pairs)

    junction_box_positions = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))
    num_pairs = 1000
    solve(solution, junction_box_positions, num_pairs)