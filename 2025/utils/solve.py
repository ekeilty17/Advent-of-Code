import time
from typing import Callable

def _format_time(seconds):
    units = [
        (1, "s"),
        (1e-3, "ms"),
        (1e-6, "µs"),
        (1e-9, "ns"),
    ]
    for threshold, unit in units:
        if seconds >= threshold:
            return f"{seconds / threshold:.3g} {unit}"

    return f"{seconds / 1e-9:.3g} ns"

def solve(solution_func: Callable, *solution_args) -> int:
    start = time.time()
    answer = solution_func(*solution_args)
    end = time.time()
    
    print(f"Puzzle Answer: {answer}")
    print(f"Time taken:    {_format_time(end - start)}")
    print()

    return answer


def test(expected_answer, solution_func: Callable, *solution_args) -> bool:
    actual_answer = solution_func(*solution_args)

    if actual_answer == expected_answer:
        print("Test Passed!")
    else:
        print("Test Failed :(")
    
    print("\tExpected:", expected_answer)
    print("\tActual:  ", actual_answer)
    print()

    return actual_answer == expected_answer