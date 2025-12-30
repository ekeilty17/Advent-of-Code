# Day 11: Plutonian Pebbles

[Problem Link](https://adventofcode.com/2024/day/11)

## Part 1

I implemented the brute-force solution for part 1. Simulating a **blink** just means iterating over each stone and calling the `apply_stone_rules()` function. Then we just call the `blink()` function `25` times.

## Part 2 

Attempting to blink `75` times with the brute-force part 1 solution is not going to work. I suspect the number of stones grows exponentially due to the _split in two_ rule.

The trick to this problem is the following observations
1. Each stone is independent of the others. So you don't have to blink the list of stones together, you can blink each stone individually and sum the total
2. Due to the _split in two_ rule, you will often get the same stone values over and over again

Lots and lots of repeated sub-problems is a perfect application of dynamic programming. I took the lazier approach and just memoized past sub-problems using the tuple `(stone_value, blinks_remaining)` as the key. I couldn't figure out a great way to do a bottom-up approach since the _multiply by 2024_ rule causes large and sparse stone values.
