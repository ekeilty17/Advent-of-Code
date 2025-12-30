# Day 1: Historian Hysteria

[Problem Link](https://adventofcode.com/2024/day/1)

## Data Loading
I loads the two columns of location IDs into two lists. I will refer to these as the **left list** and **right list**, respectively.

## Part 1

Very straight-forward. Once the example input is correctly loaded it can be solved easily in one line in Python. Just take the difference between the two numbers on each line and sum.

## Part 2

There are a few approaches to this problem that I can think of involving nested for loops. However, we can do better and solve this problem in linear time. The algorithm works as follows

1. Let `C` be a dictionary of the location ID counts in the right list
2. **Initialize** `similarity_score = 0`
3. **For each** `location_id` in the left list
    a. `similarity_score += location_id * C[location_id]`
4. **return** `similarity_score`

Step 1 can be computed in linear time by iterating over the right list. Step 3 can also be computed in linear time by iterating over the left list, since th operation `C[location_id]` is constant. Thus the entire algorithm is `O(n)`.

The other thing to note is it's important that `C` is a dictionary and not a list. Implementing as a list, `C` would have to be `99580` elements long, which would no longer make the algorithm linear with the number of location IDs.
