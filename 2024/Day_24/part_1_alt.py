from pathlib import Path
from typing import List, Tuple, Dict

from Day_24.const import DAY, SMALL_EXAMPLE_INPUT_FILE_NAME, INPUT_FILE_NAME
from Day_24.const import EXAMPLE_INPUT_FILE_NAME_PART_1 as EXAMPLE_INPUT_FILE_NAME
from Day_24.load_input import load_input
from utils.solve import test, solve

class BinaryTree:

    def __init__(self, wire, operation, value=None):
        self.wire = wire
        self.operation = operation
        self.value = value

        self.left = None
        self.right = None

def compute_binary_operation(LHS: bool, operation: str, RHS: bool) -> bool:
    if operation == "AND":
        return LHS & RHS
    if operation == "OR":
        return LHS | RHS
    if operation == "XOR":
        return LHS ^ RHS
    
    raise ValueError(f"Unexpected value for operation - '{operation}'")

def propogate_wire_inputs(wire_inputs: Dict[str, bool], gates: Dict[str, Tuple[str, str, str]]) -> Dict[str, bool]:
    wire_nodes = {
        **{wire: BinaryTree(wire, None, value) for wire, value in wire_inputs.items()},
        **{wire: BinaryTree(wire, operation, None) for wire, (_, operation, _) in gates.items()},
        
    }

    wire_values = wire_inputs.copy()
    
    def dsf(output_wire, LHS_wire, operation, RHS_wire) -> None:
        if output_wire in wire_values:
            return
        
        if LHS_wire not in wire_values:
            dsf(LHS_wire, *gates[LHS_wire])
        if RHS_wire not in wire_values:
            dsf(RHS_wire, *gates[RHS_wire])
        
        gate_output = compute_binary_operation(wire_values[LHS_wire], operation, wire_values[RHS_wire])
        wire_values[output_wire] = gate_output

    for output_wire, (LHS_wire, operation, RHS_wire) in gates.items():
        dsf(output_wire, LHS_wire, operation, RHS_wire)
    
    return wire_values

def wire_values_to_int(wires: List[str], wire_values: Dict[str, bool]) -> int:
    binary_str = "".join("1" if wire_values[wire] else "0" for wire in wires)
    return int(binary_str, 2)

def solution(wire_inputs: Dict[str, bool], gates: Dict[str, Tuple[str, str, str]]) -> int:
    wire_values = propogate_wire_inputs(wire_inputs, gates)
    wires = wire_values.keys()
    z_wires = reversed(sorted([wire for wire in wires if "z" in wire]))
    return wire_values_to_int(z_wires, wire_values)

if __name__ == "__main__":
    small_example_wire_inputs, small_example_gates = load_input(Path(f"Day_{DAY:02d}/{SMALL_EXAMPLE_INPUT_FILE_NAME}"))
    small_expected_answer = 4
    test(small_expected_answer, solution, small_example_wire_inputs, small_example_gates)

    example_wire_inputs, example_gates = load_input(Path(f"Day_{DAY:02d}/{EXAMPLE_INPUT_FILE_NAME}"))
    expected_answer = 2024
    test(expected_answer, solution, example_wire_inputs, example_gates)

    wire_inputs, gates = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))
    solve(solution, wire_inputs, gates)