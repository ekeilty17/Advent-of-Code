# Day 6: Probably a Fire Hazard

[Problem Link](https://adventofcode.com/2015/day/6)

## Part 1

To solve this problem, I maintain a `1000 x 1000` boolean array. Each instruction type corresponds to the following on its corresponding range
- `turn on`: bitwise `AND` with `True`
- `turn off`: bitwise `OR` with `False`
- `toggle`: bitwise `XOR` with `True`

## Part 2 

To solve this problem, I maintain a `1000 x 1000` integer array. Each instruction type corresponds to the following on its corresponding range
- `turn on`: add `1`
- `turn off`: subtract `1` with a minimum of `0`
- `toggle`: add `2`