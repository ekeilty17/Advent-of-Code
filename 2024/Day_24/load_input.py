from pathlib import Path
from typing import List, Tuple, Dict

def load_input(input_path: Path) -> Tuple[Dict[str, bool], Dict[str, Tuple[str, str, str]]]:
    contents = input_path.read_text()

    wire_inputs, gates = contents.split("\n\n")
    wire_inputs = dict([parse_wire_input(wire_input) for wire_input in wire_inputs.splitlines()])
    gates = dict([parse_gate(gate) for gate in gates.splitlines()])

    return wire_inputs, gates

def parse_wire_input(wire_input_str: str) -> Tuple[str, bool]:
    input_wire, input_value = wire_input_str.split(": ")
    return input_wire, bool(int(input_value))

def parse_gate(gate_str: str) -> Tuple[str, Tuple[str, str, str]]:
    gate_input_str, output_wire = gate_str.split(" -> ")
    LHS_wire, operation, RHS_wire = gate_input_str.split(" ")
    return output_wire, (LHS_wire, operation, RHS_wire)