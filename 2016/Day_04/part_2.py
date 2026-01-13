from pathlib import Path
from typing import List, Tuple


from Day_04.const import DAY, INPUT_FILE_NAME
from Day_04.const import EXAMPLE_INPUT_FILE_NAME_PART_2 as EXAMPLE_INPUT_FILE_NAME
from Day_04.load_input import load_input
from Day_04.part_1 import is_real_room
from utils.solve import test, solve

def apply_shift_cypher(shift_cypher: str|List[str], encrypted: str) -> str:
    decrypted = ""
    for char in encrypted:
        if char == "-":
            decrypted += "-"
            continue
        i = shift_cypher.index(char)
        decrypted += shift_cypher[(i+1)%len(shift_cypher)]
    return decrypted

def is_decrypted(s: str, target: str) -> bool:
    return target in s

def solution(rooms: List[Tuple[str, int, str]], target: str) -> int:
    real_rooms = [
        {"encrypted_name": encrypted_name, "sector_id": sector_id, "checksum": checksum}
        for encrypted_name, sector_id, checksum in rooms
        if is_real_room(encrypted_name, checksum)
    ]

    shift_cypher = "abcdefghijklmnopqrstuvwxyz"
    while True:
        for room in real_rooms:
            room["encrypted_name"] = apply_shift_cypher(shift_cypher, room["encrypted_name"])
            if is_decrypted(room["encrypted_name"], target):
                return room["sector_id"]

if __name__ == "__main__":
    example_target = "very-encrypted-name"
    example_rooms = load_input(Path(f"Day_{DAY:02d}/{EXAMPLE_INPUT_FILE_NAME}"))
    expected_answer = 343
    test(expected_answer, solution, example_rooms, example_target)

    target = "northpole"
    rooms = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))
    solve(solution, rooms, target)