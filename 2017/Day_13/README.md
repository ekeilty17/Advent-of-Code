# Day 13: Packet Scanners

[Problem Link](https://adventofcode.com/2017/day/13)

## Part 1

We need to write a function `is_caught_at_picosecond()` which checks whether the scanner is at position `0` at time `picosecond`. In part 1, I wanted to write a function which `get_scanner_position()` which can compute the exact scanner position at any time step. This is actually a much stronger constraint than we need, and we will discuss the faster approach in part 2.

Let's explain my implementation of `get_scanner_position()` in `part_1.py`.

The scanner cycle is a little bit deceptive. Let's take this as an example
```
[S]     [ ]     [ ]     [ ]     [ ]     [ ]     [S]
[ ]     [S]     [ ]     [ ]     [ ]     [S]     [ ]
[ ]     [ ]     [S]     [ ]     [S]     [ ]     [ ]
[ ]     [ ]     [ ]     [S]     [ ]     [ ]     [ ]
```

Even though the scanner range is length `4`, the cycle is length effectively of length `3`, but just offset. To illustrate this, let's write down the scanner indices.
```
| 012 | 321 | 012 | 321 |
```

So, to compute the scanner position, we compute
```python
position = picosecond % (scan_range - 1)
```

But if we are on an even cycle, then the indices are flipped. So we just need to add the correction
```python
if (picosecond // (scan_range-1)) % 2:
    position = (scan_range-1) - position
```

And now the problem is easy. We can compute the scanner position at every picosecond, check when its position is 0 (i.e. if we got caught), and compute the severity. We don't even necessarily have to do this in sequential order!

## Part 2 

To know whether we got caught, we actually don't care about the scanner's position; we only care when it's at position `0`. The trick to making the function `is_caught_at_picosecond()` faster is to convert the "bouncing" behavior into true cycling. Using the example from part 1, we can convert it into the following system.

```
[S]     [ ]     [ ]     [ ]     [ ]     [ ]     [S]
[ ]     [S]     [ ]     [ ]     [ ]     [ ]     [ ]
[ ]     [ ]     [S]     [ ]     [ ]     [ ]     [ ]
[ ]     [ ]     [ ]     [S]     [ ]     [ ]     [ ]
[ ]     [ ]     [ ]     [ ]     [S]     [ ]     [ ]
[ ]     [ ]     [ ]     [ ]     [ ]     [S]     [ ]
```

We have duplicated (one less than) the scanner range length and mirrored it. Now instead of bouncing at the bottom, it cycles back to the top.

Now the function implementation is very simple and very fast.
```python
def is_caught_at_picosecond(picosecond, scan_range):
    return picosecond % (2*(scan_range - 1)) == 0
```

Now I just brute force the problem by incrementing the `delay` by one and checking if I ever get caught. 

I was trying to see if there was a more mathematical way to do this. I think there might be some optimizations. Like you could do a more intelligent brute force search. But I don't think there is a closed-form formula that can produce the answer. But I'm happy to be proven wrong!