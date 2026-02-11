# Day 17: Spinlock

[Problem Link](https://adventofcode.com/2017/day/17)

## Part 1

One of those problems where the solution is to just simulate the process described by the problem. In the function `compute_spinlock()` in `part_1.py` I maintain the list `spinlock`. In each iteration I compute the updated index and insert.

After the spinlock algorithm, I find the index of `2017` and return the number after that index.

## Part 2 

In part 2, the naive solution of computing the actual spinlock does not work, as this list would be `50_000_000` elements long. Instead, we only have to keep track of what value ends up at index `1`.

In each iteration, we compute the updated index `i`. If `i == 1` then that is the value after `0`.