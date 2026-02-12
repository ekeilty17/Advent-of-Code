from pathlib import Path
from typing import List, Dict, Any
import numpy as np
import heapq

from Day_22.const import DAY, EXAMPLE_INPUT_FILE_NAME, INPUT_FILE_NAME
from Day_22.load_input import load_input
from Day_22.part_1 import is_viable_pair
from utils.solve import test, solve
from utils.grid import get_orthogonal_neighbor_indices
from utils.display_np import *

def display_memory(capacity, used):
    print(capacity)
    print(used)
    arr = np.full(capacity.T.shape, "", dtype="<U20")
    for idx in np.ndindex(capacity.T.shape):
        arr[idx] = f"{used.T[idx]}/{capacity.T[idx]}"
    print(arr)

def initialize_capacity_and_usage(disk_usage: List[Dict[str, Any]]):
    nodes = {}
    for row in disk_usage:
        filesystem = row["Filesystem"]
        *_, x, y = filesystem.split("-")
        x = int(x[1:])
        y = int(y[1:])
        nodes[(x, y)] = row

    max_x = max(x for x, _ in nodes.keys())
    max_y = max(y for _, y in nodes.keys())

    capacity = np.zeros((max_x+1, max_y+1), dtype=int)
    used = np.zeros_like(capacity, dtype=int)
    for node, usage in nodes.items():
        capacity[node] = usage["Size"]
        used[node] = usage["Used"]

    return capacity, used

def heuristic(pos, end):
    x1, y1 = pos
    x2, y2 = end
    return abs(x2 - x1) + abs(y2 - y1)

def get_state(pos, used):
    return (pos, tuple(used.flatten()))

def is_viable(capacity, used, from_pos, to_pos):
    to_available = capacity[to_pos] - used[to_pos]
    return used[from_pos] != 0 and used[from_pos] <= to_available

def a_star(capacity, used, start, end):
    zero_usage = list(zip(*np.where(used == 0)))[0]

    visited = {}
    
    frontier = []
    score = 0 + heuristic(used, start, end)
    init_state = get_state(start, used)
    heapq.heappush(frontier, (score, 0, start, init_state) )
    visited[init_state] = 0

    while frontier:
        score, depth, pos, state = heapq.heappop(frontier)
        print(depth, pos)
        used = np.array(state[1]).reshape(capacity.shape)

        if pos == end:
            return depth

        # Try to move the data packet
        for neighbor_index in get_orthogonal_neighbor_indices(used.shape, *pos):
            if not is_viable(capacity, used, pos, neighbor_index):
                continue
            
            nxt_used = used.copy()
            nxt_used[neighbor_index] += used[pos]
            nxt_used[pos] = 0

            state = get_state(neighbor_index, nxt_used)
            if visited.get(state, float("inf")) > depth + 1:
                score = depth + 1 + heuristic(used, neighbor_index, end)
                # print((score, depth+1, neighbor_index, state, nxt_used))
                heapq.heappush(frontier, (score, depth+1, neighbor_index, state))

        # print(frontier)
        # print()

        # shuffle around other data
        for data_pos in np.ndindex(used.shape):
            if data_pos == pos:
                continue
            for neighbor_index in get_orthogonal_neighbor_indices(used.shape, *data_pos):
                if neighbor_index == pos:
                    continue

                if not is_viable(capacity, used, data_pos, neighbor_index):
                    continue

                nxt_used = used.copy()
                nxt_used[neighbor_index] += used[data_pos]
                nxt_used[data_pos] = 0

                state = get_state(pos, nxt_used)
                if visited.get(state, float("inf")) > depth + 1:
                    score = depth + 1 + heuristic(used, pos, end)
                    # print((score, depth+1, pos, state, nxt_used))
                    heapq.heappush(frontier, (score, depth+1, pos, state))

        # print(frontier)
        # return

    return None

def solution(disk_usage: List[Dict[str, Any]]) -> int:
    capacity, used = initialize_capacity_and_usage(disk_usage)

    start = (used.shape[0]-1, 0)
    end = (0, 0)

    return a_star(capacity, used, start, end)

if __name__ == "__main__":
    _, example_disk_usage = load_input(Path(f"Day_{DAY:02d}/{EXAMPLE_INPUT_FILE_NAME}"))
    expected_answer = 7
    test(expected_answer, solution, example_disk_usage)

    _, disk_usage = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))
    solve(solution, disk_usage)