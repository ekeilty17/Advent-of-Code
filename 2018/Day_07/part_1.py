from pathlib import Path
from typing import List, Tuple, Set, Dict

from Day_07.const import DAY, EXAMPLE_INPUT_FILE_NAME, INPUT_FILE_NAME
from Day_07.load_input import load_input
from utils.solve import test, solve

def build_graph(instruction_dependencies: List[Tuple[str, str]]) -> Tuple[List[str], Dict[str, Set[str]]]:
    nodes = set([step for dependency in instruction_dependencies for step in dependency])
    adj = {node: set([]) for node in nodes}
    for u, v in instruction_dependencies:
        adj[u].add(v)
    
    return nodes, adj

def get_in_degrees(nodes: List[str], adj: Dict[str, Set[str]]) -> Dict[str, int]:
    in_degree = {node: 0 for node in nodes}
    for u, neighbors in adj.items():
        for v in neighbors:
            in_degree[v] += 1
    return in_degree

def topological_sort(nodes: List[str], adj: Dict[str, Set[str]]) -> List[str]:
    in_degree = get_in_degrees(nodes, adj)

    # Initialize queue with nodes of in-degree 0
    queue = [node for node in in_degree if in_degree[node] == 0]
    topological_order = []

    while queue:
        # Pop in alphabetical order
        queue = list(sorted(queue, reverse=True))
        node = queue.pop()

        topological_order.append(node)

        for neighbor in adj[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # Check for cycle
    if len(topological_order) != len(in_degree):
        raise RuntimeError("Graph contains a cycle. Topological sort not possible.")

    return topological_order

def solution(instruction_dependencies: List[Tuple[str, str]]) -> int:
    nodes, adj = build_graph(instruction_dependencies)
    topological_order = topological_sort(nodes, adj)
    return "".join(topological_order)

if __name__ == "__main__":
    example_instruction_dependencies = load_input(Path(f"Day_{DAY:02d}/{EXAMPLE_INPUT_FILE_NAME}"))
    expected_answer = "CABDFE"
    test(expected_answer, solution, example_instruction_dependencies)

    instruction_dependencies = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))
    solve(solution, instruction_dependencies)