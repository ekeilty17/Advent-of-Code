from pathlib import Path
from typing import List, Dict, Tuple

from Day_24.const import DAY, SMALL_EXAMPLE_INPUT_FILE_NAME, INPUT_FILE_NAME
from Day_24.const import EXAMPLE_INPUT_FILE_NAME_PART_2 as EXAMPLE_INPUT_FILE_NAME
from Day_24.load_input import load_input
from Day_24.part_1 import propogate_wire_inputs, wire_values_to_int
from utils.solve import test, solve

def solution(wire_inputs: Dict[str, bool], gates: Dict[str, Tuple[str, str, str]]) -> int:
    wire_values = propogate_wire_inputs(wire_inputs, gates)
    wires = wire_values.keys()

    x_wires = reversed(sorted([wire for wire in wires if "x" in wire]))
    x = wire_values_to_int(x_wires, wire_values)

    y_wires = reversed(sorted([wire for wire in wires if "y" in wire]))
    y = wire_values_to_int(y_wires, wire_values)

    z_wires = reversed(sorted([wire for wire in wires if "z" in wire]))
    z = wire_values_to_int(z_wires, wire_values)

    print(x, y, z)

if __name__ == "__main__":
    example_wire_inputs, example_gates = load_input(Path(f"Day_{DAY:02d}/{EXAMPLE_INPUT_FILE_NAME}"))
    expected_answer = "z00,z01,z02,z05"
    test(expected_answer, solution, example_wire_inputs, example_gates)

    # wire_inputs, gates = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))
    # total = solution(wire_inputs, gates)
    # print("Puzzle Answer:", total)