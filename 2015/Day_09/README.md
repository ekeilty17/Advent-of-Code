# Day 9: All in a Single Night

[Problem Link](https://adventofcode.com/2015/day/9)

## Part 1

So this problem is asking us to find a [Hamiltonian Path](https://en.wikipedia.org/wiki/Hamiltonian_path) (i.e. hits every node exactly once) with the minimum total distance.

I just brute forced it. Since the graph is complete, every permutation of the complete list of cities is a different Hamiltonian path. So I just iterate over every possible Hamiltonian path, calculate its total distance, and take the minimum. The graph is small enough that this approach is sufficient.

## Part 2 

Exactly the same as part 1, except I take the maximum instead of the minimum.