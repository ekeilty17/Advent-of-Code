from pathlib import Path
from typing import List, Tuple, Dict, Set, TypeAlias

from Day_24.const import DAY, EXAMPLE_INPUT_FILE_NAME, INPUT_FILE_NAME
from Day_24.load_input import load_input
from Day_24.part_1 import construct_graph, get_all_paths, get_bridge_strength
from utils.solve import test, solve

Node: TypeAlias = Tuple[int, int]

def solution(components: List[Tuple[int, int]]) -> int:
    start, adj = construct_graph(components)
    all_paths = get_all_paths(components, adj, start)
    all_bridges = [bridge[1:] for bridge in all_paths]        # remove pseudo-start

    # longest bridge, breaking ties by strength
    longest_bridge = max(all_bridges, key=lambda bridge: (len(bridge), get_bridge_strength(components, bridge)))
    return get_bridge_strength(components, longest_bridge)

if __name__ == "__main__":
    example_components = load_input(Path(f"Day_{DAY:02d}/{EXAMPLE_INPUT_FILE_NAME}"))
    expected_answer = 19
    test(expected_answer, solution, example_components)

    components = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))
    solve(solution, components)