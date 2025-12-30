# Day 18: RAM Run

[Problem Link](https://adventofcode.com/2024/day/18)

## Part 1

The question asks us to find the shortest distance from the top left corner of the memory space to the bottom right corner, given some corrupted bits blocking our path. It's actually just an easier version of Day 16 since we don't have to deal with directions influencing the edge weight. Again I implemented [Dijkstra's algorithm](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm) starting at position `(0, 0)`. This returns `dist` which is an array of the shortest path between `(0, 0)` and every other memory cell. The solution is therefore `dist[-1, -1]`.

## Part 2 

The naive solution for part 2 is as follows
1. Let `N` be the number of corrupt bits
2. **For each** `i = 1..N`
    1. Corrupt bits in positions `positions[0:i]`
    2. Check if there exists a path from `(0, 0)` to `(-1, -1)`
    3. If there is no path, return `i`

This is a linear search through the corrupt bit positions. With the solution being at position `3001`, this is not very fast. 

We can improve by instead using a [binary search](https://www.geeksforgeeks.org/dsa/binary-search/). See `part_2.py` for the implementation. It's just a standard binary search, nothing unique to share. Using binary search we can find the solution in only 12 steps, as opposed to the 3001 steps required with a linear search.
