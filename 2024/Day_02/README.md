# Day 02: Red-Nosed Reports

[Problem Link](https://adventofcode.com/2024/day/02)

## Part 1

The solution is just a matter of getting the logic inside the `is_safe()` function correct. We iterate through the `report` list and are checking for two conditions simultaneously. 

1. For every pair, their difference is between 1 and 3 (inclusive)
2. For each pair, their difference is between -3 and -1 (inclusive)

If we ever find that both of those conditions are not met, then we return `False`. If after checking all elements one of the conditions holds, then we return `True`.

## Part 2 

I took used the brute force approach. For each `report` list, I computed all _dampened reports_ where one element is removed from the list. For example the report `[7, 6, 4, 2, 1]` becomes the following `dampened_reports`
```
[6, 4, 2, 1]
[7, 4, 2, 1]
[7, 6, 2, 1]
[7, 6, 4, 1]
[7, 6, 4, 2]
```
Then I used my `is_safe()` function from part 1 to check if any are safe.

I'm very confident there is a more efficient way to do this. I suspect there is an `O(n)` algorithm where you can somehow iterate through `[7, 6, 4, 2, 1]` once to precompute some intermedary, which makes the problem easy to solve. But I'm going to move onto more interesting problems.
