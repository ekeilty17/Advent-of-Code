from Day_10.part_2 import knot_hash
from utils.solve import test, solve

def solution(key_string: str) -> int:
    total = 0
    for row_index in range(128):
        hex_string = knot_hash(f"{key_string}-{row_index}")
        row = int(hex_string, 16)
        total += row.bit_count()

    return total

if __name__ == "__main__":
    example_key_string = "flqrgnkx"
    expected_answer = 8108
    test(expected_answer, solution, example_key_string)

    key_string = "hwlqcszp"
    solve(solution, key_string)