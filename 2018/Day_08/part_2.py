from pathlib import Path
from typing import List

from Day_08.const import DAY, EXAMPLE_INPUT_FILE_NAME, INPUT_FILE_NAME
from Day_08.load_input import load_input
from Day_08.part_1 import TreeNode, build_tree
from utils.solve import test, solve
    
def get_node_value(node: TreeNode) -> int:
    if not node.children:
        return sum(node.metadata)

    child_values = []
    for child in node.children:
        child_values.append(get_node_value(child))

    total = 0
    for index in node.metadata:
        try:
            total += child_values[index-1]
        except:
            pass
    return total

def solution(numbers: List[int]) -> int:
    root = TreeNode()
    build_tree(numbers, root)
    return get_node_value(root)

if __name__ == "__main__":
    example_numbers = load_input(Path(f"Day_{DAY:02d}/{EXAMPLE_INPUT_FILE_NAME}"))
    expected_answer = 66
    test(expected_answer, solution, example_numbers)

    numbers = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))
    solve(solution, numbers)