from typing import List, Tuple
from Day_11.part_1 import compute_power_levels, convolution_2d
from utils.solve import test, solve

def brute_force(power_levels: List[List[int]]) -> List[List[List[int]]]:
    power_levels_by_kernel_size = [[]]
    
    for k in range(1, len(power_levels)+1):
        kernel = [[1] * k for _ in range(k)]
        power_levels_by_kernel_size.append(
            convolution_2d(power_levels, kernel)
        )

    return power_levels_by_kernel_size

def efficient(power_levels: List[List[int]]) -> List[List[List[int]]]:
    
    def compute_next_kernel_power_levels(
        power_levels_by_kernel_size: List[List[List[int]]],
        k: int
    ) -> List[List[int]]:
        n1, n2 = len(power_levels_by_kernel_size[1]), len(power_levels_by_kernel_size[1][0])
        kernel_power_levels = [[0 for _ in range(n2-k)] for _ in range(n1-k)]

        for i in range(n1-k):
            for j in range(n2-k):
                kernel_power_levels[i][j] += (
                    power_levels_by_kernel_size[1][i+k-1][j]
                    + power_levels_by_kernel_size[1][i][j+k-1]
                    + power_levels_by_kernel_size[k-1][i][j] 
                    + power_levels_by_kernel_size[k-1][i+1][j+1]
                    - power_levels_by_kernel_size[k-2][i+1][j+1]
                )
        
        return kernel_power_levels

    power_levels_by_kernel_size = [
        [],
        power_levels,
        convolution_2d(power_levels, [[1] * 2 for _ in range(2)])
    ]
    for k in range(3, len(power_levels)+1):
        power_levels_by_kernel_size.append(
            compute_next_kernel_power_levels(power_levels_by_kernel_size, k)
        )
    
    return power_levels_by_kernel_size

def solution(serial_number: int, grid_shape: Tuple[int, int]) -> Tuple[int, int, int]:
    # initial pseudo-random array
    power_levels = compute_power_levels(serial_number, grid_shape)
    
    # Compute convolutions for all kernel sizes
    # power_levels_by_kernel_size = brute_force(power_levels)
    power_levels_by_kernel_size = efficient(power_levels)

    # get maximum convolution value
    flat_power_levels = [
        (power_levels_by_kernel_size[kernel_size][x][y], x, y, kernel_size) 
        for kernel_size, power_levels in enumerate(power_levels_by_kernel_size)
        for x in range(len(power_levels))
        for y in range(len(power_levels[x]))
    ]
    max_kernel_power_level, max_x, max_y, max_kernel_size = max(flat_power_levels)
    return max_x+1, max_y+1, max_kernel_size

if __name__ == "__main__":
    grid_shape = (300, 300)
    
    examples = [
        (18, (90, 269, 16)),
        (42, (232, 251, 12)),
    ]
    for example_serial_number, expected_answer in examples:
        test(expected_answer, solution, example_serial_number, grid_shape)

    serial_number = 1955
    solve(solution, serial_number, grid_shape)
    # 231,108,14