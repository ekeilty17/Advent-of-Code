from pathlib import Path
from typing import List
import numpy as np
from numpy.typing import NDArray

from Day_03.const import DAY, EXAMPLE_INPUT_FILE_NAME, INPUT_FILE_NAME
from Day_03.load_input import load_input
from utils.test import test

def compute_joltage(ordered_batteries) -> int:
    joltage = 0
    for battery in ordered_batteries:
        joltage = 10 * joltage + battery
    return joltage

def get_max_joltage_helper(bank: NDArray[np.int64], n: int) -> NDArray[np.bool_]:
    included = np.zeros_like(bank, dtype=bool)

    # Some base cases
    if n == 0:
        return np.array([])
    if n == 1:
        max_index = np.argmax(bank)
        included[max_index] = True
        return included
    if n >= len(bank):
        included[:] = True
        return included

    # pre-compute indexes of each battery for speed
    battery_indexes = {battery: [] for battery in range(1, 10)}
    for index, battery in enumerate(bank):
        battery_indexes[battery].append(index)
    
    # iterate from highest batter to smallest
    for battery in reversed(range(1, 10)):
        if np.sum(included) >= n:
            return included
        
        indexes = battery_indexes[battery]
        if not indexes:
            continue
        
        # we want everything to the right of the left-most index, in maximized order
        # the left-most maximum digit is always included
        min_index = min(indexes)
        included[min_index] = True

        # Edge Case: the max digit is the last digit
        if min_index == len(bank)-1:
            continue

        # otherwise, we recurse on the RHS
        bank_LHS = bank[:min_index+1]
        included_LHS = included[:min_index+1]
        bank_RHS = bank[min_index+1:]

        included_RHS = get_max_joltage_helper(bank_RHS, n - np.sum(included_LHS))
        included = np.concatenate([included_LHS, included_RHS])
    
    return included


def get_max_joltage(bank: List[int], n: int) -> int:
    
    if n == 0:
        return 0
    if n == 1:
        return max(bank)

    bank = np.array(bank)
    included = get_max_joltage_helper(bank, n)
    return bank[included]
    

def solution(banks: List[List[int]]):
    total_joltage = 0
    for bank in banks:
        ordered_batteries = get_max_joltage(bank, 12)
        max_joltage = compute_joltage(ordered_batteries)
        total_joltage += max_joltage

    return total_joltage

if __name__ == "__main__":
    
    example_banks = load_input(Path(f"Day_{DAY:02d}/{EXAMPLE_INPUT_FILE_NAME}"))
    banks = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))

    expected_answer = 3121910778619
    test(expected_answer, solution, example_banks)

    total = solution(banks)
    print("Puzzle Answer:", total)