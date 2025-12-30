from pathlib import Path
from typing import List, Dict, Any

from Day_17.const import DAY, INPUT_FILE_NAME
from Day_17.const import EXAMPLE_INPUT_FILE_NAME_PART_1 as EXAMPLE_INPUT_FILE_NAME
from Day_17.load_input import load_input
from Day_17.opcodes import OPCODES_FUNCS
from utils.test import test

def execute_instruction(opcode: int, operand: int, registers: Dict[str, int]) -> Dict[str, Any]:
    result = OPCODES_FUNCS[opcode](operand, registers)
    return result if result else {}

def run_program(registers: Dict[str, int], program: List[int]) -> List[int]:
    instruction_pointer = 0
    output = []
    while instruction_pointer < len(program):
        opcode = program[instruction_pointer]
        operand = program[instruction_pointer+1]
        
        result = execute_instruction(opcode, operand, registers)
        instruction_pointer += 2

        if result.get("instruction_pointer") is not None:
            instruction_pointer = result["instruction_pointer"]

        if result.get("output") is not None:
            output.append(result["output"])
    
    return output

def solution(registers: Dict[str, int], program: List[int]) -> str:
    output = run_program(registers, program)
    return ",".join([str(x) for x in output])

if __name__ == "__main__":
    
    example_registers, example_program = load_input(Path(f"Day_{DAY:02d}/{EXAMPLE_INPUT_FILE_NAME}"))
    registers, program = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))

    expected_answer = "4,6,3,5,6,3,5,2,1,0"
    test(expected_answer, solution, example_registers, example_program)

    total = solution(registers, program)
    print("Puzzle Answer:", total)