from pathlib import Path
from typing import List

from Day_07.const import DAY, EXAMPLE_INPUT_FILE_NAME, INPUT_FILE_NAME
from Day_07.load_input import load_input
from Day_07.binary_tree import BinaryTree
from Day_07.convert_tachyon_manifold_to_binary_tree import convert_tachyon_manifold_to_binary_tree
from utils.test import test

def count_paths(node):
    # base case
    if node is None:
        return 0

    # not strictly necessary but saves a lot of time
    if node.visited:
        return node.value
    node.visited = True

    # base case
    if node.left is None and node.right is None:
        node.value = 1
        return 1

    # memoize and recurse
    node.value = count_paths(node.left) + count_paths(node.right)
    return node.value

def solution(tachyon_manifold: List[List[str]]) -> int:
    root: BinaryTree = convert_tachyon_manifold_to_binary_tree(tachyon_manifold)
    num_paths = count_paths(root)
    return num_paths

if __name__ == "__main__":
    
    example_tachyon_manifold = load_input(Path(f"Day_{DAY:02d}/{EXAMPLE_INPUT_FILE_NAME}"))
    tachyon_manifold = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))

    expected_answer = 40
    test(expected_answer, solution, example_tachyon_manifold)

    total = solution(tachyon_manifold)
    print("Puzzle Answer:", total)