# Day 5: Cafeteria

[Problem Link](https://adventofcode.com/2025/day/5)

## The Interval Set Data Structure

The first half of the input is a set of overlapping intervals. The reason part 2 is slow is because there are too many redundant intervals. This data structure is conceptually very simple, we are just merging all of the _overlapping_ intervals into a smaller set of _non-overlapping_ intervals.

Implementation of the data structure hinges on the `add()` method. It took a few tries, but I landed on a simple algorithm that I like. 
1. let `I` be the set of all intervals currently in the data structure
2. Let `[a, b]` be a new interval
3. Find all intervals `[a1, b1], ..., [an, bn]` in `I` that overlap with `[a, b]`
4. Remove the overlapping intervals `[a1, b1], ..., [an, bn]` from `I`
5. Add the interval `[min(a, a1, ..., an), max(b, b1, ..., bn)]` to `I`

There are some things you could do to make this data structure even faster. For example, you could store the intervals sorted and then use a binary search to find the overlapping intervals. This would make step `3.` `O(log n)` rather than `O(n)`. And step `5.` would now be worst case `O(log n)` instead of `O(1)`.

With this data structure, part 1 and part 2 are almost trivial.

## Part 1

Count the number of unique ingredient IDs that exist in the interval set. This can be done with `set()` in Python.

## Part 2

Sum the length of all of the intervals in the interval set. Since the intervals are inclusive, the length of `[a, b]` is `b - a + 1`.
