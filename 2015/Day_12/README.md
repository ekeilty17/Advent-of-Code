# Day 12: JSAbacusFramework.io

[Problem Link](https://adventofcode.com/2015/day/12)

## Part 1

You probably could have solved part 1 by loading the JSON object and recursively traversing, but why over-complicate things. Instead, I just extracted all integers using the regex pattern `r'[+-]?\d+'`, and returned the sum.

## Part 2 

In this problem, we do have to load the JSON object and recursively traverse. During the traversal, for every object we just have to check if it has type `"red"`. If it does, I replaced the entire object with `{}`. 

Now, I have a JSON object with all of the `"red"` numbers removed. So, I re-encoded this object as a JSON string, and used my code from part 1 to sum all integers.