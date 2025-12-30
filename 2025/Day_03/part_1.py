from pathlib import Path
from typing import List

from Day_03.const import DAY, EXAMPLE_INPUT_FILE_NAME, INPUT_FILE_NAME
from Day_03.load_input import load_input
from utils.test import test

def get_max_joltage(bank: List[int]) -> int:

    max_battery = bank[0]
    max_battery_index = 0
    for i, battery in enumerate(bank):
        # we want the earliest instance of the max, so in the case of a tie, we do nothing
        if battery > max_battery:
            max_battery = battery
            max_battery_index = i
    
    # edge case: the max is at the end of the list, so we take the second max behind it
    if max_battery_index == len(bank) - 1:
        second_max_battery = max(bank[:-1])
        return 10*second_max_battery + max_battery
    
    # typical case: take the second max of everything after the max
    second_max_battery = max(bank[max_battery_index+1:])
    return 10*max_battery + second_max_battery

def solution(banks: List[List[int]]):
    total_joltage = 0
    for bank in banks:
        max_joltage = get_max_joltage(bank)
        total_joltage += max_joltage

    return total_joltage

if __name__ == "__main__":
    
    example_banks = load_input(Path(f"Day_{DAY:02d}/{EXAMPLE_INPUT_FILE_NAME}"))
    banks = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))

    expected_answer = 357
    test(expected_answer, solution, example_banks)

    total = solution(banks)
    print("Puzzle Answer:", total)