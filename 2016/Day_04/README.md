# Day 4: Security Through Obscurity

[Problem Link](https://adventofcode.com/2016/day/4)

## Part 1

This could probably be solved in 1 or 2 lines using [collections.Counter](https://docs.python.org/3/library/collections.html#collections.Counter), but I decided to code it by hand. The `is_real_room()` function counts the frequencies of each character and gets the top 5 most frequent characters as the checksum. Then it compares the actual checksum to the reported checksum.

## Part 2 

First you have to write the `apply_shift_cypher()` function to iteratively decrypt each message. After that, it's just trial-and-error. I iterated over each room and apply `apply_shift_cypher()` to all of them and looked at the output. Eventually I found `northpole` is the secret phrase we are searching for.