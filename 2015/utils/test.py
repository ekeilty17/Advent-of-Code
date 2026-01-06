from typing import Callable

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