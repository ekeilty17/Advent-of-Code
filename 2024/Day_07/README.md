# Day 7: Bridge Repair

[Problem Link](https://adventofcode.com/2024/day/7)

## Part 1

The crux of the problem searching through all combinations of operations in which to evaluation the equation. In part 1, I just did a brute force search. I cheated a little bit because I used the `itertools.product` function to get all position combinations of `+` and `*` for the given equation. However, I remedy this sin in part 2.

## Part 2 

Here, the part 1 code does work, but it's a bit slow taking about 15 seconds. Instead I implemented a simple [Depth-First Search](https://en.wikipedia.org/wiki/Depth-first_search) (DFS). The advantage here is I can add a pruning condition. We notice that all three operations (addition, multiplication, and concetenation) and monotonically increasing operations. This means the equation is only going to get larger and larger as we continue to evaluate the expression. Therefore, the DFS lets me add the following check.

```python
if current_result > target_result:
    return False
```

Just by adding this pruning check, the part 2 code now runs in about 3 seconds.
