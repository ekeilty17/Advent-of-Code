# Day 5: How About a Nice Game of Chess?

[Problem Link](https://adventofcode.com/2016/day/5)

## Part 1

This is a problem that you just have to brute-force and simulate as described by the problem. See `part_1.py` for the details. I used `hashlib` to calculate the MD5 hash.

## Part 2 

Again, just brute-force and simulate. In part 2, password is now an array of fixed length and we use the first non-zero value of the hash to index it.