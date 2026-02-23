# Day 7: The Sum of Its Parts

[Problem Link](https://adventofcode.com/2018/day/7)

## Part 1

Part 1 is asking to find the [Topological Sort](https://en.wikipedia.org/wiki/Topological_sorting) of the input. I implement the standard [Kahn's algorithm](https://www.geeksforgeeks.org/dsa/topological-sorting-indegree-based-solution/) which is essentially a modified BFS. 

The lines
```python
queue = list(sorted(queue, reverse=True))
node = queue.pop()
```

pop the nodes in alphabetical order. This also could have been implemented as a priority queue which would be asymptotically faster. However since there are only 26 nodes in the input, this would not make a difference.

## Part 2 

I modified the topological sort code from part 1 and implemented exactly what the problem describes. I maintain 2 data structure.
1. The list `workers` which contain the nodes that are being processed. Each node comes with a counter representing how many time steps are remaining in its execution. 
2. The list `queue` which are the next available nodes (the same as `queue` in part 1).

At each iteration, the following happens
1. Each `worker` decrements their node's counter by 1. If the counter is 0, then the node is removed.
2. If a node is removed, then we do the topological sort update to determine if its neighbors should be added to the `queue`.
3. Any empty `worker` is filled with the next available node in the `queue` (in alphabetical order)