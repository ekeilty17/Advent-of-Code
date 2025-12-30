# Day 7: Laboratories

[Problem Link](https://adventofcode.com/2025/day/7)

## Binary Tree

Both part 1 and part 2 can be solved by converting the problem into a [Binary Tree](https://en.wikipedia.org/wiki/Binary_tree). `S` was the root, and each of the `^` represented a new node with a left and right child. However, there is a catch. The problem does not convert into a true binary tree because some children can be shared. This happens when beams `|` intersect. The hardest of converting the input into a binary tree is maintaining the correct reference during the beam intersections.

To do this correctly, you have to first propogate each line and only then process the splits to define the left and right child. If a child already exists due to the beam propogation, then you keep the reference rather than defining a new node. All of the glorious details can be found in `convert_tachyon_manifold_to_binary_tree.py`.

A binary tree was necessary to efficiently compute part 2, but it can also be used to solve part 1. This was done in `part_1_alt.py`.

## Part 1

This is another parsing game, but definitely more complicated than Day 6. 

### My Original Solution

I just iterate down the rows and propogate the beams according to the rules. Every time a beam `|` hits a splitter `^`, I incremented a counter. 

Note that you can't just count the `^` because you would over count. A split only occurs when a beam actually hits a `^`.

### My Alternative Solution

I converted the problem into a binary tree. The number of splits can now be solved using a modified tree traversal in `O(n)` time. If a node has a defined left and right child, then that counts as 1 split. 
```
count_splits(node) = 1 + count_splits(node.left) + count_splits(node.right)
count_splits(leaf) = 0
```
Since children can be shared, you have to included a `visited` flag to make sure you are not double counting subtrees.

## Part 2

I converted the problem into a binary tree. The "number of timelines" is now the number of unique paths from the root to the leaves in the binary tree. Again, this can be solved with a tree traversal in `O(n)` time.

```
count_paths(node) = count_paths(node.left) + num_paths(node.right)
count_paths(leaf) = 1
```

In this case, the `visited` flag is not required for correctness, but it ensure the solution stays `O(n)`.
