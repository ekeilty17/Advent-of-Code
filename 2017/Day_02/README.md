# Day 2: Corruption Checksum

[Problem Link](https://adventofcode.com/2017/day/2)

## Part 1

For each row in the spreadsheet, sum `max(row) - min(row)`. Return the total.

## Part 2 

For each row in the spreadsheet, we need to find the unique two values in the row `N > n` such that `N % n == 0`. Then we sum `N // n` in each row and return the total.