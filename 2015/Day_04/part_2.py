from pathlib import Path

from Day_04.const import DAY, INPUT_FILE_NAME
from Day_04.load_input import load_input
from Day_04.part_1 import solution

if __name__ == "__main__":
    
    secret_key = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))

    num_leading_zeros = 6

    total = solution(secret_key, num_leading_zeros)
    print("Puzzle Answer:", total)