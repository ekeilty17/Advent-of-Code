from pathlib import Path
from typing import List, Dict, Callable, Tuple

from Day_17.const import DAY, INPUT_FILE_NAME
from Day_17.const import EXAMPLE_INPUT_FILE_NAME_PART_2 as EXAMPLE_INPUT_FILE_NAME
from Day_17.load_input import load_input
from Day_17.part_1_alt import run_program, example_loop_func, loop_func
from utils.test import test


def solution(
        registers: Dict[str, int], 
        program: List[int],
        loop_func: Callable[[Dict[str, int]], Tuple[Dict[str, int], List[str]]],
    ) -> int:

    register_A = 1
    for n in range(2, len(program)+1):
        target = program[-n:]
        register_A <<= 3

        upper = register_A << 3
        while register_A < upper:
            registers_copy = registers.copy()
            registers_copy["A"] = register_A
            output = run_program(registers_copy, loop_func)
            
            if all(x == y for x, y in zip(output, target)):
                break

            register_A += 1

        # Failed to find a solution
        if register_A == upper:
            return None

    # Check that our solution is value
    if len(output) != len(program) or not all(x == y for x, y in zip(output, program)):
        return None

    return register_A

if __name__ == "__main__":
    
    example_registers, example_program = load_input(Path(f"Day_{DAY:02d}/{EXAMPLE_INPUT_FILE_NAME}"))
    registers, program = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))

    expected_answer = 117440
    test(expected_answer, solution, example_registers, example_program, example_loop_func)

    total = solution(registers, program, loop_func)
    print("Puzzle Answer:", total)