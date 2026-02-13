from pathlib import Path
from typing import List, Tuple, Dict, Set, TypeAlias

from Day_24.const import DAY, EXAMPLE_INPUT_FILE_NAME, INPUT_FILE_NAME
from Day_24.load_input import load_input
from utils.solve import test, solve

Node: TypeAlias = Tuple[int, int]

def construct_graph(components: List[Tuple[int, int]]) -> Tuple[Node, Dict[Node, int], Dict[Node, Set[Node]]]:
    
    adj = {i: set([]) for i in range(len(components))}
    for i in range(len(components)):
        component_i = components[i]
        for j in range(i+1, len(components)):
            component_j = components[j]
            if any(pins in component_i for pins in component_j):
                adj[i].add(j)
                adj[j].add(i)
    
    # Pseudo-start which connects to all 0 pins
    components_with_0_pins = [i for i, component in enumerate(components) if 0 in component]
    start = "PSEUDOSTART"
    adj[start] = set(components_with_0_pins)

    return start, adj

def get_all_paths(components: List[Tuple[int, int]], adj: Dict[Node, Set[Node]], start: Node) -> List[List[Node]]:
    all_paths = []
    stack = [(start, 0, [])]

    while stack:
        node, open_pin, path = stack.pop()
        path.append(node)

        finished_path = True
        for neighbor in adj[node]:
            if neighbor in path:
                continue
            
            p1, p2 = components[neighbor]
            if open_pin != p1 and open_pin != p2:
                continue
            
            finished_path = False
            neighbor_open_pin = p1 if open_pin == p2 else p2
            stack.append( (neighbor, neighbor_open_pin, list(path)) )

        if finished_path:
            all_paths.append(path)

    return all_paths

def get_bridge_strength(components: List[Tuple[int, int]], bridge: List[int]) -> int:
    return sum([sum(components[i]) for i in bridge])

def solution(components: List[Tuple[int, int]]) -> int:
    start, adj = construct_graph(components)
    all_paths = get_all_paths(components, adj, start)
    all_bridges = [bridge[1:] for bridge in all_paths]        # remove pseudo-start
    max_strength = max([get_bridge_strength(components, bridge) for bridge in all_bridges])
    return max_strength

if __name__ == "__main__":
    example_components = load_input(Path(f"Day_{DAY:02d}/{EXAMPLE_INPUT_FILE_NAME}"))
    expected_answer = 31
    test(expected_answer, solution, example_components)

    components = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))
    solve(solution, components)