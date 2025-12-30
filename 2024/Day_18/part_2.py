from pathlib import Path
from typing import List, Tuple
import numpy as np

from Day_18.const import DAY, EXAMPLE_INPUT_FILE_NAME, INPUT_FILE_NAME
from Day_18.load_input import load_input
from Day_18.part_1 import Dijkstra
from utils.test import test

def linear_search(positions: List[Tuple[int]], memory_shape: Tuple[int, int]) -> Tuple[int, int]:
    uncorrupted_memory = np.full(memory_shape, ".")
    
    for i in range(len(positions)-1):
        memory = uncorrupted_memory.copy()
        memory[*zip(*positions[:i+1])] = "#"

        dist = Dijkstra(memory, (0, 0))
        if np.isinf( dist[-1][-1] ):
            return positions[i]

def binary_search(positions: List[Tuple[int]], memory_shape: Tuple[int, int]) -> Tuple[int, int]:
    uncorrupted_memory = np.full(memory_shape, ".")

    a, b = 0, len(positions)
    while a < b:
        m = (a + b) // 2
        memory = uncorrupted_memory.copy()
        memory[*zip(*positions[:m])] = "#"
        
        dist = Dijkstra(memory, (0, 0))
        if np.isinf( dist[-1][-1] ):        # no path found
            b = m
        else:
            a = m+1
    
    m = (a + b) // 2
    return positions[m-1]

def solution(positions: List[Tuple[int]], memory_shape: Tuple[int, int]) -> Tuple[int, int]:
    # return linear_search(positions, memory_shape)
    return binary_search(positions, memory_shape)

if __name__ == "__main__":
    
    example_positions = load_input(Path(f"Day_{DAY:02d}/{EXAMPLE_INPUT_FILE_NAME}"))
    positions = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))

    example_memory_shape = (7, 7)
    expected_answer = (6, 1)
    test(expected_answer, solution, example_positions, example_memory_shape)

    memory_shape = (71, 71)
    total = solution(positions, memory_shape)
    print("Puzzle Answer:", total)