from pathlib import Path

from Day_15.const import DAY, INPUT_FILE_NAME
from Day_15.load_input import load_input
from Day_15.part_1 import solution as part_1_solution
from utils.solve import solve

if __name__ == "__main__":
    discs = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))
    discs.append( (0, 11) )
    solve(part_1_solution, discs)