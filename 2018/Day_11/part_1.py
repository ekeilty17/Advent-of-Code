from typing import List, Tuple
import numpy as np
from utils.solve import test, solve

def get_power_level(x: int, y: int, serial_number: int) -> int:
    rack_id = x + 10
    power_level = rack_id * y
    power_level += serial_number
    power_level *= rack_id
    power_level = int(power_level // 100) % 10
    power_level -= 5
    return power_level

def compute_power_levels(serial_number: int, grid_shape: Tuple[int, int]) -> List[List[int]]:
    return [[get_power_level(x+1, y+1, serial_number) for y in range(grid_shape[1])] for x in range(grid_shape[0])]

def convolution_2d(
        arr: List[List[int]],
        kernel: List[List[int]],
    ) -> Tuple[int, int]:
    n1, n2 = len(arr), len(arr[0])
    k1, k2 = len(kernel), len(kernel[0])
    
    convolution = [[0 for _ in range(n2-k2)] for _ in range(n1-k1)]
    for x in range(n1-k1):
        for y in range(n2-k2):
            for i in range(k1):
                for j in range(k2):
                    convolution[x][y] += kernel[i][j] * arr[x+i][y+j]
    
    return convolution

def solution(serial_number: int, grid_shape: Tuple[int, int], kernel_shape: Tuple[int, int]) -> Tuple[int, int]:
    # initial pseudo-random array
    power_levels = compute_power_levels(serial_number, grid_shape)
    
    # compute convolution
    kernel = [[1] * kernel_shape[1] for _ in range(kernel_shape[0])]
    kernel_power_levels = convolution_2d(power_levels, kernel)
    
    # get maximum convolution value
    flat_power_levels = [
        (kernel_power_levels[x][y], x, y)
        for x in range(len(kernel_power_levels)) 
        for y in range(len(kernel_power_levels[x]))
    ]
    max_kernel_power_level, max_x, max_y = max(flat_power_levels)
    return max_x+1, max_y+1

if __name__ == "__main__":
    grid_shape = (300, 300)
    kernel_shape = (3, 3)
    
    examples = [
        (18, (33, 45)),
        (42, (21, 61)),
    ]
    for example_serial_number, expected_answer in examples:
        test(expected_answer, solution, example_serial_number, grid_shape, kernel_shape)

    serial_number = 1955
    solve(solution, serial_number, grid_shape, kernel_shape)