from pathlib import Path
from typing import List, Tuple, Dict

from Day_18.const import DAY, INPUT_FILE_NAME
from Day_18.const import EXAMPLE_INPUT_FILE_NAME_PART_2 as EXAMPLE_INPUT_FILE_NAME
from Day_18.load_input import load_input
from Day_18.opcodes import OPCODES
from utils.solve import test, solve


def compile(
    instructions: List[Tuple[str, List[int|str]]], 
    registers: Dict[str, int],
    output: List[int],
    output_other: List[int],
    pc: int
    ) -> bool:
    
    while pc < len(instructions):
        opcode, operands = instructions[pc]

        if opcode == "snd":
            x = operands[0]
            x = registers.get(x, 0) if isinstance(x, str) else x
            output.append(x)
            return pc+1, False            # context-switch to other program
        
        elif opcode == "rcv":
            if len(output_other) == 0:
                return pc, True           # terminate
            
            x = operands[0]
            registers[x] = output_other.pop(0)
            pc_step = 1
        else:
            pc_step = OPCODES[opcode](registers, *operands)
        
        pc_step = 1 if pc_step is None else pc_step
        pc += pc_step
    
    return pc, True                     # terminate

def solution(instructions: List[Tuple[str, List[int|str]]]) -> int:
    registers_0 = {"p": 0}
    output_0 = []
    pc_0 = 0
    halted_0 = False
    num_program_0_sends = 0

    registers_1 = {"p": 1}
    output_1 = []
    pc_1 = 0
    halted_1 = False
    num_program_1_sends = 0

    while not (halted_0 and halted_1):
        pc_0, halted_0 = compile(instructions, registers_0, output_0, output_1, pc_0)
        pc_1, halted_1 = compile(instructions, registers_1, output_1, output_0, pc_1)
        
        if not halted_0:
            num_program_0_sends += 1
        if not halted_1:
            num_program_1_sends += 1

    return num_program_1_sends

if __name__ == "__main__":
    example_instructions = load_input(Path(f"Day_{DAY:02d}/{EXAMPLE_INPUT_FILE_NAME}"))
    expected_answer = 3
    test(expected_answer, solution, example_instructions)

    instructions = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))
    solve(solution, instructions)