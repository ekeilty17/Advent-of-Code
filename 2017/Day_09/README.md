# Day 9: Stream Processing

[Problem Link](https://adventofcode.com/2017/day/9)

## Part 1

It took me a second to get my head around what the problem was asking. The up-shot is that the `score` of each group is the **nesting depth** of that group.

So this means, I can iterate linearly over the string and just keep track of how many open `{` I've seen. Every time I see a `}`, I add the nesting depth to the total score, and then decrement the nesting depth
```python
score += group_nesting_depth
group_nesting_depth -= 1
```

Finally, you just have to account for **garbage** characters (`<>`) and the **ignore** character (`!`). When you see `!`, just skip over the next character. To account for garbage, I just have a boolean. If I ever see `<`, then the boolean is set to `True` in which case all characters except `!` and `>` are ignored. You can see my full implementation in `part_1.py`.

## Part 2 

Mostly the same as part 1. Increment a counter any time `is_garbage` is `True` and the next character is not `>`.