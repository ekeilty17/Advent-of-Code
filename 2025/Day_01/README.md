# Day 1: Secret Entrance

[Problem Link](https://adventofcode.com/2025/day/1)

## Data Loading

The data is given as `L68` to mean "turn left by 68" and `R45` to mean "turn right by 45". In my data loader, I converted them to integers to make them easier to work with, i.e. `-68` and `+45` respectively.

## Part 1

Fairly straight-forward solution
1. **Initialize** dial `d = 0`
2. **Initialize** counter `c = 0`
3. **For each** rotation `r`
    1. Simulate the rotation of the dial: `d = (d + r) % 100`
    2. **If** `d == 0` **then** increment counter `c`

I was wondering if the dial starting at `0` should count towards the total. But I don't think this edge case was ever tested.

## Part 2

### Brute Force Solution

Now we have to check every time the dial ever crosses `0`. The brute force way is the following
1. **Initialize** dial `d = 0`
2. **Initialize** counter `c = 0`
3. **For each** rotation `r`
    1. Increment the dial `d` 1 step for a total of `r` times
    2. **If** the dial `d` is ever `0` **then** increment counter `c`

### Mathematical Solution

Alternatively, we can solve this with a bit of math. The "tricky" part is that in a single rotation we can cross `0` multiple times. In the full input we see instructions like `L549`. So we just need to do the proper modular arithmetic. Now the algorithm is
1. **Initialize** dial `d = 0`
2. **Initialize** counter `c = 0`
3. **For each** rotation `r`
    1. Increment counter `c` by `|(d + r) // 100|`
    2. Assign `d = (d + r) % 100`
    3. _some corrections if `d == 0`_

These _corrections `d == 0`_ are to making sure you don't double count when the dial stops at `0`. Look at the code if you want to see those details.
