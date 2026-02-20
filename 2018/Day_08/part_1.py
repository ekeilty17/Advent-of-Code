from pathlib import Path
from typing import List

from Day_08.const import DAY, EXAMPLE_INPUT_FILE_NAME, INPUT_FILE_NAME
from Day_08.load_input import load_input
from utils.solve import test, solve

class TreeNode:

    def __init__(self):
        self.children = []
        self.metadata = []

def build_tree(numbers: List[int], node: TreeNode) -> List[int]:
    if not numbers:
        return []

    num_children, num_metadata, *remaining_numbers = numbers
    for _ in range(num_children):
        child = TreeNode()
        remaining_numbers = build_tree(remaining_numbers, child)
        node.children.append(child)
    
    node.metadata = remaining_numbers[:num_metadata]
    return remaining_numbers[num_metadata:]
    
def get_node_value(node: TreeNode) -> int:
    return sum(node.metadata) + sum([get_node_value(child) for child in node.children])

def solution(numbers: List[int]) -> int:
    root = TreeNode()
    build_tree(numbers, root)
    return get_node_value(root)

if __name__ == "__main__":
    example_numbers = load_input(Path(f"Day_{DAY:02d}/{EXAMPLE_INPUT_FILE_NAME}"))
    expected_answer = 138
    test(expected_answer, solution, example_numbers)

    numbers = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))
    solve(solution, numbers)