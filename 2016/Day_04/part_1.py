from pathlib import Path
from typing import List, Tuple

from Day_04.const import DAY, INPUT_FILE_NAME
from Day_04.const import EXAMPLE_INPUT_FILE_NAME_PART_1 as EXAMPLE_INPUT_FILE_NAME
from Day_04.load_input import load_input
from utils.solve import test, solve

def is_real_room(encrypted_name: str, checksum: str) -> bool:
    k = len(checksum)
    counter = {}
    for char in encrypted_name.replace("-", ""):
        if char in counter:
            counter[char] += 1
        else:
            counter[char] = 1
    
    most_frequent_characters = list(sorted(counter.items(), key=lambda t: (-t[1], t[0])))
    generated_checksum = "".join([char for char, frequency in most_frequent_characters[:k]])
    return generated_checksum == checksum

def solution(rooms: List[Tuple[str, int, str]]) -> int:
    total = 0
    for encrypted_name, sector_id, checksum in rooms:
        if is_real_room(encrypted_name, checksum):
            total += sector_id

    return total

if __name__ == "__main__":
    example_rooms = load_input(Path(f"Day_{DAY:02d}/{EXAMPLE_INPUT_FILE_NAME}"))
    expected_answer = 1514
    test(expected_answer, solution, example_rooms)

    rooms = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))
    solve(solution, rooms)