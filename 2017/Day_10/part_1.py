from pathlib import Path
from typing import List, Any, Tuple

from Day_10.const import DAY, EXAMPLE_INPUT_FILE_NAME, INPUT_FILE_NAME
from Day_10.load_input import load_input
from utils.solve import test, solve

def reverse_at_index(lst: List[Any], start: int, length: int):
    if length <= 1:
        return 
    
    for k in range(length//2):
        a = (start+k) % len(lst)
        b = (start+length-1-k) % len(lst)
        lst[a], lst[b] = lst[b], lst[a]

def knot_hash_round(lst: List[Any], lengths: List[int], i: int=0, skip: int=0) -> Tuple[List[int], int, int]:

    for length in lengths:
        reverse_at_index(lst, i, length)
        i += length + skip
        i %= len(lst)
        skip += 1

    return lst, i, skip

def solution(N:int, lengths: str) -> int:
    lengths = [int(x.strip()) for x in lengths.split(",")]
    numbers, _, _ = knot_hash_round(list(range(N)), lengths)
    return numbers[0] * numbers[1]

if __name__ == "__main__":
    example_N = 5
    example_lengths = load_input(Path(f"Day_{DAY:02d}/{EXAMPLE_INPUT_FILE_NAME}"))
    expected_answer = 12
    test(expected_answer, solution, example_N, example_lengths)

    N = 256
    lengths = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))
    solve(solution, N, lengths)