from pathlib import Path

from Day_04.const import DAY, INPUT_FILE_NAME
from Day_04.load_input import load_input
from Day_04.part_1 import solution
from utils.solve import solve

if __name__ == "__main__":
    num_leading_zeros = 6
    secret_key = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))
    solve(solution, secret_key, num_leading_zeros)