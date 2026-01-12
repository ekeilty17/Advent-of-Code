# Day 19: Medicine for Rudolph

[Problem Link](https://adventofcode.com/2015/day/19)

## Part 1

First, I wrote the function `parse_elements()` which converts the molecule string into its list of elements, for example `parse_elements("PTiMg") --> ["P", "Ti", "Mg"]`. Now, the goal to get all possible distinct elements that we can fabricate by a single replacement. To do this, I just iterate over this element list and do every possible replacement at each index. For example, the first element `P` can be replaced by `CaP`, `PTi`, or `SiRnFAr`. Therefore, just replacing that index results in the following molecules `["CaPTiMg", "PTiTiMg", "SiRnFArTiMg"]`. Each of the fabricated molecules are stored in a set to remove duplicates.

## Part 2 

This problem relies on a cooperative input. Doing a complete brute force search takes way too long as the search space is way too large. It turns out, if you take the greedy approach and just replace the largest molecules first, you arrive at the optimal solution. This is not true in general and it's easy to come up with counter examples. 

First, I do my search backwards. Instead of starting from `e` and additively replace to create the target molecule, I start at the target molecule and subtractively replace to get back to `e`. This reverse mapping is the dictionary `elements_by_replacement`.

Then, my code implements a [Depth-First Search](https://en.wikipedia.org/wiki/Depth-first_search) where we traverse the largest replacements first. Then I just return the first time that I hit `e` and assume it's optimal. I don't love it, but it solves the problem I guess.