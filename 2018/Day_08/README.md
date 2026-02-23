# Day 8: Memory Maneuver

[Problem Link](https://adventofcode.com/2018/day/8)

## Part 1

Conceptually this solution is very simple. 1) parse the input into a tree structure while also extracting the **metadata** of each node, 2) compute the **value** of root node.

The input is sort of a mix between a [pre-order](https://www.w3schools.com/dsa/dsa_algo_binarytrees_preorder.php) and [post-order](https://www.w3schools.com/dsa/dsa_algo_binarytrees_postorder.php) traversal. The current node's information sandwiches the information of its children. Our first task is to reconstruct tree.

In general the input numbers can be split into the following sections

```python
numbers = [num_children, num_metadata, *children_numbers, *metadata, *remaining_numbers]
```

The length of `children_numbers` can be computed recursively using `children_numbers`. The length of `metadata` is `num_metadata`. The section `remaining_numbers` represents nodes in a different subtree as the current node.

So the algorithm is the following 
1. `numbers` is given as input with the structure `[num_children, num_metadata, *children_numbers, *metadata, *remaining_numbers]`
2. Extract `num_children` and `num_metadata`
3. **Iterate** `num_children` times
    1. recurse on `[*children_numbers, *metadata, *sibling_numbers]`
4. After all iterations, we should have processed all elements in the section `*children_numbers`, therefore we are left with `[*metadata, *remaining_numbers]`
5. Extract `metadata`

Using this logic, we can parse the input into a [search tree](https://en.wikipedia.org/wiki/Search_tree). See the function `build_tree()` in `part_1.py`.

Now, let's define the **value** of a node as sum of its metadata entries and all metadata entries in its subtree. This is a simple recursion
```python
def get_node_value(node):
    return sum(node.metadata) + sum([get_node_value(child) for child in node.children])
```

The solution is the value of the root node.

## Part 2 

Part 2 just has a different definition for the **value** of a node. If a node has no children, then its value is the sum of the nodes metadata. Otherwise, the value is the sum of the children index by the metadata list. See `get_node_value()` in `part_2.py` for the implementation details.