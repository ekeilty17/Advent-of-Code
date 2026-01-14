# Day 13: A Maze of Twisty Little Cubicles

[Problem Link](https://adventofcode.com/2016/day/13)

## Part 1

We are trying to find the shortest number of steps to get from some `start` location to an `end` location on an infinite grid. The solution is to implement a [Breadth-First Search](https://www.geeksforgeeks.org/dsa/breadth-first-search-or-bfs-for-a-graph/) (BFS). Note that when all edge weights are `1`, a BFS is equivalent to [Dijkstra's algorithm](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm).

At each iteration, we are incrementing our frontier by 1 depth, skipping any locations that we have already visited. The solution is the depth at the first time we encounter the `end` location.

## Part 2 

Same as part 1, except we are not terminating when we reach some `end` location. Instead we are terminating once we have reached a depth of `50`. Then we just returned all of the unique nodes that we have visited (maintained by the set `visited`).