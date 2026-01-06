from pathlib import Path
from typing import List, Tuple

from Day_13.const import DAY, INPUT_FILE_NAME
from Day_13.load_input import load_input
from Day_13.part_1 import solution as part_1_solution

def solution(pairwise_happiness: List[Tuple[str, str, int]]) -> int:
    people = set([name1 for name1, _, _ in pairwise_happiness] + [name2 for _, name2, _ in pairwise_happiness])
    for person in people:
        pairwise_happiness.append(("Me", person, 0))
        pairwise_happiness.append((person, "Me", 0))

    return part_1_solution(pairwise_happiness)

if __name__ == "__main__":
    
    pairwise_happiness = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))

    total = solution(pairwise_happiness)
    print("Puzzle Answer:", total)