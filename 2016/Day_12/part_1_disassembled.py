from typing import Dict, Tuple
from utils.solve import test, solve

def example_solution(registers: Dict[str, int], target_register: str) -> int:
    registers["a"] = 42                 # sets a to 42 on any input
    return registers[target_register]

def disassembled(a: int, b: int, c: int, d: int) -> Tuple[int, int, int, int]:
    # chunk 0
    a = 1
    b = 1
    d = 26

    # chunk 1
    if c != 0:
        c = 7
        while c != 0:
            d += 1
            c -= 1

    # chunk 2
    while d != 0:
        c = a
        while b != 0:
            a += 1
            b -= 1

        b = c
        d -= 1

    # chunk 3
    c = 17
    while c != 0:
        d = 18
        while d != 0:
            a += 1
            d -= 1
        c -= 1

    return a, b, c, d

def efficient(a: int, b: int, c: int, d: int) -> Tuple[int, int, int, int]:
    # chunk 0
    a = 1
    b = 1
    d = 26

    # chunk 1
    if c != 0:
        d += 7

    # chunk 2
    for _ in range(d):
        b, a = a, a + b

    # chunk 3
    a += 17*18

    return a, b, c, d

def solution(registers: Dict[str, int], target_register: str) -> int:
    # registers["a"], registers["b"], registers["c"], registers["d"] = disassembled(**registers)
    registers["a"], registers["b"], registers["c"], registers["d"] = efficient(**registers)
    return registers[target_register]

if __name__ == "__main__":
    registers = {"a": 0, "b": 0, "c": 0, "d": 0}
    target_register = "a"

    expected_answer = 42
    test(expected_answer, example_solution, registers, target_register)

    solve(solution, registers, target_register)