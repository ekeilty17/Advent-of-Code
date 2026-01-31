from pathlib import Path
from typing import List, Tuple, Dict

from Day_25.const import DAY, INPUT_FILE_NAME
from Day_12.load_input import load_input
from Day_12.opcodes import OPCODES
from utils.solve import test, solve

def compile(registers: Dict[str, int], instructions: List[Tuple[str, List[int|str]]], N: int=10) -> Tuple[Dict[str, int], List[int]]:
    output = []
    
    # Obviously I can't simulate an infinite loop, so the variable N
    # defines the number of times the `while True` runs

    infinite_loop_counter = 0
    pc = 0
    while pc < len(instructions) and infinite_loop_counter < N:
        if pc == len(instructions) - 1:
            infinite_loop_counter += 1

        opcode, operands = instructions[pc]
        
        if opcode == "out":
            x = operands[0]
            x = registers[x] if x in registers else x
            output.append(x)
            pc_step = 1
        else:
            pc_step = OPCODES[opcode](registers, *operands)
        
        pc_step = 1 if pc_step is None else pc_step
        pc += pc_step
    
    return registers, output

def simulate(instructions: List[Tuple[str, List[int|str]]]) -> List[int]:
    registers = {"a": 158, "b": 0, "c": 0, "d": 0}
    registers, output = compile(registers, instructions)
    return output

if __name__ == "__main__":
    instructions = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))
    output = simulate(instructions)
    print(output)