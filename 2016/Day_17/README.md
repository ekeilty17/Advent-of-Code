# Day 17: Two Steps Forward

[Problem Link](https://adventofcode.com/2016/day/17)

## Part 1

A nice problem today which requires a standard [Breadth-First Search](https://www.geeksforgeeks.org/dsa/breadth-first-search-or-bfs-for-a-graph/) (BFS) to find the shorteset path from a `start` position to an `end` position.

The most annoying part of the problem was determining the neighbors, i.e. what vault doors are open/closed given your current position and state. All of those details are in `get_neighbor_offsets_and_directions()`. I don't think they are very interesting.

The only major difference between this and the standard BFS is there is no `visited` list. This is because your state depends both on your current position AND your path history. So landing on `(1, 1)` via `DR` vs `RD` are actually two different states with different neighbors.

## Part 2 

Just a modification to the BFS from part 1. Instead of terminating when `pos == end`, we maintain a `longest_path` variable and update it every time we reach the `end` position. Note that once you reach the `end` position, that path terminates (otherwise the state-space is likely infinite).