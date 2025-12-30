from pathlib import Path
from typing import List, Tuple, Dict, Set

from Day_23.const import DAY, EXAMPLE_INPUT_FILE_NAME, INPUT_FILE_NAME
from Day_23.load_input import load_input
from utils.test import test

def get_adjacency_list(edges: List[Tuple[str, str]]) -> Dict[str, Set[str]]:
    adj = {}
    for u, v in edges:
        if u in adj:
            adj[u].add(v)
        else:
            adj[u] = set([v])
            
        if v in adj:
            adj[v].add(u)
        else:
            adj[v] = set([u])
    
    return adj

def solution(connections: List[Tuple[str, str]]) -> int:
    adj = get_adjacency_list(connections)

    triples = set([])
    for u in adj:
        for v in adj[u]:
            for w in adj[v]:
                if u in adj[w]:
                    triples.add(tuple(sorted((u, v, w))))

    t_nodes = [node for node in adj.keys() if node[0] == "t"]
    t_triples = [triple for triple in triples if any(node in triple for node in t_nodes)]
    
    return len(t_triples)

if __name__ == "__main__":
    
    example_connections = load_input(Path(f"Day_{DAY:02d}/{EXAMPLE_INPUT_FILE_NAME}"))
    connections = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))

    expected_answer = 7
    test(expected_answer, solution, example_connections)

    total = solution(connections)
    print("Puzzle Answer:", total)