from pathlib import Path
from typing import List

from Day_22.const import DAY, EXAMPLE_INPUT_FILE_NAME, INPUT_FILE_NAME
from Day_22.load_input import load_input
from utils.test import test

def mix(n: int, m: int) -> int:
    return n ^ m

def prune(n: int) -> int:
    return n % 16777216

def compute_next_secret_number(secret_number: int) -> int:
    result = secret_number
    result = mix(result, result*64)
    result = prune(result)
    result = mix(result, result//32)
    result = prune(result)
    result = mix(result, result*2048)
    result = prune(result)
    return result

def compute_secret_number_sequence(initial_secret_number: int, N: int) -> List[int]:
    secret_number_sequence = [initial_secret_number]
    secret_number = initial_secret_number
    for _ in range(N):
        secret_number = compute_next_secret_number(secret_number)
        secret_number_sequence.append(secret_number)
    return secret_number_sequence

def solution(secret_numbers: List[int], N: int) -> int:
    final_secret_numbers = []
    for secret_number in secret_numbers:
        secret_number_sequence = compute_secret_number_sequence(secret_number, N)
        final_secret_numbers.append(secret_number_sequence[-1])
    return sum(final_secret_numbers)

if __name__ == "__main__":
    
    small_example_secret_numbers = [123]
    example_secret_numbers = load_input(Path(f"Day_{DAY:02d}/{EXAMPLE_INPUT_FILE_NAME}"))
    secret_numbers = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))
    
    small_example_N = 10
    small_expected_answer = 5908254
    test(small_expected_answer, solution, small_example_secret_numbers, small_example_N)

    example_N = 2000
    expected_answer = 37327623
    test(expected_answer, solution, example_secret_numbers, example_N)

    N = 2000
    total = solution(secret_numbers, N)
    print("Puzzle Answer:", total)