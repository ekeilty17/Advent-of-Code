# Day 12: Subterranean Sustainability

[Problem Link](https://adventofcode.com/2018/day/12)

## Part 1

This is a classic Cellular Automaton question with a small twist. It's essentially a 1D version of the convolution, which was implemented in Day 11.

Using the example, my algorithm works as follows. Given the initial state `#..#.#..##......###...###`, first I add empty plants as padding to each side

```
    #..#.#..##......###...###
....#..#.#..##......###...###....
```

Now, I iterate over every contiguous set of `5` plants. Using the state transitions from the input, I determine if that tuple maps to `.` or `#`. I iteratively construct the new state.

```
[....#]..#.#..##......###...###....     -->     .
.[...#.].#.#..##......###...###....     -->     ..
..[..#..]#.#..##......###...###....     -->     ..#
...[.#..#].#..##......###...###....     -->     ..#.
....[#..#.]#..##......###...###....     -->     ..#..
....#[..#.#]..##......###...###....     -->     ..#..
....#[..#.#]..##......###...###....     -->     ..#...
....#.[.#.#.].##......###...###....     -->     ..#...#
etc
```

This process would continue until I get the final new state `..#...#....#.....#..#..#..#.`. Then, to prevent unnecessary computation, I trim off excess `.`. So the final updated state would be 
```
#...#....#.....#..#..#..#
```

The final complication of this problem is we have to keep track of the pot indices. To do this, I just keep track of the index of the **left-most pot** in the final updated state. After the original automata update, the left-most pot will have decreased by `2` (since the context size is `5`, which will always result in `5//2 = 2` extra cells). Then, the left-most pot may increase due to removal of excess `.`. See the function `update_state()` in `part_1.py` for the full implementation.

## Part 2 

Part 2 is the same as part 1, except instead of 20 generations it asks to compute 50 billion. This is obviously way too large to brute force. After experimentation, you will notice that after 94 generations the input reaches a **fixed point**. 

```
##......##...........##.....##......##.....##........................##.....##.....##....................##...................##
```

calling the function `update_state()` results in the same state. 

All that is left is to compute how the leftmost pot index changes. In this case, the leftmost pot actually keeps increasing by 1. So actually, this is not _exactly_ the same state. It's the same state, but shifted to the right by 1. This is the purpose of the line

```python
leftmost_pot += leftmost_pot_difference * (num_generations - k - 1)
```

I believe this solution is input-specific. In general I believe it is possible that the solution cycles over many states rather than reaches a single fixed point. 