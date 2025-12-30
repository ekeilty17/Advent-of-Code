# Day 8: Resonant Collinearity

[Problem Link](https://adventofcode.com/2024/day/8)

## Part 1

Once you understand the problem the algorithm is fairly straight-forward

1. **Initialize** `A` as the set of unique antinode locations
2. **For each** unique frequency `f`
    1. **For each** unique pair of antennas with frequency `f`
        1. Let `(i1, j1)` and `(i2, j2)` be the antenna locations
        2. Let `di, dj = (i2 - i1), (j2 - j1)`
        3. The antinode locations are `(i1 - di, j1 - dj)` and `(i2 + di, j2 + dj)`
        4. If those antinodes are in bounds of the map, add those locations to the set `A`
3. **Return** `A.length`

In steps 2, we are computing the distance between the antenna locations. In step 3, we just mirroring those locations on either side of the antennas.

In my code I was a bit more clever and I just did
```python
for i1, j1 in antenna_locations:
    for i2, j2 in antenna_locations:
```

This will repeat location pairs, but in opposite order. I use this to my advantage and only compute 1 direction of antinodes as the other direction will be computed in the subsequent iteration. I think it makes the code a bit cleaner.

It's important that `A` is a set and not a list or just a counter as we don't want to double count the same antinode locations.

## Part 2 

Part 2 is a similar idea, except step 3 is replaced by a loop which keeps stepping down the map by increments of `(di, dj)`, adding antinodes at each location. 

Another important difference is that

> an antinode occurs at any grid position exactly in line with at least two antennas of the same frequency.

Effectively, this means that every antenna is now also an antinode. So now, we just also add each antenna location to the set `A`.