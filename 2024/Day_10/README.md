# Day 10: Hoof It

[Problem Link](https://adventofcode.com/2024/day/10)

## Background

### The Graph Data Structure

The topographic map from the problem statement can be thought of as a [graph](https://en.wikipedia.org/wiki/Graph_(abstract_data_type)). Two orthogonally adjacent positions `p1` and `p2` in the topographical map form an edge if and only if the elevation of `p2` is exactly one greater than the elevation of `p1`. Both parts are applications of graph traversals.

To solve this problem, I did not abstract the grid into a generic graph data type. Instead I used the grid as a graph with the `get_orthogonal_neighbor_indices()` function found in `utils/grid/py`.

## Part 1

Part 1 is a graph traversal finding all _connected components_, i.e. positions reachable from the trailheads. This can be done by either using a [Breadth-First Search](https://en.wikipedia.org/wiki/Breadth-first_search) (BFS) or [Depth-First Search](https://en.wikipedia.org/wiki/Depth-first_search) (DFS). Since I used a recursive approach, DFS is the simplest to implement.

My modified DFS returns a boolean array of all positions reachable from the trailhead. I also had a boolean array of all of the positions of the peaks. Thus, the peaks reachable by the trailhead is the bitwise `AND` between these arrays. The solution to part 1 is the count of all peaks reachable from each trailhead.

## Part 2 

Part 1 is another type of graph traversal attempting to find _all paths_ from a trailhead to a peak. I implemented this using the standard DFS + backtracking algorithm. The solution to part 2 is the count of all paths from each trailhead to each any peak.
