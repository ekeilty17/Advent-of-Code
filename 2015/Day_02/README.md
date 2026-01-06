# Day 2: I Was Told There Would Be No Math

[Problem Link](https://adventofcode.com/2015/day/2)

## Part 1

The problem essentially gives us the formula to compute the answer. The key to the problem is to sort the length, width, height in ascending order. In python, we can do this as follows
```python
l, w, h = list(sorted([l, w, h]))
```

Now `l` is the smallest dimension, and `w` is the second smallest dimension. The rest of the problem is simply the formula
```python
total_wrapping_paper += surface_area(l, w, h) + l * w
```

## Part 2 

Exactly the same as part 1, just a different formula
```python
l, w, h = list(sorted([l, w, h]))
total_ribbon += volume(l, w, h) + 2*l + 2*w
```