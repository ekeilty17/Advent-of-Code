# Day 12: Christmas Tree Farm

[Problem Link](https://adventofcode.com/2025/day/12)

## Part 1


Before I talk about the solution, I want to talk about all of the things that do not work when trying to solve this problem. 

### The Complexity of the Problem

First, the search space is ridiculously large. Each present shape can have up to 8 different orientations (in this problem's input, there are `22` unique shapes after rotations and reflections). The brute force search approach means you have to iterate over every cell in the region to see if each unique present shape fits. Approximating that's around $20 \times 50 \times 50 = 5000$ checks per iteration. Then we have to try and fit approximately $50 + 50 + 50 + 50 + 50 = 250$ presents. So that's a search space of about $5000^{250} \approx 10^{900}$. The brute force approach is implemented in `part_1_slow.py`.

So my next thought was to see if is there some dynamic programming or caching approach. And I think the answer is also no. Because the present shapes are irregular, there is no way to break the problem down into sub-problems For example, suppose I was given all possible ways to fill a `25x25` grid...how does that help me determine if I can fill a `50x50` grid for a certain quantity of presents? Firstly, that number is probably huge. Secondly, in general there is no efficient way to patch together the `25x25` grids because the borders are irregular and could require complex iterlocking.

So all this leaves us with is to come up with pruning methods. And that turns out to be the key.

### The Solution

It turns out, we have a well-behaved input and there are 2 simple pruning checks solve all inputs.

1) There are so few presents, that no interlocking is required to fit inside the region. So essentially you can treat all of the presents as `3x3` squares and check if `N` of these squares fit inside the region.

2) There are too many presents such that even with perfect interlocking, leaving no gaps, they still would not fit in the region.

All inputs fall into these two buckets. And these are very simple to compute. See the functions `fit_without_interlocking()` and `too_large_to_fit()` inside `part_1.py` for the implementations.

Personally, I don't love when the solution is tailored towards the input, but I do believe this was the intended solution. I also find it annoying that the solution does not work on the example input.