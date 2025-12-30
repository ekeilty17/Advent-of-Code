from pathlib import Path
from typing import List, Tuple, Dict, Set

from Day_23.const import DAY, EXAMPLE_INPUT_FILE_NAME, INPUT_FILE_NAME
from Day_23.load_input import load_input
from Day_23.part_1 import get_adjacency_list
from utils.test import test

def clique_induction(
        nodes: Set[int], 
        adj: Dict[str, Set[str]],
        cliques_n: Set[Tuple[str, ...]]
    ) -> Set[Tuple[str, ...]]:
    
    cliques_n_plus_1 = set([])
    for clique in cliques_n:
        for node in nodes:
            if node in clique:
                continue
            
            if all(u in adj[node] for u in clique):
                new_clique = node, *clique
                cliques_n_plus_1.add(tuple(sorted(new_clique)))
    
    return cliques_n_plus_1

def solution(connections: List[Tuple[str, str]]) -> str:
    adj = get_adjacency_list(connections)
    nodes = adj.keys()
    
    CLIQUES = []
    CLIQUES.append(set(tuple([node]) for node in nodes))
    while CLIQUES[-1]:
        CLIQUES.append( clique_induction(nodes, adj, CLIQUES[-1]) )

    return ",".join(sorted(CLIQUES[-2].pop()))

if __name__ == "__main__":
    
    example_connections = load_input(Path(f"Day_{DAY:02d}/{EXAMPLE_INPUT_FILE_NAME}"))
    connections = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))

    expected_answer = "co,de,ka,ta"
    test(expected_answer, solution, example_connections)

    total = solution(connections)
    print("Puzzle Answer:", total)