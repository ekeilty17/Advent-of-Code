from pathlib import Path
from typing import List, Dict, Callable, Tuple

from Day_17.const import DAY, INPUT_FILE_NAME
from Day_17.const import EXAMPLE_INPUT_FILE_NAME_PART_2 as EXAMPLE_INPUT_FILE_NAME
from Day_17.load_input import load_input
from utils.solve import test, solve

def example_loop_func(registers: Dict[str, int]) -> Tuple[Dict[str, int], List[str]]:
    registers = {
        "A": registers["A"] >> 3,
        "B": 0,
        "C": 0,
    }
    output = [registers["A"] % 8]

    return registers, output
    
def loop_func(registers: Dict[str, int]) -> Dict[str, int]:
    B_intermediary = (registers["A"] % 8) ^ 3
    C = registers["A"] >> B_intermediary
    registers = {
        "A": registers["A"] >> 3,
        "B": B_intermediary ^ 5 ^ C,
        "C": C,
    }
    output = [registers["B"] % 8]

    return registers, output

def run_program(registers: Dict[str, int], loop_func: Callable[[Dict[str, int]], Tuple[Dict[str, int], List[str]]]) -> List[int]:
    output = []
    while registers["A"]:
        registers, loop_output = loop_func(registers)
        output.extend(loop_output)
    return output

def solution(registers: Dict[str, int], loop_func: Callable[[Dict[str, int]], Tuple[Dict[str, int], List[str]]]) -> str:
    output = run_program(registers, loop_func)
    return ",".join([str(x) for x in output])

if __name__ == "__main__":
    example_registers, example_program = load_input(Path(f"Day_{DAY:02d}/{EXAMPLE_INPUT_FILE_NAME}"))
    expected_answer = "5,7,3,0"
    test(expected_answer, solution, example_registers, example_loop_func)
    
    registers, program = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))
    solve(solution, registers, loop_func)