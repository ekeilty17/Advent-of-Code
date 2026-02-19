from pathlib import Path
from typing import List, Tuple, Dict
import string

from Day_05.const import DAY, EXAMPLE_INPUT_FILE_NAME, INPUT_FILE_NAME
from Day_05.load_input import load_input
from utils.solve import test, solve

MATCHES = {None: None}
MATCHES.update({lower: lower.upper() for lower in string.ascii_lowercase})
MATCHES.update({upper: upper.lower() for upper in string.ascii_uppercase})

def is_match(e1: str, e2: str) -> bool:
    return MATCHES[e1] == e2

def reduce_polymer_slow(polymer: List[str]) -> List[str]:
    polymer.append(None)        # easier way to deal with the edge case of the last element
    
    i = 0
    while i < len(polymer)-1:
        if is_match(polymer[i], polymer[i+1]):
            polymer = polymer[:i] + polymer[i+2:]       # destroy `polymer[i]` and `polymer[i+1]`
            i -= 1                                      # check for match on previous index
        else:
            i += 1

    return polymer[:-1]

def reduce_polymer(polymer: List[str]) -> List[str]:
    reduced_polymer = []

    for unit in polymer:
        if len(reduced_polymer) and is_match(reduced_polymer[-1], unit):
            reduced_polymer.pop()       # destroy `reduced_polymer[-1]` and `unit`
        else:
            reduced_polymer.append(unit)

    return reduced_polymer

def solution(polymer: str) -> int:
    polymer = list(polymer)
    return len(reduce_polymer(polymer))

if __name__ == "__main__":
    example_polymer = load_input(Path(f"Day_{DAY:02d}/{EXAMPLE_INPUT_FILE_NAME}"))
    expected_answer = 10
    test(expected_answer, solution, example_polymer)

    polymer = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))
    solve(solution, polymer)