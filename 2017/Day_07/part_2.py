from pathlib import Path
from typing import List, Tuple, Dict
from collections import deque

from Day_07.const import DAY, EXAMPLE_INPUT_FILE_NAME, INPUT_FILE_NAME
from Day_07.load_input import load_input
from Day_07.part_1 import get_roots
from utils.solve import test, solve

class TreeNode:

    def __init__(self, name: str, weight: int):
        self.name = name
        self.weight = weight
        self.children = []

        self.subtree_weight = 0
    
    def __repr__(self):
        return f"{self.name} ({self.weight})"

    def add_child(self, child):
        self.children.append(child)
    
    def add_children(self, *children):
        self.children.extend(children)


# Standard DFS
def construct_tree(
    weight_by_program:  Dict[str, List[str]], 
    children_by_program: Dict[str, List[str]], 
    node_name: str|None=None
) -> TreeNode:
    if node_name is None:
        node_name = get_roots(children_by_program)[0]
    
    weight = weight_by_program[node_name]
    children = children_by_program[node_name]
    node = TreeNode(node_name, weight)

    for child_name in children:
        child = construct_tree(weight_by_program, children_by_program, child_name)
        node.add_child(child)
    
    return node


# Standard DFS
def compute_subtree_weights(node: TreeNode) -> int:
    node.subtree_weight = node.weight + sum([compute_subtree_weights(child) for child in node.children])
    return node.subtree_weight


# Post-Order traversal
def search_for_unbalanced_node(node: TreeNode) -> TreeNode:
    for child in node.children:
        result = search_for_unbalanced_node(child)
        if result:
            return result
    
    # check if current node is unbalanced
    if not all(child.subtree_weight == node.children[0].subtree_weight for child in node.children):
        return node

def compute_balance_correction(unbalanced_node: TreeNode) -> int:
    weights = {}
    for child in unbalanced_node.children:
        if child.subtree_weight not in weights:
            weights[child.subtree_weight] = []
        weights[child.subtree_weight].append(child)
    
    unbalanced_weight, unbalanced_children = min(weights.items(), key=lambda t: len(t[1]))
    balanced_weight, balanced_children = max(weights.items(), key=lambda t: len(t[1]))

    unbalanced_child = unbalanced_children[0]
    return unbalanced_child.weight + (balanced_weight - unbalanced_weight)


def solution(weight_by_program:  Dict[str, List[str]], children_by_program: Dict[str, List[str]]) -> str:
    root = construct_tree(weight_by_program, children_by_program)
    compute_subtree_weights(root)
    unbalanced_node = search_for_unbalanced_node(root)
    return compute_balance_correction(unbalanced_node)

if __name__ == "__main__":
    example_weight_by_program, example_children_by_program = load_input(Path(f"Day_{DAY:02d}/{EXAMPLE_INPUT_FILE_NAME}"))
    expected_answer = 60
    test(expected_answer, solution, example_weight_by_program, example_children_by_program)

    weight_by_program, children_by_program = load_input(Path(f"Day_{DAY:02d}/{INPUT_FILE_NAME}"))
    solve(solution, weight_by_program, children_by_program)