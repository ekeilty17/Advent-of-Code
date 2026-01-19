from typing import Tuple, Dict
import math

from utils.solve import test, solve

def example_solution(egg_register: str, num_eggs: int) -> int:
    registers = {"a": 0, "b": 0, "c": 0, "d": 0}
    registers["a"] = 3                 # sets a to 3 on any input
    return registers[egg_register]

def disassembled(a: int, b: int, c: int, d: int) -> Tuple[int, int, int, int]:
    # chunk 0
    b = a
    b -= 1

    # chunk 1
    while c != 2:        # when c == 2, the jnz instruction becomes cpy

        # chunk 1.1
        d = a
        a = 0
        while d != 0:
            c = b
            while c != 0:
                a += 1
                c -= 1
            d -= 1

        # chunk 1.2
        b -= 1
        c = b
        d = c
        while d != 0:
            d -= 1
            c += 1

    # chunk 2
    c = 81
    while c != 0:
        d = 73
        while d != 0:
            a += 1
            d -= 1
        c -= 1

    return a, b, c, d

def efficient(a: int, b: int, c: int, d: int) -> Tuple[int, int, int, int]:
    a = 81 * 73 + math.factorial(a)
    b = 1
    c = d = 0
    return a, b, c, d

def solution(egg_register: str, num_eggs: int) -> int:
    registers = {"a": 0, "b": 0, "c": 0, "d": 0}
    registers[egg_register] = num_eggs

    # registers["a"], registers["b"], registers["c"], registers["d"] = disassembled(**registers)
    registers["a"], registers["b"], registers["c"], registers["d"] = efficient(**registers)
    
    return registers[egg_register]

if __name__ == "__main__":
    egg_register = "a"

    example_num_eggs = 0
    expected_answer = 3
    test(expected_answer, example_solution, egg_register, example_num_eggs)

    num_eggs = 7
    solve(solution, egg_register, num_eggs)