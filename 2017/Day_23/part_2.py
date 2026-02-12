import math
from utils.solve import solve

def count_composite_numbers(start: int, end: int, steps: int) -> int:
    num_composites = 0
    for n in range(start, end+steps, steps):
        for k in range(2, int(math.sqrt(n))+1):
            if n % k == 0:
                num_composites += 1
                break
    
    return num_composites

def solution() -> int:
    start = end = 79
    start = 100*start + 100000
    end = start + 17000

    return count_composite_numbers(start, end, 17)

if __name__ == "__main__":
    solve(solution)