from pathlib import Path
from typing import List

from Day_11.const import DAY, EXAMPLE_INPUT_FILE_NAME, INPUT_FILE_NAME
from Day_11.load_input import load_input
from utils.solve import test, solve

def apply_stone_rules(stone: int) -> List[int]:
    stone_str = str(stone)
    if stone == 0:
        return [1]
    elif len(stone_str) % 2 == 0:
        left = stone_str[:len(stone_str)//2]
        right = stone_str[len(stone_str)//2:]
        return [int(left), int(right)]
    else:
        return [stone * 2024]

def blink(stones: List[int]) -> List[int]:
    updated_stones = []

    for stone in stones:
        updated_stones.extend(apply_stone_rules(stone))

    return updated_stones

def solution(stones: List[int], num_blinks: int) -> int:
    for _ in range(num_blinks):
        stones = blink(stones)
    
    return len(stones)

if __name__ == "__main__":
    num_blinks = 25

    example_stones = load_input(Path(f"Day_{DAY:02d}/{EXAMPLE_INPUT_FILE_NAME}"))
    expected_answer = 55312
    test(expected_answer, solution, example_stones, num_blinks)

    stones = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))
    solve(solution, stones, num_blinks)