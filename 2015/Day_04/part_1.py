from pathlib import Path
import hashlib

from Day_04.const import DAY, EXAMPLE_INPUT_FILE_NAME, INPUT_FILE_NAME
from Day_04.load_input import load_input
from utils.test import test

def MD5(secret_key: str) -> str:
    return hashlib.md5(secret_key.encode()).hexdigest()

def solution(secret_key: str, num_leading_zeros: int) -> int:
    
    num = 0
    hashed_key = ""
    leading_zeros = "0" * num_leading_zeros
    while hashed_key[:num_leading_zeros] != leading_zeros:
        num += 1
        hashed_key = MD5(f"{secret_key}{num}")
    
    return num

if __name__ == "__main__":
    
    example_secret_key = load_input(Path(f"Day_{DAY:02d}/{EXAMPLE_INPUT_FILE_NAME}"))
    secret_key = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))

    num_leading_zeros = 5

    expected_answer = 1048970
    test(expected_answer, solution, example_secret_key, num_leading_zeros)

    total = solution(secret_key, num_leading_zeros)
    print("Puzzle Answer:", total)