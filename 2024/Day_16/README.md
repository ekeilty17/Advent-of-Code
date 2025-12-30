# Day 16: Reindeer Maze

[Problem Link](https://adventofcode.com/2024/day/16)

## Part 1

This falls under the class of problems called [Single Source Shortest Path](https://en.wikipedia.org/wiki/Shortest_path_problem) (SSSP). Since the shortest path from `S` to `E` contains within it the shortest path to all intermediary cells, the most efficient solution contains the shortest path from `S` to all other cells in the maze. 

The most famous SSSP algorithm is [Dijkstra's algorithm](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm). The only assumption made by Dijkstra's algorithm is that all edge weights are strictly position, which this problem fulfills. 

So, my part 1 solution is a standard implementation of Dijkstra's algorithm. The algorithm updates the object `dist` such that by the end of the algorithm `dist[u]` gives the shortest distance between `start` and `u`. Therefore, the solution is `dist[end]`. The only thing unique is we have to carry around the node direction and we have to add an extra condition `direction != neighbor_direction` when computing the edge weight. See the function `compute_neighbor_weight()` for more details.

## Part 2 

Part 2 is asking us to backtrack through all of the shortest paths from `S` to `E`. In theory, all this requires is for us to add another object `pred` such that `pred[u]` contains all of the precessors of `u` on the shortest paths from `start`. However, for this problem, naively that doesn't work. Let's see why.

### Why My Part 1 Solution Fails

In part 1, the node direction was not part of the index into `dist`, I was only using the grid coordinates. In part 1, we didn't care what direction we came from, we just cared that the distance was smaller. However, when backtracking this causes issues. Consider this example

```
#######
#....E#
#####.#
#.....#
#.###.#
#.....#
#S#####
#######
```

According to the rules of the problem, there will are 2 shortest paths with scores of `3009` (assuming `S` starts out facing east). This is because each path traverses `9` cells and turns `3` times.

```
#######
#....O#
#####O#
#OOOOO#
#O###O#
#OOOOO#
#O#####
#######
```

However, when we go to backtrack, we get a problem at this cell with an `X`. 
```
#######
#....O#
#####O#
#OOO1X#
#O###2#
#OOOOO#
#O#####
#######
```

The `1` directly next to the `X` has a shortest path of `2006` and the `2` directly below the `X` has a shortest path of `3006`. This is because the `2` path is already facing upwards, but the `1` path turns at the `X`. This is a problem because when we go to backtrack, the algorithm will think the `2` path is not part of a shortest path to `E`.

### The Part 2 Solution

The fix is that we have to include direction in the index of `dist`. Instead of `dist[u]` we now have `dist[u, direction]`. Now, in the above example, 
- `dist[X, ^] = 3006` with `pred[X, ^] = [(1, >), (2, ^)]`
- `dist[X, >] = 2006` with `pred[X, ^] = [(1, >)]`

The reason the part 1 solution did not work was the conflation of the states `dist[X, ^]` and `dist[X, >]`. Thus, `pred[X]` is not well defined.

Then all that is left is to write the backtracking to get all of the shortest paths, which took me longer than I expected. I don't love the way I wrote it, but it get's the job done.
