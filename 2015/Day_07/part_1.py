from pathlib import Path
from typing import List, Tuple, Dict, Any
import re
from collections import deque

from Day_07.const import DAY, EXAMPLE_INPUT_FILE_NAME, INPUT_FILE_NAME
from Day_07.load_input import load_input
from utils.solve import test, solve

def parse_gate(gate: str) -> Dict[str, Any]:
    
    m = re.fullmatch(r"[A-Za-z0-9]+", gate)
    if m:
        operand = m.group(0)
        return {
            "operation": "assign",
            "operands": [operand]
        }
    
    m = re.fullmatch(r"NOT ([A-Za-z0-9]+)", gate)
    if m:
        operand = m.group(1)
        return {
            "operation": "NOT",
            "operands": [operand]
        }

    m = re.fullmatch(r"([A-Za-z0-9]+) ([A-Z]+) ([A-Za-z0-9]+)", gate)
    if m:
        operand_1 = m.group(1)
        operation = m.group(2)
        operand_2 = m.group(3)
        return {
            "operation": operation,
            "operands": [operand_1, operand_2]
        }

    raise ValueError(f"Unable to parse '{gate}'")


def execute_gate(wires: Dict[str, int], output_wire: str, operation: str, operands: List[int | str]) -> None:
    
    def resolve_operand(wires: Dict[str, int], operand: int | str) -> int:
        try:
            value = int(operand)
        except:
            value = wires[operand]
        return value
    
    def u16(x: int) -> int:
        MASK16 = 0xFFFF
        return x & MASK16
    
    OPS = {
        "assign": lambda a: a,
        "NOT": lambda a: ~a,
        "AND": lambda a, b: a & b,
        "OR": lambda a, b: a | b,
        "LSHIFT": lambda a, b: a << b,
        "RSHIFT": lambda a, b: a >> b,
    }
    if operation not in OPS:
        raise ValueError(f"Expected one of '{list(OPS.keys())}'. Instead got '{operation}'")

    operands = [resolve_operand(wires, operand) for operand in operands]
    wires[output_wire] = u16( OPS[operation](*operands) )


def get_wire_execution_order(gate_by_output_wire: Dict[str, Any]) -> List[str]:
    nodes = gate_by_output_wire.keys()
    adj = {
        output_wire: [input_wire for input_wire in gate["operands"] if input_wire in gate_by_output_wire]
        for output_wire, gate in gate_by_output_wire.items()
    }
    
    def topological_sort(nodes: List[str], adj: Dict[str, List[str]]) -> List[str]:
        
        # Initialize in-degree
        in_degree = {node: 0 for node in nodes}
        for node in nodes:
            for neighbor in adj[node]:
                in_degree[neighbor] += 1

        # Initialize queue with nodes of in-degree 0
        queue = deque([node for node in in_degree if in_degree[node] == 0])
        topological_order = []

        # Modified BFS
        while queue:
            node = queue.popleft()
            topological_order.append(node)

            for neighbor in adj[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        return topological_order

    return list(reversed(topological_sort(nodes, adj)))


def compute_circuit(gate_by_output_wire: Dict[str, Dict[str, Any]]) -> Dict[str, int]:

    wire_signals = {}
    wire_order = get_wire_execution_order(gate_by_output_wire)
    for output_wire in wire_order:
        gate = gate_by_output_wire[output_wire]
        execute_gate(wire_signals, output_wire, **gate)
    
    return wire_signals


def solution(instructions: List[Tuple[str, str]], target_wire: str) -> int:
    gate_by_output_wire = {
        output_wire: parse_gate(gate) for gate, output_wire in instructions
    }

    wire_signals = compute_circuit(gate_by_output_wire)
    return wire_signals[target_wire]

if __name__ == "__main__":
    example_instructions = load_input(Path(f"Day_{DAY:02d}/{EXAMPLE_INPUT_FILE_NAME}"))
    example_target_wire = "d"
    expected_answer = 72
    test(expected_answer, solution, example_instructions, example_target_wire)

    instructions = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))
    target_wire = "a"
    solve(solution, instructions, target_wire)