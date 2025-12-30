from pathlib import Path
from typing import List
import numpy as np

from Day_22.const import DAY, EXAMPLE_INPUT_FILE_NAME, INPUT_FILE_NAME
from Day_22.load_input import load_input
from Day_22.part_1 import compute_secret_number_sequence
from utils.test import test

def solution(secret_numbers: List[int], N: int) -> int:
    sequences = np.array([compute_secret_number_sequence(secret_number, N-1) for secret_number in secret_numbers])
    prices = sequences % 10
    price_changes = prices[:, 1:] - prices[:, :-1]
    
    total_price_by_consecutive_change = {}
    for i in range(price_changes.shape[0]):
        
        # Compute the price value on the first occurance of every consecutive sequence of 4 price changes
        row_prices_by_consecutive_change = {}
        for j in range(price_changes.shape[1]-4):
            consecutive_change = tuple(price_changes[i, j:j+4])
            price = prices[i, j+4]
            if consecutive_change not in row_prices_by_consecutive_change:       # we only care about the first occurance
                row_prices_by_consecutive_change[consecutive_change] = price

        # Merge these into the total price for each consecutive sequence
        for consecutive_change, price in row_prices_by_consecutive_change.items():
            if consecutive_change in total_price_by_consecutive_change:
                total_price_by_consecutive_change[consecutive_change] += price
            else:
                total_price_by_consecutive_change[consecutive_change] = price

    max_consecutive_change, max_price = max(total_price_by_consecutive_change.items(), key=lambda t: t[1])
    return max_price

if __name__ == "__main__":
    
    very_small_example_secret_numbers = [123]
    small_example_secret_numbers = [1, 2, 3, 2024]
    example_secret_numbers = load_input(Path(f"Day_{DAY:02d}/{EXAMPLE_INPUT_FILE_NAME}"))
    secret_numbers = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))
    
    very_small_example_N = 10
    very_small_expected_answer = 6
    test(very_small_expected_answer, solution, very_small_example_secret_numbers, very_small_example_N)

    small_example_N = 2000
    small_expected_answer = 23
    test(small_expected_answer, solution, small_example_secret_numbers, small_example_N)

    example_N = 2000
    expected_answer = 24
    test(expected_answer, solution, example_secret_numbers, example_N)

    N = 2000
    total = solution(secret_numbers, N)
    print("Puzzle Answer:", total)