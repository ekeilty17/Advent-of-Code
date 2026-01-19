from pathlib import Path
from typing import List, Tuple, Dict

from Day_23.const import DAY, EXAMPLE_INPUT_FILE_NAME, INPUT_FILE_NAME
from Day_23.load_input import load_input
from Day_12.opcodes import OPCODES
from utils.solve import test, solve

def tgl(registers, instructions, pc, x):
    x = registers[x] if x in registers else x
    k = (pc + x) % len(instructions)
    
    opcode, operands = instructions[k]
    if len(operands) == 1:
        toggled_opcode = "dec" if opcode == "inc" else "inc"
    else:
        toggled_opcode = "cpy" if opcode == "jnz" else "jnz"

    instructions[k] = (toggled_opcode, operands)

def compile(registers: Dict[str, int], instructions: List[Tuple[str, List[int|str]]]) -> Dict[str, int]:
    pc = 0
    while pc < len(instructions):
        opcode, operands = instructions[pc]
        
        if opcode == "tgl":
            # handle tgl instruction as an exception
            pc_step = tgl(registers, instructions, pc, *operands)
        else:
            # Use the same opcodes from Day 12
            try:
                pc_step = OPCODES[opcode](registers, *operands)
            except:
                # tgl caused an invalid instruction, so we just skip
                pc_step = 1
        
        pc_step = 1 if pc_step is None else pc_step
        pc += pc_step
    
    return registers

def solution(
        instructions: List[Tuple[str, List[int|str]]], 
        egg_register: str,
        num_eggs: int
    ) -> int:
    registers = {"a": 0, "b": 0, "c": 0, "d": 0}
    registers[egg_register] = num_eggs
    compile(registers, instructions)
    return registers[egg_register]

if __name__ == "__main__":
    egg_register = "a"

    example_instructions = load_input(Path(f"Day_{DAY:02d}/{EXAMPLE_INPUT_FILE_NAME}"))
    example_num_eggs = 0
    expected_answer = 3
    test(expected_answer, solution, example_instructions, egg_register, example_num_eggs)

    instructions = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))
    num_eggs = 7
    solve(solution, instructions, egg_register, num_eggs)