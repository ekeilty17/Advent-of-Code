from pathlib import Path
from typing import List, Tuple, Dict

def load_input(input_path: Path) -> Tuple[Dict[str, int], List[int]]:
    contents = input_path.read_text()

    registers, program = contents.split("\n\n")
    registers = dict([parse_register(register) for register in registers.splitlines()])
    program = parse_program(program)
    
    return registers, program

def parse_register(register_str: str) -> Tuple[str, int]:
    return register_str[len("Register X")-1], int(register_str[len("Register X: "):])

def parse_program(program_str: str) -> List[int]:
    return [int(x) for x in program_str[len("Program: "):].split(",")]