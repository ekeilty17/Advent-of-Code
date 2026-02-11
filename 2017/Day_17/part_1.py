from typing import List
from utils.solve import test, solve

def compute_spinlock(steps_per_insert: int, num_inserts: int) -> List[int]:
    spinlock = [0]
    i = 0
    for k in range(1, num_inserts+1):
        i = (i + steps_per_insert) % k
        spinlock = spinlock[:i+1] + [k] + spinlock[i+1:]
        i += 1

    return spinlock

def solution(steps_per_insert: int, num_inserts: int) -> int:
    spinlock = compute_spinlock(steps_per_insert, num_inserts)
    
    index = spinlock.index(num_inserts)
    next_index = (index + 1) % len(spinlock)
    return spinlock[next_index]

if __name__ == "__main__":
    num_inserts = 2017
    
    example_steps_per_insert = 3
    expected_answer = 638
    test(expected_answer, solution, example_steps_per_insert, num_inserts)

    steps_per_insert = 363
    solve(solution, steps_per_insert, num_inserts)