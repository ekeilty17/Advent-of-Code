# Day 14: Chocolate Charts

[Problem Link](https://adventofcode.com/2018/day/14)

## Part 1

The problem describes a process which iteratively generates a pseudo-random sequence of numbers. The solution to part 1 is just implementing this process as described by the problem. The stop condition is if the `recipe_scores` list grows large enough so that we could return the `10` recipe scores **after** the puzzle input. I don't have much to say. See `part_1.py` for my implementation.

## Part 2 

Part 2 is similar to part 1, except there is a different stop condition. The solution to part 2 is the index of the first instance of a given target sub-sequence within the generated sequence.

I imagine a common mistake would be to do an update step, but only check the last `n` elements for the target sub-sequence. The update step in general adds more than 1 score. So you just have to make sure you check all of the new sub-sequences produced. In my implementation in `part_2.py`, this is the purpose of the `for-loop` inside the `while-loop`.

An alternative implementation could have been iterating over `new_recipe_scores` and appending them one at a time. Then naively checking the last `n` elements would work.