# Day 1: No Time for a Taxicab

[Problem Link](https://adventofcode.com/2016/day/1)

## Part 1

This definitely takes some explaining. Firstly, I converted instructions such as `L5` and `R13` into `-5` and `+13`, respectively. Now one key insight is to realize the even indices respresent you moving in the East/West direction and odd indices represent you moving in the North/South direction.

Let's define going North and going East as moving in the positive direction. If we are facing North, then `R13` moves us to the East. If we are facing East, then `R13` represents going South. So to keep our convension, we actually need to flip the signs of all North/South directions. This is the purpose of 
```python
instructions = [-x if i % 2 else x for i, x in enumerate(instructions)]
```

Let `blocks = [0, 0]` where `blocks[0]` is the horizontal displacement and `blocks[1]` is the vertical displacement. Additionally, we need to maintain the variable `orientation`, which is `+1` if we are facing North or East, and `-1` if we are facing South or West. Now, the direction we move is equal to the relative direction given by the sign of the instruction times our orientation
```python
blocks[i%2] += orientation * instruction
```

And we update the orientation similarly
```python
orientation *= 1 if instruction > 0 else -1
```

## Part 2 

Part 2 is similar to part 1, except we have to step one by one through each instruction, i.e.
```python
direction = 1 if orientation * instruction > 0 else -1
for _ in range(abs(instruction)):
    blocks[i%2] += direction
```
Using a [set](https://en.wikipedia.org/wiki/Set_(abstract_data_type)) to store all past locations, at each step we check if we've visited `blocks` before. If we find a duplicate, then we return.