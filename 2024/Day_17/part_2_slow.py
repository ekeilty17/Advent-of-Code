from pathlib import Path
from typing import List, Dict

from Day_17.const import DAY, INPUT_FILE_NAME
from Day_17.const import EXAMPLE_INPUT_FILE_NAME_PART_2 as EXAMPLE_INPUT_FILE_NAME
from Day_17.load_input import load_input
from Day_17.part_1 import run_program
from utils.solve import test, solve

# In theory this would work, but it's way too slow
# Even if you added faster stop conditions, it's still too slow
def solution(registers: Dict[str, int], program: List[int]) -> int:

    register_A = 0
    while True:
        registers_copy = registers.copy()
        registers_copy["A"] = register_A
        output = run_program(registers_copy, program)
        if len(output) == len(program) and all(x == y for x, y in zip(output, program)):
            return register_A

        register_A += 1

if __name__ == "__main__":
    example_registers, example_program = load_input(Path(f"Day_{DAY:02d}/{EXAMPLE_INPUT_FILE_NAME}"))
    expected_answer = 117440
    test(expected_answer, solution, example_registers, example_program)

    registers, program = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))
    solve(solution, registers, program)