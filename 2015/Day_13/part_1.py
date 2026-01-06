from pathlib import Path
from typing import List, Tuple, Dict
from itertools import permutations

from Day_13.const import DAY, EXAMPLE_INPUT_FILE_NAME, INPUT_FILE_NAME
from Day_13.load_input import load_input
from utils.test import test

def compute_total_happiness(cycle: List[str], happiness_by_people_pairs: Dict[Tuple[str, str], int]):
    total_happiness = 0
    for i in range(len(cycle)):
        n1, n2 = cycle[i], cycle[(i+1)%len(cycle)]
        total_happiness += happiness_by_people_pairs[n1, n2]
        total_happiness += happiness_by_people_pairs[n2, n1]
    return total_happiness

def solution(pairwise_happiness: List[Tuple[str, str, int]]) -> int:
    people = set([name1 for name1, _, _ in pairwise_happiness] + [name2 for _, name2, _ in pairwise_happiness])
    
    happiness_by_people_pairs = {
        (n1, n2): happiness for n1, n2, happiness in pairwise_happiness
    }

    fixed_person = people.pop()
    max_cycle = max([list(perm) + [fixed_person] for perm in permutations(people)], key=lambda cycle: compute_total_happiness(cycle, happiness_by_people_pairs))
    return compute_total_happiness(max_cycle, happiness_by_people_pairs)

if __name__ == "__main__":
    
    example_pairwise_happiness = load_input(Path(f"Day_{DAY:02d}/{EXAMPLE_INPUT_FILE_NAME}"))
    pairwise_happiness = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))


    expected_answer = 330
    test(expected_answer, solution, example_pairwise_happiness)

    total = solution(pairwise_happiness)
    print("Puzzle Answer:", total)