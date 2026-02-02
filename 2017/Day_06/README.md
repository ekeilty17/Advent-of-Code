# Day 6: Memory Reallocation

[Problem Link](https://adventofcode.com/2017/day/6)

## Redistribution

The slow way to code this problem would be to iteratively add `1` block to each bank one by one. Something like
```python
memory[max_bank] = 0
for i in range(max_blocks):
    memory[(max_bank + 1 + i) % len(memory)] += 1
```

The runtime of each iteration in this implementation is `O(max_blocks)`.

Instead, we can compute how many blocks each bank is redistributed.
```
redistribution = max_blocks // len(memory)
extra = max_blocks % len(memory)
```

`redistribution` is the number of blocks that each bank is getting at minimum. Then `extra` is the overflow which we iterate one by one
```python
for i in range(extra):
    memory[(max_bank + 1 + i) % len(memory)] += 1
```

Except now, the runtime of each iteration is `O(len(memory))` since by definition `extra < len(memory)`. And to be more accurate, the runtime is actually `O( min{max_blocks, len(memory)} )`. So this is strictly better than the naive algorithm.

## Part 1

For part 1, we just simulate the redistribution until we find a memory configuration which we have seen before. Originally I implemented this as a set, but for part 2 I implement it as a dictionary, keeping track of the iteration at which this configuration occurred. The solution is to return the length of the memory history.

## Part 2 

The exact same as part 1, except we want to return how many steps occurred between the duplicate memory configuration and the length of the memory history.