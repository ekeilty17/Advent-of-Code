from pathlib import Path
from typing import List, Tuple

from Day_07.const import DAY, INPUT_FILE_NAME
from Day_07.load_input import load_input
from Day_07.part_1 import parse_gate, compute_circuit

def solution(instructions: List[Tuple[str, str]], target_wire: str, override_wire: str) -> int:
    gate_by_output_wire = {
        output_wire: parse_gate(gate) for gate, output_wire in instructions
    }
    wire_signals_part_1 = compute_circuit(gate_by_output_wire)
    
    # override `override_wire` with the signal from `target_wire`
    gate_by_output_wire[override_wire] = {
        "operation": "assign",
        "operands": [wire_signals_part_1[target_wire]]
    }
    wire_signals = compute_circuit(gate_by_output_wire)
    return wire_signals[target_wire]

if __name__ == "__main__":
    
    instructions = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))

    target_wire = "a"
    override_wire = "b"
    total = solution(instructions, target_wire, override_wire)
    print("Puzzle Answer:", total)