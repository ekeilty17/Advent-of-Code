# Day 1: No Time for a Taxicab

[Problem Link](https://adventofcode.com/2016/day/1)

## Part 1

This definitely takes some explaining. Firstly, I converted instructions such as `L5` and `R13` into `-5` and `+13`, respectively. Now one key insight is to realize the even indices respresent you moving in the East/West direction and odd indices represent you moving in the North/South direction.

Let's define going North and going East as moving in the positive direction. If we are facing North, then `R13` moves us to the East. If we are facing East, then `R13` represents going South. So to keep our convension, we actually need to flip the signs of all North/South directions. This is the purpose of 
```python
instructions = [-x if i % 2 else x for i, x in enumerate(instructions)]
```

This allows for an elegant solution. Because we are using the [Traxicab distance](https://en.wikipedia.org/wiki/Taxicab_geometry) `blocks = abs(horizontal_blocks) + abs(vertical_blocks)`, we don't have to split up horizontal and vertical displacement into 2 case. We just need to maintain the variable `orientation`, which is `+1` if we are facing North or East, and `-1` if we are facing South or West. Now, the direction we move is equal to the relative direction given by the sign of the instruction times our orientation
```python
blocks += orientation * instruction
```

And we update the orientation similarly
```python
orientation *= 1 if instruction > 0 else -1
```

## Part 2 

In part 2 we modify part 1 to keep track of both the horizontal and vertical displacement. Now, `blocks = [0, 0]` and we use `blocks[i%2]` to index horizontal/vertical displacements.

Another difference is instead of doing `blocks[i%2] += orientation * instruction`, we determine the direction `direction = 1 if orientation * instruction > 0 else -1` and then step one block at a time
```python
for _ in range(abs(instruction)):
    blocks[i%2] += direction
```
keeping track of each block that we have visited using a set. If we ever repeat, then we return.