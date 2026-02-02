# Day 7: Recursive Circus

[Problem Link](https://adventofcode.com/2017/day/7)

## Search Trees

The puzzle is input is a [Search Tree](https://en.wikipedia.org/wiki/Search_tree). Because I think it makes the explainations more clear, I am going to use tree terms (e.g. node, root, children, parent, etc) rather than the terms from the problem statement (e.g. program, bottom program, above, below, etc).

## Part 1

The input gives us the list of children for each node in the tree. In order to find the root we need to _"invert"_ this list by finding the parent of each node. The node which does not have a parent is the root node. See the implementation in the function `get_roots()` in `part_1.py`.

## Part 2 

There are probably more efficient ways of doing this with less lines of code, but I broke up the solution into very modular steps for explainability. 

**Step 1**: Construct the search tree. From part 1 we know the root of the tree and from the puzzle input we have a list of children for each node. Therefore, we do a [Depth-First Search](https://en.wikipedia.org/wiki/Depth-first_search) (DFS) tree traversal and recursively add children starting at the root.

**Step 2**: Compute the subtree weight at each node. We can use the recurrence
```python
node.subtree_weight = node.weight + sum([child.subtree_weight for child in node.children])
```
except `child.subtree_weight` is replaced by a recursive function call. Again, we use a DFS tree traversal.

**Step 3**: Identify the unbalanced node. You have to be careful here. An unbalanced node will cause all of its parents to also become unbalanced. So actually, we want to find the unbalanced node at the farthest depth. To accomplish this, we use a [Post-Order Traversal](https://en.wikipedia.org/wiki/Tree_traversal#Post-order_implementation) where we process the children before processing the parent. 

**Step 4**: Finally, we analyze the children of the unbalanced node and determine the required correction. See the function `compute_balance_correction()` in `part_2.py` for the implementation.

Steps 1-3 are `O(n)` and step 4 is `O(1)`, so the entire algorithm is `O(n)`. I'm sure that steps 1-3 could be condensed into a single function if you tried hard enough.