# Day 10: Elves Look, Elves Say

[Problem Link](https://adventofcode.com/2015/day/10)

## Part 1 and Part 2 

I just implemented `look_and_say_step()` in `part_1.py`, which calculates the next Look-and-Say number exactly how you would by hand. This approach is fast enough to solve both parts in seconds.

## Improvements

I know the Look-and-Say numbers are highly recursive. So if we can identify sub-pattern which we have already seen, then we can extract them without computing them. I may come back to this problem another time and try to improve it.