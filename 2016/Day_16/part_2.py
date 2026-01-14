from Day_16.part_1 import solution as part_1_solution
from utils.solve import solve

if __name__ == "__main__":
    init_state = "01111010110010011"
    checksum_length = 35651584
    solve(part_1_solution, init_state, checksum_length)