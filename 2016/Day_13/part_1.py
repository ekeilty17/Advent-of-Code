from typing import Tuple
import queue

from utils.solve import test, solve
from utils.grid import get_orthogonal_neighbor_indices

def f(x, y):
    return x*x + 3*x + 2*x*y + y + y*y

def is_wall(n, x, y):
    z = f(x, y) + n
    return z.bit_count() % 2

def bfs(n, start, end):
    visited = set([])

    q = queue.Queue()
    q.put((start, 0))

    while not q.empty():
        node, depth = q.get()
        visited.add(node)

        if node == end:
            return depth

        for neighbor in get_orthogonal_neighbor_indices((float("inf"), float("inf")), *node):
            neighbor = tuple([int(x) for x in neighbor])
            if is_wall(n, *neighbor):
                continue
            if neighbor in visited:
                continue
            q.put((neighbor, depth+1))

    return None

def solution(favorite_number: int, start: Tuple[int, int], end: Tuple[int, int]) -> int:
    return bfs(favorite_number, start, end)

if __name__ == "__main__":
    start = (1, 1)

    example_favorite_number = 10
    example_end = (7, 4)
    expected_answer = 11
    test(expected_answer, solution, example_favorite_number, start, example_end)

    favorite_number = 1352
    end = (31, 39)
    solve(solution, favorite_number, start, end)