# Day 8: Playground

[Problem Link](https://adventofcode.com/2025/day/8)

## Heap Data Structure

In this problem, we need to iterate through pairs of coordinates in order of their minimum distance. You could just do this with a sorted list. I decided to use a heap since that is a bit more efficient. 

One subtlety is to make sure that we are including only unique pairs of coordinates. We can do this by applying the constraint 
```
coord1 < coord2
```

## Part 1

The hardest part for me was just the interpretation of the problem. Once I understood it, it was not so bad. I used a list of sets of coordinates where each set represented a circuit, and a heap. The algorithm is the following.

1. **Initialize** a list `C` containing a singleton set for each box `b`. This is the current set of circuits.
2. **For each** unique pair of boxes, add them to heap `H` using the [Euclidean distance](https://en.wikipedia.org/wiki/Euclidean_distance) as the priority metric
3. **Iterate** `N` times
    1. Pop the next closest pair boxes `b1` and `b2` from `H`
    2. Find their corresponding circuits in `c1` and `c2` in `C`
    3. **If** `c1 == c2` **then** skip to next iteration
    4. **Else** merge `c1` and `c2`, and replace both with the merged circuit in `C`

The problem says to "connect together the `N` pairs of junction boxes which are closest together". This is where `N` comes from in step `3.`.

## Part 2

Once you have part 1 this is easy. Just replace the for loop iterating a set `N` number of times with a while loop iterating until the number of circuits (i.e. length of `C`) is `1`.
