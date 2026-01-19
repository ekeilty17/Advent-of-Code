import hashlib
import queue
from typing import List, Tuple, Optional

from utils.solve import test, solve

def get_neighbor_offsets_and_directions(passcode: str, pos: Tuple[int, int], vault_shape: Tuple[int, int]) -> List[Tuple[int, int, str]]:
    OPEN_CHARS = "bcdef"
    h = hashlib.md5(passcode.encode()).hexdigest()
    offsets = []
    if h[0] in OPEN_CHARS:
        offsets.append((-1, 0, "U"))
    if h[1] in OPEN_CHARS:
        offsets.append((1, 0, "D"))
    if h[2] in OPEN_CHARS:
        offsets.append((0, -1, "L"))
    if h[3] in OPEN_CHARS:
        offsets.append((0, 1, "R"))
    
    x, y = pos
    return [(x+dx, y+dy, D) for dx, dy, D in offsets if 0 <= x+dx < vault_shape[0] and 0 <= y+dy < vault_shape[1]]

def bfs(passcode: str, vault_shape: Tuple[int, int], start: Tuple[int, int], end: Tuple[int, int]) -> Optional[str]:

    q = queue.Queue()
    q.put((start, ""))

    while not q.empty():
        pos, directions = q.get()

        if pos == end:
            return directions
        
        for x, y, D in get_neighbor_offsets_and_directions(passcode + directions, pos, vault_shape):
            q.put(((x, y), directions + D))

    return None

def solution(passcode: str, vault_shape: Tuple[int, int], start: Tuple[int, int], end: Tuple[int, int]) -> str:
    return bfs(passcode, vault_shape, start, end)

if __name__ == "__main__":
    vault_shape = (4, 4)
    start = (0, 0)
    end = (3, 3)
    
    example_passcode_1 = "hijkl"
    expected_answer_1 = None
    test(expected_answer_1, solution, example_passcode_1, vault_shape, start, end)

    example_passcode_2 = "ihgpwlah"
    expected_answer_2 = "DDRRRD"
    test(expected_answer_2, solution, example_passcode_2, vault_shape, start, end)

    example_passcode_3 = "kglvqrro"
    expected_answer_3 = "DDUDRLRRUDRD"
    test(expected_answer_3, solution, example_passcode_3, vault_shape, start, end)

    example_passcode_4 = "ulqzkmiv"
    expected_answer_4 = "DRURDRUDDLLDLUURRDULRLDUUDDDRR"
    test(expected_answer_4, solution, example_passcode_4, vault_shape, start, end)

    passcode = "lpvhkcbi"
    solve(solution, passcode, vault_shape, start, end)