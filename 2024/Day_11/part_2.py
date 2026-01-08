from pathlib import Path
from typing import List, Dict, Tuple, TypeAlias

from Day_11.const import DAY, EXAMPLE_INPUT_FILE_NAME, INPUT_FILE_NAME
from Day_11.load_input import load_input
from Day_11.part_1 import apply_stone_rules
from Day_11.part_1 import solution as part_1_solution
from utils.solve import test, solve

MemoizationDict: TypeAlias = Dict[Tuple[int, int], int]

def blink_single_stone(memo: MemoizationDict, stone: int, blinks_remaining: int) -> Tuple[int, MemoizationDict]:
    if blinks_remaining == 0:
        return 1, memo
    if (stone, blinks_remaining) in memo:
        return memo[(stone, blinks_remaining)], memo
    
    updated_stones = apply_stone_rules(stone)
    
    total = 0
    for stone in updated_stones:
        stone_sub_total, memo = blink_single_stone(memo, stone, blinks_remaining-1)
        memo[(stone, blinks_remaining-1)] = stone_sub_total
        total += stone_sub_total
    
    return total, memo

def solution(stones: List[int], num_blinks: int) -> int:
    # return part_1_solution(stones, num_blinks)        # takes way too long, even the example doesn't finish
    memo = {}
    total = 0
    for stone in stones:
        stone_total, memo = blink_single_stone(memo, stone, num_blinks)
        total += stone_total
    return total

if __name__ == "__main__":
    num_blinks = 75

    example_stones = load_input(Path(f"Day_{DAY:02d}/{EXAMPLE_INPUT_FILE_NAME}"))
    expected_answer = 65601038650482
    test(expected_answer, solution, example_stones, num_blinks)

    stones = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))
    solve(solution, stones, num_blinks)