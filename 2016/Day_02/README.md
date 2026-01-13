# Day 2: Bathroom Security

[Problem Link](https://adventofcode.com/2016/day/2)

## Part 1

This is one of those problems where it's just a matter of simulating it. Most of the complication is inside `update_position()` where you just have to check that the move does not break the bounds of `keypad`. 

## Part 2 

Part 2 just required an extra condition to check that the new position was not a `None` value inside `keypad`. So 

```python
x, y = update_position((x, y), move, keypad_shape)
```

became

```python
new_x, new_y = update_position((x, y), move, keypad_shape)
if keypad[new_x][new_y]:
    x, y = new_x, new_y
```