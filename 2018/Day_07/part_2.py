from pathlib import Path
from typing import List, Tuple, Dict, Set
import string

from Day_07.const import DAY, EXAMPLE_INPUT_FILE_NAME, INPUT_FILE_NAME
from Day_07.load_input import load_input
from Day_07.part_1 import build_graph, get_in_degrees
from utils.solve import test, solve

def modified_topological_sort(nodes: List[str], adj: Dict[str, Set[str]], num_workers: int, startup_duration: int) -> int:
    in_degree = get_in_degrees(nodes, adj)

    queue = [node for node in in_degree if in_degree[node] == 0]
    workers = [None] * num_workers
    
    execution_time_map = {letter: startup_duration + index for index, letter in enumerate(string.ascii_uppercase)}

    total_seconds = 0
    execution_order = []

    while queue or not all(worker is None for worker in workers):
        total_seconds += 1

        # Update process times within each worker
        for i in range(len(workers)):
            if workers[i] is not None:
                node, seconds_remaining = workers[i]

                # decrement process time
                if seconds_remaining != 0:
                    workers[i] = (node, seconds_remaining-1)
                    continue
                
                # Process is finished with the worker, so free it
                workers[i] = None

                # Toposort update to add newly available processes to the queue
                execution_order.append(node)
                for neighbor in adj[node]:
                    in_degree[neighbor] -= 1
                    if in_degree[neighbor] == 0:
                        queue.append(neighbor)
                    

        # Add new processes if workers are empty
        for i in range(len(workers)):
            if queue and workers[i] is None:
                queue = list(sorted(queue, reverse=True))
                node = queue.pop()
                workers[i] = (node, execution_time_map[node])

    return total_seconds - 1

def solution(instruction_dependencies: List[Tuple[str, str]], num_workers: int, startup_duration: int) -> int:
    nodes, adj = build_graph(instruction_dependencies)
    return modified_topological_sort(nodes, adj, num_workers, startup_duration)

if __name__ == "__main__":
    example_instruction_dependencies = load_input(Path(f"Day_{DAY:02d}/{EXAMPLE_INPUT_FILE_NAME}"))
    example_num_workers = 2
    example_startup_duration = 0
    expected_answer = 15
    test(expected_answer, solution, example_instruction_dependencies, example_num_workers, example_startup_duration)

    instruction_dependencies = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))
    num_workers = 5
    startup_duration = 60
    solve(solution, instruction_dependencies, num_workers, startup_duration)