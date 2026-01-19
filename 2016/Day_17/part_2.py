import queue
from typing import List, Tuple, Optional

from Day_17.part_1 import get_neighbor_offsets_and_directions
from utils.solve import test, solve

def bfs(passcode: str, vault_shape: Tuple[int, int], start: Tuple[int, int], end: Tuple[int, int]) -> str:

    q = queue.Queue()
    q.put((start, ""))

    longest_path = ""

    while not q.empty():
        pos, directions = q.get()

        if pos == end:
            if len(directions) > len(longest_path):
                longest_path = directions
            continue
        
        for x, y, D in get_neighbor_offsets_and_directions(passcode + directions, pos, vault_shape):
            q.put(((x, y), directions + D))

    return longest_path

def solution(passcode: str, vault_shape: Tuple[int, int], start: Tuple[int, int], end: Tuple[int, int]) -> int:
    longest_path = bfs(passcode, vault_shape, start, end)
    return len(longest_path)

if __name__ == "__main__":
    vault_shape = (4, 4)
    start = (0, 0)
    end = (3, 3)
    
    example_passcode_1 = "hijkl"
    expected_answer_1 = 0
    test(expected_answer_1, solution, example_passcode_1, vault_shape, start, end)

    example_passcode_2 = "ihgpwlah"
    expected_answer_2 = 370
    test(expected_answer_2, solution, example_passcode_2, vault_shape, start, end)

    example_passcode_3 = "kglvqrro"
    expected_answer_3 = 492
    test(expected_answer_3, solution, example_passcode_3, vault_shape, start, end)

    example_passcode_4 = "ulqzkmiv"
    expected_answer_4 = 830
    test(expected_answer_4, solution, example_passcode_4, vault_shape, start, end)

    passcode = "lpvhkcbi"
    solve(solution, passcode, vault_shape, start, end)