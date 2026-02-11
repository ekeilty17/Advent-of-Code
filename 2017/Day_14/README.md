# Day 14: Disk Defragmentation

[Problem Link](https://adventofcode.com/2017/day/14)

## Part 1

Reusing my `knot_hash()` function from Day 10 part 2 do the following
1. **For** each `index` 0 to 127
    1. Compute `knot_hash(f"{key_string}-{index}")`
    2. Convert the hex string to an integer
    3. Count the number of `1`'s in the resulting binary string
2. **return** the total `1`'s in all binary strings

## Part 2 

In part 2 we need to actually construct the disk grid. Each binary string is converted to a boolean array and concatenated into a 2D numpy array.

Then we run a series of [Depth-First Searches](https://en.wikipedia.org/wiki/Depth-first_search) (DFS) to find all of the [Connected Component](https://en.wikipedia.org/wiki/Component_(graph_theory)), similar to Day 12 part 2. The solution is the number of component in the graph.