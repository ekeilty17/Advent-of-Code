# Day 6: Signals and Noise

[Problem Link](https://adventofcode.com/2016/day/6)

## Part 1

Very straight-forward solution. First, transpose the rows and columns from the input so you have a list of column strings. Then just count the most common letter in each column. This time, I did use [collections.Counter](https://docs.python.org/3/library/collections.html#collections.Counter).

## Part 2 

Exactly the same as part 1, except get the least common instead of most common.