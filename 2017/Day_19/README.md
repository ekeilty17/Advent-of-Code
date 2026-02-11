# Day 19: A Series of Tubes

[Problem Link](https://adventofcode.com/2017/day/19)

## Part 1 and Part 2

Both part 1 and part 2 are essentially the same. One is counting the letter along the path and the other is counting the number of steps. In both parts, we need to travel along the routing diagram provided by the input.

The key to traversing the routing diagram is to maintain both your current position and direction. Now we have a concept of `forward`, `backward`, `left`, and `right`. The rules of traversal are now simple
- `forward` is always preferred if it exists
- never travel `backward`
- otherwise travel either `left` or `right`

Note in the last case, there should always be only 1 left or right direction. Otherwise, the routing diagram is ambiguous. The input always has a space between adjacent lines which are not related.