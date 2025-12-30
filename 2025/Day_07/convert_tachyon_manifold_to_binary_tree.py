from typing import List
from Day_07.binary_tree import BinaryTree

def convert_tachyon_manifold_to_binary_tree(tachyon_manifold: List[List[str]]) -> BinaryTree:
    root = BinaryTree()
    for j, cell in enumerate(tachyon_manifold[0]):
        if cell == "S":
            tachyon_manifold[0][j] = root

    for i, row in enumerate(tachyon_manifold[:-1]):

        # First propogate the lines
        for j, cell in enumerate(row):
            if isinstance(cell, BinaryTree):
                node = cell
                if tachyon_manifold[i+1][j] == "^":
                    # do this in the next pass
                    pass
                else:
                    tachyon_manifold[i+1][j] = node

        # Then we do the splits
        for j, cell in enumerate(row):
            if isinstance(cell, BinaryTree):
                node = cell
                if tachyon_manifold[i+1][j] == "^":
                    left_cell = tachyon_manifold[i+1][j-1]
                    if isinstance(left_cell, BinaryTree):
                        node.left = left_cell
                    else:
                        node.left = BinaryTree()
                        tachyon_manifold[i+1][j-1] = node.left
                    
                    right_cell = tachyon_manifold[i+1][j+1]
                    if isinstance(right_cell, BinaryTree):
                        node.right = right_cell
                    else:
                        node.right = BinaryTree()
                        tachyon_manifold[i+1][j+1] = node.right
                else:
                    # done in previous pass
                    pass

    return root