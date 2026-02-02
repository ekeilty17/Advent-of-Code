# Day 8: I Heard You Like Registers

[Problem Link](https://adventofcode.com/2017/day/8)

## Part 1 and Part 2

The problem just requires you to simulate each instruction correctly, which will take the shape of this code in some form

```python
for operation, condition in instructions:
    if execute_condition(registers, condition):
        execute_operation(registers, operation)
```

Now the functions `execute_condition()` and `execute_operation()` just have to be properly implemented. You can see my implementation in `part_1.py`.