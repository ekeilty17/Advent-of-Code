# Day 4: Printing Department

[Problem Link](https://adventofcode.com/2025/day/4)

## Part 1

The most annoying part was just writing the `get_neighbors()` function. I stored all of the paper spots in a boolean numpy array. Then I compute all of the accessible spots as a boolean numpy array. Then the accessible paper spots is just an element-wise `AND` between them

## Part 2

Take the code in part 1 and just loop until there are no accessible spots. I can't think of any more efficient algorithm.
