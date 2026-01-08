from pathlib import Path
from typing import List, Tuple

from Day_05.const import DAY, EXAMPLE_INPUT_FILE_NAME, INPUT_FILE_NAME
from Day_05.load_input import load_input
from Day_05.graph import Graph
from utils.solve import test, solve

def get_median(lst):
    return lst[len(lst)//2]

def is_sequence_match(seq1, seq2):
    return all(x1 == x2 for x1, x2 in zip(seq1, seq2))

def solution(page_ordering_rules: List[Tuple[int, int]], page_sequences: List[List[int]]) -> int:
    G = Graph()    
    for edge in page_ordering_rules:
        G.add_edge(edge)

    count = 0
    for page_sequence in page_sequences:
        subG = G.get_subgraph(page_sequence)
        correct_page_sequence = subG.topological_sort()
        if is_sequence_match(page_sequence, correct_page_sequence):
            count += get_median(page_sequence)

    return count

if __name__ == "__main__":
    example_page_ordering_rules, example_page_sequences = load_input(Path(f"Day_{DAY:02d}/{EXAMPLE_INPUT_FILE_NAME}"))
    expected_answer = 143
    test(expected_answer, solution, example_page_ordering_rules, example_page_sequences)

    page_ordering_rules, page_sequences = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))
    solve(solution, page_ordering_rules, page_sequences)