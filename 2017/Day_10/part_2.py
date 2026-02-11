from pathlib import Path
from typing import List

from Day_10.const import DAY, INPUT_FILE_NAME
from Day_10.load_input import load_input
from Day_10.part_1 import knot_hash_round
from utils.solve import test, solve

def compute_dense_hash(numbers: List[int], num_buckets: int) -> List[int]:
    bucket_size = len(numbers) // num_buckets
    
    dense_numbers = []
    for i in range(0, len(numbers), bucket_size):
        xor = 0
        for n in numbers[i:i+bucket_size]:
            xor ^= n
        dense_numbers.append(xor)
    
    return dense_numbers

def knot_hash(string: str) -> str:
    N = 256
    
    lengths = [ord(n) for n in string]
    lengths.extend([17, 31, 73, 47, 23])
    
    i = skip = 0
    numbers = list(range(N))
    for _ in range(64):
        numbers, i, skip = knot_hash_round(numbers, lengths, i, skip)

    dense_numbers = compute_dense_hash(numbers, 16)

    hex_string = ''.join([format(n, '02x') for n in dense_numbers])
    return hex_string

def solution(lengths: str) -> str:
    return knot_hash(lengths)


if __name__ == "__main__":
    examples = [
        ("", "a2582a3a0e66e6e86e3812dcb672a272"),
        ("AoC 2017", "33efeb34ea91902bb2f59c9920caa6cd"),
        ("1,2,3", "3efbe78a8d82f29979031a4aa0b16a9d"),
        ("1,2,4", "63960835bcdc130f0b66d7ff4f6a5a8e")
    ]
    for example_lengths, expected_answer in examples:
        test(expected_answer, solution, example_lengths)

    lengths = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))
    solve(solution, lengths)