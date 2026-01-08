from pathlib import Path
from typing import List

from Day_07.const import DAY, EXAMPLE_INPUT_FILE_NAME, INPUT_FILE_NAME
from Day_07.load_input import load_input
from Day_07.binary_tree import BinaryTree
from Day_07.convert_tachyon_manifold_to_binary_tree import convert_tachyon_manifold_to_binary_tree
from utils.solve import test, solve

def count_splits(node):
    if node is None:
        return 0
    
    # This is required because nodes can have multiple parents
    # without this check we would be double counting some splits
    if node.visited:
        return 0
    
    node.visited = True
    # In this problem you'd never have one side defined but not the other
    # not sure what you'd consider it, but probably wouldn't count as a split
    if node.left is None or node.right is None:
        return 0
    return 1 + count_splits(node.left) + count_splits(node.right)

def solution(tachyon_manifold: List[List[str]]) -> int:
    root: BinaryTree = convert_tachyon_manifold_to_binary_tree(tachyon_manifold)
    num_splits = count_splits(root)
    return num_splits

if __name__ == "__main__":
    example_tachyon_manifold = load_input(Path(f"Day_{DAY:02d}/{EXAMPLE_INPUT_FILE_NAME}"))
    expected_answer = 21
    test(expected_answer, solution, example_tachyon_manifold)

    tachyon_manifold = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))
    solve(solution, tachyon_manifold)